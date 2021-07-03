FROM python:3.8.5
LABEL maintainer="John Yauyo"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
