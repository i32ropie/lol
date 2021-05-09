FROM python:3.8-alpine
RUN apk add --update py3-psutil py3-lxml && rm -rf /var/cache/apk/* && ln -s /usr/lib/python3.8/site-packages/psutil /usr/local/lib/python3.8/site-packages/psutil && ln -s /usr/lib/python3.8/site-packages/lxml /usr/local/lib/python3.8/site-packages/lxml
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["python", "LCS_bot.py"]
