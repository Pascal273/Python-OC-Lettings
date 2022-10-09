FROM python:3.10.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind :$PORT
