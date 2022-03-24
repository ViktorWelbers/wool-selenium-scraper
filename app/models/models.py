from pydantic import BaseModel
from pydantic.class_validators import Optional


class Product(BaseModel):
    """ Hier koennte man einfach SQL Alchemy mit z.B. einer PG-Datenbank (in Docker aufgesetzt) nutzen um die Modelle dort zu speichern :)"""
    href: Optional[str]
    name: Optional[str]
    preis: Optional[float]
    nadel_str: Optional[str]
    zusammenstellung: Optional[str]
