FROM python:3.10.7-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", ":8000", "oc_lettings_site.wsgi:application"]

#CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT