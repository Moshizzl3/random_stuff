FROM python:3.9

WORKDIR /app/src

COPY . /app/src/

RUN apt-get update && \
    apt-get install -y iputils-ping && \
    pip install -r requirements/requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app","--host", "0.0.0.0","--port", "8000"]