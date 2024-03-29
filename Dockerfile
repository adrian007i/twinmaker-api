From python:3.11-slim

RUN mkdir /app
WORKDIR /app

RUN pip install flask-socketio boto3 flask-cors

COPY . .

ENV PYTHONBUFFERED 1

EXPOSE 5000

STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["app.py"]