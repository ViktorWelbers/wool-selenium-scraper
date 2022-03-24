from pydantic import BaseModel
from pydantic.class_validators import Optional


class Product(BaseModel):
    href: Optional[str]
    name: Optional[str]
    preis: Optional[float]
    nadel_str: Optional[str]
    zusammenstellung: Optional[str]
