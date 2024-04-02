from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    product_name: str
    supplier_id: int
    category_id: int
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: int
