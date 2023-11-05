FROM python

WORKDIR /app

COPY requirements.txt .

COPY . .

CMD ["python", "main.py"]