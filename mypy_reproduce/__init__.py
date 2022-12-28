from datetime import datetime
from itertools import cycle
from random import choice

from pydantic import BaseModel, validator
from pydantic_factories import ModelFactory, Use


class Item(BaseModel):
    plu_id: str



class Check(BaseModel):
    rtl_txn_id: str
    items: list[Item]

    created: datetime

    def __hash__(self):
        return hash(self.created)


rtl_ids = map(str, cycle(range(1, 1000000)))
item_ids = [str(i) for i in range(1, 1000)]


class ItemFactory(ModelFactory):
    __model__ = Item

    plu_id = Use(choice, item_ids)


class CheckFactory(ModelFactory):
    __model__ = Check

    rtl_txn_id = Use(next, rtl_ids)

    items = Use(ItemFactory.batch, size=1)

