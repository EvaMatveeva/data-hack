from reader import SOURCE_TYPE_TO_READER_CLS
from loader import LOAD_TYPE_TO_LOADER_CLS

class Runner:
    def __init__(self, config) -> None:
        source_type = config["source_type"]
        if source_type not in SOURCE_TYPE_TO_READER_CLS:
            raise ValueError(f"Unsupported source_type {source_type}")

        load_type = config["load_type"]
        if source_type not in SOURCE_TYPE_TO_READER_CLS:
            raise ValueError(f"Unsupported source_type {load_type}")

        self.reader = SOURCE_TYPE_TO_READER_CLS[source_type](config)
        self.loader = LOAD_TYPE_TO_LOADER_CLS[load_type](config)

    def run(self):
        for df in self.reader.read():
            self.loader.load(df)
