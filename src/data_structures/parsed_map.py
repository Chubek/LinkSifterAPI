import enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Any, List, Literal, Optional, Tuple, TypeVar, Union, Generic
from __future__ import annotations
import json

DataT = TypeVar('DataT')


class DirectionTty(str, enum):
    Next = 'next'
    Prev = 'prev'
    Child = 'child'
    Parent = 'parent'
    Root = 'root'
    Self = 'self'


class MutateTty(GenericModel, Generic[DataT]):
    direction: DirectionTty
    val: DataT


class ParsedNode(GenericModel, Generic[DataT]):
    val: DataT
    key: int
    child_key: Optional[int] = -1
    next_key: Optional[int] = -1
    prev_key: Optional[int] = -1
    parent_key: Optional[int] = -1
    root_key: Optional[int] = -1

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self)


class ParsedMap(GenericModel, Generic[DataT]):
    hashtable: List[Union[ParsedNode[DataT], None]] = []
    length: int = 0

    def key_function(
        self,
        obj: Union[DataT, ParsedNode]
    ) -> int:
        return self.make_key_hash(obj)

    def hash_function(self, key: int) -> int:
        return key % self.length

    def get_single(
        self,
        key: int,
        unwrap=True
    ) -> Optional[Union[ParsedMap, DataT]]:
        key_index = self.hash_function(key)

        try:
            match unwrap:
                case True:
                    return self.hashtable[key_index].val
                case False:
                    return self.hashtable[key_index]
        except:
            return None

    
    def set_single_object(self, value: DataT):
        key_inner = self.key_function(value)

        parsed_node = ParsedNode(
            val=value,
            key=key_inner,
            parent_key=None,
            child_key=None,
            next_key=None,
            prev_key=None,
            root_key=None,
        )

        key_outer = self.key_function(parsed_node)
        item_index = self.hash_function(key_outer)

        match 0 <= item_index <= self.length:
            case True:
                self.hashtable[item_index] = value
            case False:
                self.length = item_index

                while len(self.hashtable) <= self.length:
                    self.hashtable.append[None]

                self.hashtable[item_index] = value

    def set_index(
        self,
        index: int,
        object: ParsedNode
    ):
        self.hashtable[index] = ParsedNode

    def get_index(
        self,
        index: int,
        object: ParsedNode
    ) -> ParsedNode:
        return self.hashtable[index]

    def get_single_object(self, key: int) -> ParsedNode:
        item_index = self.hash_function(key)

        return self.hashtable[item_index]

    def mutate(
        self,
        target_key,
        mutate_tty: MutateTty
    ):
        key_item = self.key_function(mutate_tty.val)
        target_index = self.hash_function(target_key)

        match mutate_tty.direction:
            case DirectionTty.Parent:
                parsed_node = self.get_index(target_index)
                parsed_node.parent_key = key_item
                self.set_index(target_index, parsed_node)
            case DirectionTty.Next:
                parsed_node = self.get_index(target_index)
                parsed_node.next_key = key_item
                self.set_index(target_index, parsed_node)
            case DirectionTty.Prev:
                parsed_node = self.get_index(target_index)
                parsed_node.prev_key = key_item
                self.set_index(target_index, parsed_node)
            case DirectionTty.Root:
                parsed_node = self.get_index(target_index)
                parsed_node.root_key = key_item
                self.set_index(target_index, parsed_node)
            case DirectionTty.Child:
                parsed_node = self.get_index(target_index)
                parsed_node.child_key = key_item
                self.set_index(target_index, parsed_node)
            case DirectionTty.Self:
                parsed_node = self.get_index(target_index)
                parsed_node.key = key_item
                self.set_index(target_index, parsed_node)

    def __getitem__(self, key: Tuple[int, bool]) -> ParsedNode:
        self.get_single(key[0], key[1])

        self.get_single_object(key)

    def __setitem__(self, _: Literal['_'], value: ParsedNode):
        self.set_single_object(value)

    def __str__(self):
        return "".join([pn.key 
                for pn in self.hashtable])

    @staticmethod
    def make_key_hash(obj: Any) -> int:
        str_obj = str(obj)

        bins_rev = [int(j) ^ 1 for j in
                    sum([list(f"{x:08b}")
                         for x in str_obj], [])]

        while len(bins_rev) % 8 != 0:
            bins_rev = [0] + bins_rev

        def to_decimal(ls: List[int]) -> int:
            sum = 0

            for i, l in enumerate(ls):
                sum += l * (2**i)

                return sum

        return abs(sum([
            to_decimal(bins_rev[i:i + 8])
            for i in range(0, len(bins_rev), 8)
        ]))
