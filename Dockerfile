FROM python:3.9-alpine

WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies using a public mirror
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# Copy application code
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
