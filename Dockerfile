FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
RUN python3 -m pip install --upgrade pip && pip install -r requirements.txt
CMD "/bin/bash"
