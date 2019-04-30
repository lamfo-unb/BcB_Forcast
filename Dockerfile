FROM python:3.7
MAINTAINER Carlos Aragon "carloseraragon@gmail.com"
COPY . /app
WORKDIR /app

RUN pip install -r requirements
CMD ["app.py"]
