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


class HTrie(BaseModel):
    root = HTrieNode()

    def get_array_index(
        self,
        char: str,
        length: int,
    ) -> int:
        char_hash = self.hash_char(char)

        return char_hash % length

    def insert(
        self,
        addr: AddrKey,
        value: DataHTML
    ):
        key_str = str(addr)
        length = len(key_str)

        root = self.root
        is_still_root = True

        if len(root) < length:
            root: HTrieNode = root + ([None] * length - len(root))
            self.root = root

        for i, ch in enumerate(key_str):
            length = len(root)
            ind = self.get_array_index(ch, length)

            if root[ind] is None:
                root[ind] = HTrieNode.from_size(length - i)
                if is_still_root:
                    self.root = root

            root = root[ind]
            is_still_root = False

        root.value = value
        root.is_terminal = True

    def search(
            self,
            addr: AddrKey) -> Optional[DataHTML]:
        key_str = str(addr)

        root = self.root
        length = len(root)

        for ch in key_str:
            length = len(root)
            ind = self.get_array_index(ch, length)

            curr_node = root[ind]

            if curr_node is None:
                return None

            if curr_node.is_terminal:
                break

            root = curr_node

        return root.value

    def __getitem__(self, key: AddrKey) -> DataHTML:
        return self.search(key)

    def __setitem__(self, key: AddrKey, value: DataHTML):
        self.insert(key, value)

    @staticmethod
    def hash_char(ch: str) -> int:
        ord_ch = ord(ch)
        bin_int = [int(c) for c in
                   list(f"{ord_ch:08b}")]
        bin_inv = [i ^ 1 for i in bin_int]

        def bin_to_int(ls: List[int]) -> int:
            res = 0

            for i, b in enumerate(ls):
                res += i * (2**b)

            return res

        return bin_to_int(bin_inv)
