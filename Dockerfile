FROM python:3.9

WORKDIR /app

COPY main.py .

COPY requirements.txt .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]