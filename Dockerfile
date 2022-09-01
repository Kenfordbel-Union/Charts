FROM python:3.9.13

COPY ./requirements.txt requirements.txt
RUN python -m pip install --upgrade setuptools pip && pip install -r requirements.txt

COPY . /usr/src/charts
WORKDIR /usr/src/charts

# RUN ["chmod", "+x", "./entrypoint.sh"]
# ENTRYPOINT ["./entrypoint.sh"]
