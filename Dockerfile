FROM python:3.8-alpine
RUN apk add --update gcc libc-dev linux-headers && rm -rf /var/cache/apk/*
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["python", "LCS_bot.py"]
