from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

from app.domain.enums.category_type import CategoryType
from app.domain.enums.transaction_type import TransactionType

class Transaction(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: Optional[str] = None
    amount: float
    type: TransactionType
    category: CategoryType
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
        validate_by_name = True

class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[TransactionType] = None
    category: Optional[CategoryType] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        from_attributes = True
        validate_by_name = True