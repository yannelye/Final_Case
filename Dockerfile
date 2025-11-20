FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY assets/ assets/

ENV DATA_PATH=/app/assets
ENV PORT=8080
EXPOSE 8080

RUN python src/pipeline.py

CMD ["python", "src/app.py"]
