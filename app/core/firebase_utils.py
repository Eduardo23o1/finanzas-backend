import firebase_admin
from firebase_admin import credentials, auth
from app.core.config import settings

firebase_app = None

def initialize_firebase():
    """Inicializa la app de Firebase si aún no ha sido inicializada."""
    global firebase_app
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_app = firebase_admin.initialize_app(cred)
    else:
        firebase_app = firebase_admin.get_app()
    return firebase_app


def verify_token(id_token: str):
    """
    Verifica el token enviado por el cliente (Firebase Auth)
    y devuelve el UID del usuario si es válido.
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Error al verificar el token: {str(e)}")
        raise Exception(f"Token inválido o expirado: {str(e)}")
