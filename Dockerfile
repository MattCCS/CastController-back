FROM python:3.9-slim

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app

ENV PYTHONPATH /app
ENV FLASK_APP castcontroller/server.py
ENV FLASK_ENV development

CMD ["flask", "run", "--host=0.0.0.0", "--port=11001"]
