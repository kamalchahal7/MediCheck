FROM python:3.12

WORKDIR /code

COPY requirements.txt /code/

RUN pip3 install --no-cache-dir -r /code/requirements.txt

# Model is not a part of release (dev side to build models)
COPY /Release/ /code/Release

ENV FLASK_APP=Release/app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

# Based on default localhost and port for flask (127.0.0.1:5000)
CMD ["flask","run","--host=0.0.0.0","--port=5000"]
#"--app","Release.app"
