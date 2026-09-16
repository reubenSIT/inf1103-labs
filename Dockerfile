FROM python:3.13-slim

WORKDIR /usr/src/app

COPY auditor.py .

CMD ["python", "auditor.py"]