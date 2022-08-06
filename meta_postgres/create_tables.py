# Imports

from sqlalchemy import create_engine
import pandas as pd

# Creating meta tables
engine = create_engine("postgresql://test_user:1234@localhost:4321/sourse_db")

engine.execute("""create schema meta""")

engine.execute("""
    create table meta.logging (
    	table_name varchar(255),
    	operation_type varchar(50),
    	log_message text,
    	log_state varchar(50),
    	log_dttm timestamp
    )
    """)

# Other tables 
