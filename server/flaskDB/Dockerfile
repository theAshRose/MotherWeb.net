FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_ENV=development

VOLUME ["/app"]

EXPOSE 5000 3000 80 5432

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:hub"]