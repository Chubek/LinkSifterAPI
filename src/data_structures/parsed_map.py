import enum
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Any, List, Optional, TypeVar, Union, Generic
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
        return json.dumps({
            "val": str(self.val),
            "key": self.key,
            "child_key": self.child_key,
            "next_key": self.next_key,
            "prev_key": self.prev_key,
            "parent_key": self.parent_key,
            "root_key": self.root_key,

        }, indent=4, sort_keys=True)

    def __repr__(self) -> str:
        return str(self)


class ParsedMap(GenericModel, Generic[DataT]):
    hashtable: List[Union[ParsedNode[DataT], None]] = []
    length: int = 0

    def key_function(self, obj: DataT) -> int:
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
                    return self.hashtable[key_index - 1].val
                case False:
                    return self.hashtable[key_index - 1]
        except:
            return None

    def get_addr(
        self,
        key: int,
        directions: List[DirectionTty],
        unwrap=True
    ) -> Optional[Union[ParsedMap, DataT]]:
        key_index = self.hash_function(key)

        try:
            first_level = self.hashtable[key_index - 1]
        except:
            return None

        fin = first_level

        for dir in directions:
            match dir:
                case DirectionTty.Self:
                    fin = fin
                    break
                case DirectionTty.Next:
                    fin_key_next = fin.next_key

                    if fin_key_next is None:
                        break

                    if fin_key_next == -1:
                        break

                    fin = self.get_single(
                        fin_key_next,
                        unwrap=False
                    )
                case DirectionTty.Prev:
                    fin_key_prev = fin.prev_key

                    if fin_key_prev is None:
                        break

                    if fin_key_prev == -1:
                        break

                    fin = self.get_single(
                        fin_key_prev,
                        unwrap=False
                    )
                case DirectionTty.Parent:
                    fin_key_parent = fin.parent_key

                    if fin_key_parent is None:
                        break

                    if fin_key_parent == -1:
                        break

                    fin = self.get_single(
                        fin_key_parent,
                        unwrap=False
                    )
                case DirectionTty.Parent:
                    fin_key_root = fin.root_key

                    if fin_key_root is None:
                        break

                    if fin_key_root == -1:
                        break

                    fin = self.get_single(
                        fin_key_root,
                        unwrap=False
                    )

                case DirectionTty.Child:
                    fin_key_child = fin.child_key

                    if fin_key_child is None:
                        break

                    if fin_key_child == -1:
                        break

                    fin = self.get_single(
                        fin_key_child,
                        unwrap=False
                    )

        match unwrap:
            case True:
                return fin.val
            case False:
                return fin

    def set_key(self,
                val: DataT,
                key: int,
                next_key=-1,
                prev_key=-1,
                child_key=-1,
                parent_key=-1,
                root_key=-1,
                ):
        hash_item = ParsedNode(
            val=val,
            key=key,
            next_key=next_key,
            prev_key=prev_key,
            child_key=child_key,
            parent_key=parent_key,
            root_key=root_key
        )

        hash_val = self.hash_function(key)

        if self.length >= hash_val:
            self.hashtable[hash_val] = hash_item
        else:
            self.hashtable.append(hash_item)
            self.length += 1

    def set_single_object(self, key: int, value: ParsedNode):
        item_index = self.hash_function(key)

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

    def __getitem__(self, key: int) -> ParsedNode:
        self.get_single_object(key)

    def __setitem__(self, key: int, value: ParsedNode):
        self.set_single_object(key, value)

    def __str__(self):
        return

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
