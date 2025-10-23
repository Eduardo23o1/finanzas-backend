from typing import List, Optional
from bson import ObjectId
from app.infrastructure.db.mongo_client import get_database
from app.domain.entities.transaction import Transaction
from app.domain.repositories.transaction_repository import TransactionRepository

class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self):
        self.db = get_database()
        self.collection = self.db["transactions"]

    async def create(self, transaction: Transaction) -> Transaction:
        transaction_dict = transaction.model_dump()
        result = await self.collection.insert_one(transaction_dict)
        transaction.id = str(result.inserted_id)
        return transaction

    async def get_by_id(self, transaction_id: str) -> Optional[Transaction]:
        doc = await self.collection.find_one({"_id": ObjectId(transaction_id)})
        if not doc:
            return None
        
        doc["_id"] = str(doc["_id"])
        
        return Transaction(**doc)

    async def list_all(
        self,
        user_id: str,
        transaction_type: Optional[str] = None,
        category: Optional[str] = None
    ) -> List[Transaction]:
        query = {"user_id": user_id}
        
        if transaction_type:
            query["type"] = transaction_type
        
        if category:  # 👈 se agrega el filtro opcional por categoría
            query["category"] = category
            
        cursor = self.collection.find(query)
        docs = await cursor.to_list(length=None)
        
        transactions = []
        for doc in docs:
            doc["id"] = str(doc["_id"])
            doc.pop("_id", None)
            transactions.append(Transaction(**doc))
        
        return transactions



    async def update(self, transaction_id: str, transaction: Transaction) -> Optional[Transaction]:
        transaction_dict = transaction.model_dump(exclude_unset=True)
        result = await self.collection.update_one(
            {"_id": ObjectId(transaction_id)}, {"$set": transaction_dict}
        )
        if result.modified_count == 0:
            return None
        updated_doc = await self.collection.find_one({"_id": ObjectId(transaction_id)})
        if updated_doc:
            updated_doc["_id"] = str(updated_doc["_id"])  # 🔄 Convierte ObjectId a str
            return Transaction(**updated_doc)
        return None


    async def delete(self, transaction_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(transaction_id)})
        return result.deleted_count > 0
