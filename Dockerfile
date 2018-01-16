FROM python:3
MAINTAINER André Cruz <github_hook@cabine.org>

# first install requirements
RUN apt-get update && apt-get install -y gettext \
 && rm -rf /var/lib/apt/lists/*
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# then include app
ADD . /app

# runtime configuration
WORKDIR /app
RUN django-admin compilemessages
RUN ./manage.py collectstatic --noinput
CMD uwsgi -i uwsgi-production.ini
