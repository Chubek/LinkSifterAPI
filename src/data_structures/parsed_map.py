import enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Any, List, Optional, TypeVar, Union, Generic
from __future__ import annotations
from .hash import make_key_hash

DataT = TypeVar('DataT')

class DirectionTty(str, enum):
    Left = 'left'
    Right  = 'right'
    Self = 'self'

class ParsedNode(GenericModel, Generic[DataT]):
    val: DataT
    key: int
    next_key: Optional[int]
    prev_key: Optional[int]
    parent_key: Optional[int]
    root_key: Optional[int]
       

class ParsedMap(GenericModel, Generic[DataT]):
    hashtable: List[Union[ParsedNode[DataT], None]] = []
    length: int = 0

    def key_function(self, obj: DataT) -> int:
        return make_key_hash(obj)
        
   
    def hash_function(self, key: int) -> int:
        return key % self.length

    def get_addr(
        self, 
        key: int, 
        directions: List[DirectionTty]
    ):
        key_index = self.hash_function(key)

        try:
            

    def add(self, 
            val: DataT,
            key: int,
            next_key=-1,
            prev_key=-1,
            parent_key=-1,
            root_key=-1,
        ):
        hash_item = ParsedNode(
            val=val,
            key=key,
            next_key=next_key,
            prev_key=prev_key,
            parent_key=parent_key,
            root_key=root_key
        )

        hash_val = self.hash_function(key)

        if self.length > hash_val:
            self.hashtable[hash_val] = hash_item
        else:
            self.hashtable.append(hash_item)
            self.length += 1

    def __getitem__(self, idx: int) -> DataT:
        self.find(idx)

    def __setitem__(self, idx: int, val: DataT):
        self.add(idx, val) 

    


