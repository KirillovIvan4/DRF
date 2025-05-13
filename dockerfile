# Используем официальный slim-образ Python 3.12
FROM python:3.12-slim
# Используем официальный образ Nginx
FROM nginx:latest


# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-pip \
    python3-venv \
    netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Создаем и активируем venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Копируем файл зависимостей и  в контейнер (исправлено: убрана лишняя строка)
COPY requirements.txt .
# Копируем файл конфигурации nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статические файлы веб-сайта в директорию для обслуживания
COPY html/ /usr/share/nginx/html/

# Устанавливаем зависимости Python (исправлено: объединено в один RUN)
RUN pip install --no-cache-dir -r requirements.txt python-dotenv
# Копируем исходный код приложения в контейнер
COPY . .

# Определяем переменные окружения
ENV CELERY_BROKER_URL='redis://localhost:6379'
ENV CELERY_BACKEND='redis://localhost:6379'

# Создаем директорию для медиафайлов
RUN mkdir -p /app/media
RUN adduser --disabled-password --gecos '' --uid 1000 celeryuser && \
    chown -R celeryuser /app

# Пробрасываем порт, который будет использовать Django
EXPOSE 8000
# Открываем порт 80 для HTTP-трафика
EXPOSE 80

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]