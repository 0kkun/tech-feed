FROM python:3.12-slim

ENV TZ=Asia/Tokyo

RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY cron/crontab /etc/cron.d/tech-feed
RUN chmod 0644 /etc/cron.d/tech-feed && crontab /etc/cron.d/tech-feed

CMD ["sh", "-c", "env >> /etc/environment && cron -f"]
