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
RUN pip install psycopg2-binary
RUN pip install gunicorn

ENTRYPOINT ["python"]
CMD ["run.py"]
