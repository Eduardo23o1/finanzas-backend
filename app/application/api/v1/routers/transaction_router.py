from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from typing import List, Optional
from app.domain.entities.transaction import Transaction, TransactionUpdate
from app.domain.enums.category_type import CategoryType
from app.domain.enums.transaction_type import TransactionType
from app.domain.use_cases.transaction_use_cases import TransactionUseCases
from app.infrastructure.repositories.transaction_repository_impl import TransactionRepositoryImpl
from app.core.auth_dependency import get_current_user, FirebaseUser  # autenticación Firebase

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# Dependencia que crea el caso de uso con el repositorio concreto
def get_transaction_use_cases() -> TransactionUseCases:
    repository = TransactionRepositoryImpl()
    return TransactionUseCases(repository)

@router.post("/", response_model=Transaction)
async def create_transaction(
    transaction: Transaction = Body(...),
    current_user: FirebaseUser = Depends(get_current_user),
    use_cases: TransactionUseCases = Depends(get_transaction_use_cases)
):
    try:
        transaction.user_id = current_user.uid
        created = await use_cases.create_transaction(transaction)
        return created
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[Transaction])
async def list_transactions(
    current_user: FirebaseUser = Depends(get_current_user),
    use_cases: TransactionUseCases = Depends(get_transaction_use_cases),
    type: Optional[TransactionType] = Query(None, description="Filtrar por tipo: income o expense"),
    category: Optional[CategoryType] = Query(None, description="Filtrar por categoría")
):
    return await use_cases.list_transactions(current_user.uid, type, category)


@router.get("/{transaction_id}", response_model=Transaction)
async def get_transaction(
    transaction_id: str,
    use_cases: TransactionUseCases = Depends(get_transaction_use_cases)
):
    try:
        return await use_cases.get_transaction(transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.put("/{transaction_id}", response_model=Transaction)
async def update_transaction(
    transaction_id: str,
    transaction: TransactionUpdate,
    use_cases: TransactionUseCases = Depends(get_transaction_use_cases)
):
    try:
        updated = await use_cases.update_transaction(transaction_id, transaction)
        return updated
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(
    transaction_id: str,
    use_cases: TransactionUseCases = Depends(get_transaction_use_cases)
):
    try:
        await use_cases.delete_transaction(transaction_id)
        return {"message": "Eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
