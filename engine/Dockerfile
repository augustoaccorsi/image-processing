FROM python:3

ADD . /code
WORKDIR /code

RUN pip install pipenv
RUN pip install flask
RUN pip install -U flask_uploads
RUN pip install flask_sqlalchemy
RUN pip install werkzeug==0.16.1
RUN pip install Pillow
RUN pip install requests
RUN pip install uuid
RUN pip install urllib3
RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install opencv-python
RUN pip install numpy

ENTRYPOINT ["python"]
CMD ["run.py"]
