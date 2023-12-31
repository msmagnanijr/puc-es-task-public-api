FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP app.py

EXPOSE 6000

CMD ["flask", "run", "--host=0.0.0.0", "--port=6000"]
