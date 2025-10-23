from enum import Enum

class CategoryType(str, Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    HEALTH = "health"
    ENTERTAINMENT = "entertainment"
    EDUCATION = "education"
    OTHER = "other"
    SALARY = "salary"
    SHOPPING = "shopping"
