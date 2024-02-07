from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from src.database import Base


phone_memory = Table(
    "phone_memory",
    Base.metadata,
    Column("phone_id", Integer, ForeignKey("phone.id")),
    Column("memory_id", Integer, ForeignKey("memory.id"))
)

phone_color = Table(
    "phone_color",
    Base.metadata,
    Column("phone_id", Integer, ForeignKey("phone.id")),
    Column("color_id", Integer, ForeignKey("color.id"))
)


class MemoryDB(Base):
    __tablename__ = "memory"

    id = Column(Integer, index=True, primary_key=True)
    ram = Column(String(5), nullable=False)
    built_in = Column(String(5), nullable=False)
    price = Column(Float, nullable=False)


class ColorDB(Base):
    __tablename__ = "color"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(63), nullable=False)


class ImageDB(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)


class PhoneDB(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    memories = relationship(MemoryDB, secondary=phone_memory, back_populates="phones")
    colors = relationship(ColorDB, secondary=phone_color, back_populates="phones")
    screen = Column(String(10), nullable=False)
    resolution = Column(String(20), nullable=False)
    processor = Column(String(63), nullable=False)
    camera = Column(String(255), nullable=False)
    zoom = Column(String(255), nullable=False)
    cell = Column(String(255), nullable=False)
    images = relationship(ImageDB)
    about = Column(String, nullable=False)
    is_favourite = Column(Boolean, default=False)
    in_cart = Column(Boolean, default=False)
