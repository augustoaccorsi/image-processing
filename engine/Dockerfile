FROM python:3

ENV FLASK_ENV=prod

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
RUN pip install numpy
RUN pip install requests-toolbelt
RUN pip install gunicorn

ENTRYPOINT ["python"]
CMD ["run.py"]
