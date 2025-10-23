from typing import List, Optional
from app.domain.entities.transaction import Transaction
from app.domain.enums.category_type import CategoryType
from app.domain.enums.transaction_type import TransactionType
from app.domain.repositories.transaction_repository import TransactionRepository

class TransactionUseCases:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    async def create_transaction(self, transaction: Transaction) -> Transaction:
        if transaction.amount <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        if transaction.type == TransactionType.EXPENSE and transaction.amount > 0:
            transaction.amount = -transaction.amount
        return await self.repository.create(transaction)

    async def get_transaction(self, transaction_id: str) -> Optional[Transaction]:
        transaction = await self.repository.get_by_id(transaction_id)
        if not transaction:
            raise ValueError("Transacción no encontrada.")
        return transaction

    async def list_transactions(
        self,
        user_id: str,
        transaction_type: Optional[TransactionType] = None,
        category: Optional["CategoryType"] = None
    ) -> List["Transaction"]:
        transactions = await self.repository.list_all(user_id)
        
        if transaction_type:
            transactions = [t for t in transactions if t.type == transaction_type]
        if category:
            transactions = [t for t in transactions if t.category == category]
        
        return transactions


    async def update_transaction(self, transaction_id: str, transaction: Transaction) -> Optional[Transaction]:
        updated = await self.repository.update(transaction_id, transaction)
        if not updated:
            raise ValueError("No se pudo actualizar la transacción.")
        return updated

    async def delete_transaction(self, transaction_id: str) -> bool:
        deleted = await self.repository.delete(transaction_id)
        if not deleted:
            raise ValueError("No se pudo eliminar la transacción.")
        return deleted
