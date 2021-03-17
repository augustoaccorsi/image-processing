import os, subprocess
from app import app, db

env = os.environ['FLASK_ENV']

if __name__ == '__main__':
    if env == 'dev':
        db.create_all()
        app.run(host='0.0.0.0', port="5001", debug=True)
    else:
        subprocess.run(["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "wsgi"],debug=True)