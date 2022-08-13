from __future__ import annotations
from ast import Add
import enum
import json
from bs4 import Tag
from pydantic import BaseModel
from typing import Any, List, Literal, NamedTuple, Optional, Tuple, TypeVar, Union
from .grammar_tty import TagsTty
from ...ner.scoring import NERTty
from .grammar_tty import TagsTty


class AddrKey(BaseModel):
    root_tag: TagsTty = TagsTty.null
    parent_tag: TagsTty = TagsTty.null
    tag: TagsTty = TagsTty.null
    cls_sorted: List[str] = ["default"]
    id: str = "default"
    attribute_keys: List[str] = ["default"]
    ner_tty: NERTty = NERTty.NotEntity
    position: int
    __list_iter: List[str] = []
    __curr_next: int = []

    @classmethod
    def new_default(
        cls,
    ) -> AddrKey:
        return cls()

    @classmethod
    def new(
        cls,
        position: int,
        root_tag: TagsTty = TagsTty.null,
        parent_tag: TagsTty = TagsTty.null,
        tag: TagsTty = TagsTty.null,
        cls_sorted: List[str] = ["default"],
        id: str = "default",
        attribute_keys: List[str] = ["default"],
        ner_tty: NERTty = NERTty.NotEntity,
    ) -> AddrKey:
        return cls(
            root_tag=root_tag,
            parent_tag=parent_tag,
            tag=tag,
            cls_sorted=cls_sorted,
            id=id,
            attribute_keys=attribute_keys,
            ner_tty=ner_tty,
            position=position
        )

    def __iter__(self) -> List[str]:
        self.__list_iter = [
            str(self.root_tag),
            str(self.parent_tag),
            str(self.tag),
            "-".join(sorted(self.cls_sorted)),
            self.id,
            "-".join(sorted(self.attribute_keys)),
            str(self.ner_tty),
            str(self.position)
        ]

        self.__curr_next = -1

        return self

    def __next__(self) -> str:
        self.__curr_next += 1

        if self.__curr_next >= len(self):
            raise StopIteration

        return self.__list_iter[self.__curr_next]

    def __len__(self) -> int:
        return len(self.__list_iter)
