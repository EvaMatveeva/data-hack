from abc import ABC, abstractmethod

import pandas as pd

from type_mappings import CSV_MAPPING


class AbstractReader(ABC):
    def __init__(self, config) -> None:
        super().__init__()
        self.fields = config["fields"]
        self.batch_size = config["batch_size"]

    @abstractmethod
    def read(self):
        pass
    

class CSVReader(AbstractReader):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.file_path = config["file_path"]
        self.dtypes = {k : CSV_MAPPING[v] for k, v in self.fields.items()}

    def read(self):
        # TODO: column from self.fields
        with pd.read_csv(self.file_path, chunksize=self.batch_size, dtype=self.dtypes) as reader:
            for batch in reader:
                yield batch

class PGReader(AbstractReader):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.fields_names = ', '.join(config["fields"].keys())
        self.source_table = config["source_table"]
        self.key_column = config["key_column"]

    def read(self):
        i = 0
        while True:
            SQL = f"""
            select {fields_names} from {source_table} where {key_column} between {i * batch_size} and {(i + 1) * batch_size - 1}
            """
            df = pd.read_sql(SQL, engine)
            if len(df) == 0:
                break
            i += 1
            yield df

SOURCE_TYPE_TO_READER_CLS = {
    "csv" : CSVReader,
    "postgresql": PGReader
}