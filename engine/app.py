from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageFilter
from io import BytesIO
import urllib, requests, uuid
from process.Process import Process


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/transform", methods=['POST'])
def transform_image():
    if request.method == 'POST':

        # Get the image to be transformed, this can be any of the following:
        # - image uploaded as a file
        # - url of a publicaly accessible image
        # - the image_id of an iamge stored in the image_storage microservice
        image = None
        quality = 100

        url = request.form.get('url')
        if url is not None:
            file = BytesIO(urllib.request.urlopen(url).read())
            if not allowed_file(url):
                return jsonify({'error': 'This file type is not allowed'}), 400
            image = Image.open(file)

        image_file = request.files.get('image')
        if image_file is not None:
            if not allowed_file(image_file.filename):
                return jsonify({'error': 'This file type is not allowed'}), 400
            image = Image.open(request.files['image'])

        image_id = request.form.get('image_id')
        if image_id is not None:
            file = BytesIO(urllib.request.urlopen('http://database:5000/images/'+image_id).read())
            image = Image.open(file)

        if image is None:
            return jsonify({'error': 'Could not find an image to transform'}), 400

        # Parse the query string and apply the transformation
        try:
            for command in request.query_string.split(b'&'):
                # Split the command in a key and value
                command_list = command.split(b'=')
                key = command_list[0]
                if key == b'':
                    continue
                value = float(command_list[1])

                # Perform the transform
                if key == b'rotate':
                    image = image.rotate(value, expand=True)
                elif key == b'thumb':
                    iamge = image.thumbnail((value, value))
                elif key == b'compress':
                    quality = min(quality, int(value))
                elif key == b'blur':
                    image = image.filter(ImageFilter.GaussianBlur(value))
        except:
            return jsonify({'error': 'Could not parse filter list: {}'.format(key)}), 400

        # Return the transformed image from memory
        mem_file = BytesIO()
        image.save(mem_file, "JPEG", quality=quality)
        mem_file.seek(0)
        return send_file(mem_file, attachment_filename='_.jpg')

@app.route("/transform/healthcheck")
def healthcheck():
    return jsonify({'service': 'image-transform', 'status': 'okay'}), 200

@app.route("/transform/edge", methods=['GET'])
def process_edge():
    if request.method == 'GET':

        for command in request.query_string.split(b'&'):
            # Split the command in a key and value
            command_list = command.split(b'=')
            key = command_list[0]
            if key == b'':
                continue
            value = command_list[1]

            if key == b'image_id':
                image_id = str(value)[2:]

        if image_id is not None:    
            file = BytesIO(urllib.request.urlopen('http://database:5000/images/'+image_id).read())
            image = Process().edge(file)

            mem_file = BytesIO()
            image.save(mem_file, "JPEG", quality=100)
            mem_file.seek(0)

            id = str(uuid.uuid4().hex)

            requests.post(url='http://database:5000/images/engine', files={'image': ('file.PNG', mem_file, 'image/png')}, params={'id': id})
            
            return jsonify({
                "image_id": id,
                "filename": id+'.png'
            }), 201

        return jsonify({"error": "image_id "+str(image_id)+" not found"}), 404

@app.route("/transform/mandelbrot", methods=['POST'])
def face():
    if request.method == 'POST':

        width = None
        height = None
        max_iter = None
            
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
        
        image = Process().mandelbrot(width, height, max_iter)

        mem_file = BytesIO()
        image.save(mem_file, "PNG", quality=100)
        mem_file.seek(0)
        
        id = str(uuid.uuid4().hex)

        requests.post(url='http://database:5000/images/engine', files={'image': ('file.PNG', mem_file, 'image/png')}, params={'id': id})
        
        return jsonify({
            "image_id": id,
            "filename": id+'.png'
        }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)