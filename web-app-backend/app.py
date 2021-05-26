from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageFilter
from io import BytesIO
import urllib, requests, uuid, os


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/engine/mand", methods=['POST'])
def mandelbrot():
    if request.method == 'POST':
                
        url = "http://augusto-accorsi-engine-elb-1884692720.sa-east-1.elb.amazonaws.com:5000/engine/mand?max_iter=&1&width=&2&height=&3"

        width = 500
        height = 500
        max_iter = 500
            
        for command in request.query_string.split(b'&'):
            # Split the command in a key and value
            command_list = command.split(b'=')
            key = command_list[0]
            if key == b'':
                continue
            value = float(command_list[1])

            if key == b'width':
                width = int(value)
            elif key == b'height':
                height = int(value)
            elif key == b'max_iter':
                max_iter = int(value)
        
        session = requests.Session()
        session.trust_env = False
        url = url.replace("&1", str(max_iter))
        url = url.replace("&2", str(width))
        url = url.replace("&3", str(height))
        res = session.post(url)

        return jsonify({
            "call on": url,
            "status code": res.status_code
        }), 201

@app.route("/database/save", methods=['POST'])
def database_save():
    if request.method == 'POST':

        try:
            file = request.files['image']
        except:
            return jsonify({'error': 'No image found with the \'image\' key'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'This file type is not allowed'}), 400

        url = "http://augusto-accorsi-database-elb-1912352354.sa-east-1.elb.amazonaws.com:5001/database"
        
        id = uuid.uuid4().hex

        #res = requests.post(url=url, files={'image': ('file.PNG', file, 'image/png')}, params={'id': id})
        session = requests.Session()
        session.trust_env = False
        #res = session.get(url)
        res = session.post(url=url, files={'image': ('file.PNG', file, 'image/png')}, params={'id': id})

        return jsonify({
            "image_id": id,
            "filename": id+'.png',
            "call on": url,
            "status code": res.status_code
        }), 201

@app.route("/")
def heartbeat():
    return jsonify({'web-app-back v1 heartbeat <3': 'okay'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)