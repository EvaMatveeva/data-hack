# Imports

from sqlalchemy import create_engine
import pandas as pd
from faker import Faker
from datetime import date, datetime, timedelta
import random

fake = Faker()

# Creating dfs
df_company = pd.DataFrame(columns=['id', 'name', 'created_at'])
df_employee = pd.DataFrame(columns=['first_name', 'last_name', 'company_id', 'phone', 'start_at', 'end_at'])

# Filling the dfs
# df_company
for i in range(500):
    l = [i + 1, fake.company(), fake.date()]
    df_company.loc[i] = l

# df_employee
n = len(df_company) * 3
for j in range(n):
    first_name = fake.first_name()
    last_name = fake.last_name()
    company_id = random.choice(df_company['id'])
    phone = fake.phone_number()
    created_at = df_company[df_company['id'] == company_id]['created_at'].values[0]
    start_at = fake.date_between(
        start_date=datetime(*[int(c) for c in created_at.split("-")]).date()
    )
    if start_at + timedelta(days=10) >= date.today():
        None
    else:
        end_at = random.choice([
            fake.date_between(
                start_date=(start_at + timedelta(days=10))
            ),
            None]
        )
    l = [first_name, last_name, company_id, phone, start_at, end_at]
    df_employee.loc[j] = l

engine = create_engine("postgresql://test_user:1234@postgres:5432/sourse_db")

# Creating tables
# df_company
engine.execute("""
CREATE TABLE companies (
    id int not null,
    name varchar(255),
    created_at date
    )
    """)

# df_employee
engine.execute("""
CREATE TABLE IF employees (
    first_name varchar(255),
    last_name varchar(255),
    company_id int,
    phone varchar(50),
    start_at date,
    end_at date
    )
    """)

# Filling tables
df_company.to_sql('companies', con=engine, if_exists='append', index=False)
df_employee.to_sql('employees', con=engine, if_exists='append', index=False)
