From python:310

WORKDIR /app

COPY ..

RUN pip insttall --no-cache-dir -r requirements.txt

RUN python manage.py migrate

Expose 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]