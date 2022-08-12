from enum import Enum
from typing import Any
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

with open("settings.yaml") as fs:
    settings_read = yaml.load(fs, Loader=Loader)



class Settings(Any, Enum):
    NERDataSetLoc = settings_read['ConlluFileForNER']