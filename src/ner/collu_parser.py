from enum import Enum
from typing import List
from pydantic import BaseModel
import re

class NERTty(str, Enum):
    NotEntity = "0"
    Location = "LOC"
    Misc = "MISC"
    Organization = "ORG"
    Person = "PER"


class NEREntity(BaseModel):
    word: str
    type: NERTty


def parse_collu_get_ner(path: str) -> List[NEREntity]:
    lines = open(path).readlines()

    def make_ner_entity(line: str) -> NEREntity:
        l_split = [l.strip() for l in re.split(r"\s+", line)]

        match l_split[-1]:
            case "O" | '':
                tty = NERTty.NotEntity
            case _:
                tty = NERTty(l_split[-1].split("-")[-1])

        word = l_split[-2]

        return NEREntity(
            word=word,
            type=tty
        )

    return [
        make_ner_entity(l.strip()) 
                for l in lines
                if len(l.strip()) > 0
                and set(l.strip()) != {' '}
                and set(l.strip()) != set()
    ]

    


    
