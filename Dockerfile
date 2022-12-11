FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY /task_2 /code
WORKDIR /code/task_2
