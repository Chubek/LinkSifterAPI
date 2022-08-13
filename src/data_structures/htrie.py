import enum
from pydantic import BaseModel
from typing import Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar, Union
from __future__ import annotations
import json
from .addr_key import AddrKey
from .data_html import DataHTML


class HTrieNode(BaseModel):
    children: List[Optional[HTrieNode]] = []
    is_terminal: bool = False
    value: DataHTML = DataHTML.default()
    __next_iter = 0

    @classmethod
    def from_size(
        cls,
        length: int
    ) -> HTrieNode:
        node = cls()

        cls.children = [None]*length

        return cls

    def __getitem__(self, idx: int) -> Optional[HTrieNode]:
        return self.children[idx]

    def __setitem__(self, idx: int, value: Optional[HTrieNode]):
        self.children[idx] = value

    def __len__(self) -> int:
        return len(self.children)

    def __add__(
        self,
        other: List[Optional[HTrieNode]]
    ) -> HTrieNode:
        self.children = self.children + other

        return self

    def __iter__(self) -> HTrieNode:
        self.__next_iter = -1
        return self

    def __next__(self) -> HTrieNode:
        self.__next_iter += 1

        if self.__next_iter >= len(self.children):
            raise StopIteration

        return self.children[self.__next_iter]


class HTrie(BaseModel):
    root = HTrieNode()

    def get_array_index(
        self,
        word: str,
        length: int,
    ) -> int:
        char_hash = self.hash_char(word)

        return char_hash % length

    def insert(
        self,
        addr: AddrKey,
        value: DataHTML
    ):
        root = self.root

        for key in addr:
            ind = self.get_array_index(
                key,
                len(root),
            )

            if len(root) >= ind or root[ind] is None:
                root[ind] = HTrieNode()

            root = root[ind]

        root.is_terminal = True
        root.value = value

    def search(
            self,
            addr: AddrKey
    ) -> Optional[DataHTML]:

        root = self.root

        for key in addr:
            if root.is_terminal:
                break

            ind = self.get_array_index(
                key,
                len(root),
            )

            if len(root) >= ind or root[ind] is None:
                return None

            root = root[ind]

        return root.value

    def __getitem__(self, key: AddrKey) -> DataHTML:
        return self.search(key)

    def __setitem__(self, key: AddrKey, value: DataHTML):
        self.insert(key, value)

    @staticmethod
    def hash_char(word: str) -> int:
        ord_ch = [ord(ch) for ch in word]
        bin_int = sum([[int(c) for c in
                        list(f"{orded:08b}")]
                       for orded in ord_ch
                       ], [])
        bin_inv = [i ^ 1 for i in bin_int]

        def bin_to_int(ls: List[int]) -> int:
            res = 0

            for i, b in enumerate(ls):
                res += i * (2**b)

            return res

        return bin_to_int(bin_inv)
