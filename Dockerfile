FROM python:3.7.5-slim
ENV FLASK_APP=project
ENV FLASK_DEBUG=1
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/app/
WORKDIR /opt/app
CMD python run.py