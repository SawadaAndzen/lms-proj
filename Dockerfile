FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

COPY init_user.py /app/

CMD sh -c "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py shell < /app/init_user.py && gunicorn project.wsgi -b 0.0.0.0:8000"