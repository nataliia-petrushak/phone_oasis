from pydantic import BaseModel

from .models import PhoneDB, ColorDB, ImageDB, MemoryDB


class PhoneBase(BaseModel):
    name: str
    memories: MemoryDB
    colors: ColorDB
    screen: str
    resolution: str
    processor: str
    camera: str
    zoom: str
    cell: str
