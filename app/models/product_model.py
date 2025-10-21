from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from app.config.database import Base
from sqlalchemy.sql import func

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)  # Removed comma
    title = Column(String(200), nullable=False, index=True)  # Added length, removed comma
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    category = Column(String(100), nullable=True)  # Added length
    image_url = Column(String(500), nullable=True)  # Added length
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Product(id={self.id}, title='{self.title}', price={self.price})>"