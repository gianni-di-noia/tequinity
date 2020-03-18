FROM python:3.7.5-slim
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/app/
WORKDIR /opt/app
CMD gunicorn -w 3 project.main:main --log-level=DEBUG