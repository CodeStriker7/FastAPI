# 1-bosqich: Build 
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --user -r requirements.txt

# 2-bosqich: Final 
FROM python:3.12-slim

WORKDIR /app

# Root bo'lmagan foydalanuvchi yaratish
RUN useradd -m myuser
USER myuser

# Builder bosqichidan faqat kerakli kutubxonalarni ko'chirib olish
COPY --from=builder /root/.local /home/myuser/.local
COPY . .

# PATH ni yangilash (pip install qilingan kutubxonalar ko'rinishi uchun)
ENV PATH=/home/myuser/.local/bin:$PATH

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]