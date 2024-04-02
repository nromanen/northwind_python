from dataclasses import dataclass
from typing import Optional, List
import sys

sys.path.append(".")
from src.model.product import Product


@dataclass
class Category:
    category_id: int
    category_name: str
    description: str
    picture: memoryview
    products: Optional[List[Product]] = None

    # def __str__(self):
    #     """Returns a string containing only the non-default field values."""
    #     s = ', '.join(f'{field.name}={getattr(self, field.name)!r}'
    #                   for field in dataclasses.fields(self)
    #                   if getattr(self, field.name) != field.default)
    #     return f'{type(self).__name__}({s})'
