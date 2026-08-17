import json
from typing import TypedDict

class Movie(TypedDict):
    name: str
    original_name: str
    buget: int
    is_movie: bool
    characters: list[str]
    director: str | None

json_create = """{
    "name":"Circulo de fogo",
    "orinal_name": "Pacific rin",
    "buget": 3000000,
    "characters": ["Beget","Mako"],
    "is_movie":true,
    "director":null
}"""
 
filme:Movie = json.loads(json_create)
print(type(filme))
print(json.dumps(filme, ensure_ascii=False))