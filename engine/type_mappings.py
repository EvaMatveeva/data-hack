import numpy as np
import pandas as pd

CSV_MAPPING = {
    "int": np.int32,
    "float": np.float32,
    "str": str,
    "bool": bool,
}