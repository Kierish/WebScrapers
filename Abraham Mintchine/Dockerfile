FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    libxml2-dev libxslt-dev \
    gcc \
    chromium-driver \
    libx11-xcb1 libxtst6 libnss3 libxrandr2 libasound2 libpangocairo-1.0-0 \
    fonts-liberation libxcomposite1 libxcursor1 xdg-utils \
    libx11-xcb-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUBUFFERED=1

CMD ["python", "abraham.py"]