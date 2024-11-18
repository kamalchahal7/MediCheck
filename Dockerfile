FROM python:3.12

WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install --no-cache-dir -r /code/requirements.txt

# Model is not a part of release (dev side to build models)
COPY /Release/ /code/

EXPOSE 5000

ENV FLASK_APP=Release.app
ENV FLASK_ENV=development

# Based on default localhost and port for flask (127.0.0.1:5000)
CMD ["flask","run","--host=127.0.0.1","--port=5000","--no-reload"]
