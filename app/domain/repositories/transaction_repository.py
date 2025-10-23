from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.transaction import Transaction
from app.domain.enums.category_type import CategoryType

class TransactionRepository(ABC):

    @abstractmethod
    async def create(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    async def get_by_id(self, transaction_id: str) -> Optional[Transaction]:
        pass

    @abstractmethod
    async def list_all(self, user_id: str, transaction_type: Optional[str] = None, category: Optional["CategoryType"] = None) -> List[Transaction]:
        pass

    @abstractmethod
    async def update(self, transaction_id: str, transaction: Transaction) -> Optional[Transaction]:
        pass

    @abstractmethod
    async def delete(self, transaction_id: str) -> bool:
        pass
