FROM python:3

ENV FLASK_ENV=prod
ENV DATABASE_URI=postgresql://postgres:productionpassword@database-db/postgres

ADD . /code
WORKDIR /code

RUN pip install pipenv
RUN pip install Flask==1.1.2
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
