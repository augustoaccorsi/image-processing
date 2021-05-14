import os, subprocess
from app import app

env = os.environ['FLASK_ENV']

if __name__ == '__main__':
    if env == 'dev':
        app.run(host='0.0.0.0', debug=True)
    else:
        subprocess.run(["gunicorn", "--timeout", "1500", "-w", "4", "-b", "0.0.0.0:3001", "wsgi"])
        
   #    ["gunicorn", "--timeout", "1000", "--workers=1","-b", "0.0.0.0:8000","--log-level", "debug", "manage"]