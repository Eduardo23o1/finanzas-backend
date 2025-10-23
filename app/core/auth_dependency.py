from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth
from app.core.firebase_utils import initialize_firebase

security = HTTPBearer()
initialize_firebase()

class FirebaseUser:
    def __init__(self, uid: str, email: str | None):
        self.uid = uid
        self.email = email

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> FirebaseUser:
    token = credentials.credentials
    try:

        decoded_token = auth.verify_id_token(token)

        user = FirebaseUser(
            uid=decoded_token.get("uid"),
            email=decoded_token.get("email")
        )
        return user

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error al verificar el token: {str(e)}",
        )

