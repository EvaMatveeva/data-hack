FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY create_tables.py create_tables.py

CMD ["python", "create_tables.py"]
