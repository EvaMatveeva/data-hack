FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY fill_tables.py fill_tables.py

CMD ["python", "fill_tables.py"]
