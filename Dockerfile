FROM python:3

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "pin-manager.py"]
