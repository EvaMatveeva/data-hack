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


SOURCE_TYPE_TO_READER_CLS = {
    "csv" : CSVReader,
}