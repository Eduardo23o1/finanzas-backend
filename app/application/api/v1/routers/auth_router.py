from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login_user(request: LoginRequest):
    """
    Autentica al usuario contra Firebase y devuelve su idToken (JWT).
    """
    firebase_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={settings.FIREBASE_API_KEY}"

    payload = {
        "email": request.email,
        "password": request.password,
        "returnSecureToken": True
    }

    response = requests.post(firebase_url, json=payload)
    data = response.json()

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail=data.get("error", {}).get("message", "Error de autenticación"))

    return {
        "idToken": data["idToken"],
        "refreshToken": data["refreshToken"],
        "expiresIn": data["expiresIn"],
        "email": data["email"]
    }
