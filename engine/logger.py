from abc import ABC, abstractmethod
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


class AbstractLogger(ABC):
    def __init__(self, config) -> None:
        super().__init__()
        self.source_table = config["source_table"]

    @abstractmethod
    def log(self, operation_type, log_state):
        pass


class Logger(AbstractLogger):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.engine = create_engine("postgresql://test_user:1234@meta_postgres:5432/meta_db")

    def log(self, operation_type, log_state):
        SQL = f"""
        insert into meta.logging 
        select {self.source_table}, {operation_type}, {log_state}, {datetime.now()}
        """
        pd.read_sql(SQL, self.engine)
