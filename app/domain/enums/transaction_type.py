from enum import Enum

class TransactionType(str, Enum):
    INCOME = "income"   # Ingreso
    EXPENSE = "expense" # Gasto
