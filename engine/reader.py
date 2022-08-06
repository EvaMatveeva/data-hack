from abc import ABC, abstractmethod

SOURCE_TYPE_TO_READER_CLS = {}

class AbstractReader(ABC):
    @abstractmethod
    def read(config):
        pass
