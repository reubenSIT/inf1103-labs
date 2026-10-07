FROM python:3.13-slim

WORKDIR /usr/src/app

COPY inventory_manager.py .

CMD ["python", "inventory_manager.py"]