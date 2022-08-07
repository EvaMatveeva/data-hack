from abc import ABC, abstractmethod
from sqlalchemy import create_engine
import pandas as pd
from logger import Logger

from type_mappings import CSV_MAPPING


class AbstractReader(ABC):
    def __init__(self, config) -> None:
        super().__init__()
        self.fields = config["fields"]
        self.batch_size = config["batch_size"]
        self.config = config

    @abstractmethod
    def read(self):
        pass
    

class CSVReader(AbstractReader):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.file_path = config["file_path"]
        self.dtypes = {k : CSV_MAPPING[v] for k, v in self.fields.items()}

    def read(self):
        logger = Logger(self.config)
        logger.log("READ", "START")
        try:
            with pd.read_csv(self.file_path, chunksize=self.batch_size, dtype=self.dtypes) as reader:
                for batch in reader:
                    yield batch
            logger.log("READ", "SUCCESS")
        except:
            logger.log("READ", "ERROR")


class PGReader(AbstractReader):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.fields_names = ', '.join(config["fields"].keys())
        self.source_table = config["source_table"]
        self.key_column = config["key_column"]
        self.engine = create_engine("postgresql://test_user:1234@localhost:5432/source_db")

    def read(self):
        logger = Logger(self.config)
        logger.log("READ", "START")
        i = 0
        try:
            while True:
                SQL = f"""
                select {self.fields_names} from {self.source_table} where {self.key_column} between {i * self.batch_size} and {(i + 1) * self.batch_size - 1}
                """
                df = pd.read_sql(SQL, self.engine)
                if len(df) == 0:
                    break
                i += 1
                yield df
            logger.log("READ", "SUCCESS")
        except Exception as e:
            print(e)
            logger.log("READ", "ERROR")


SOURCE_TYPE_TO_READER_CLS = {
    "csv" : CSVReader,
    "postgresql": PGReader
}