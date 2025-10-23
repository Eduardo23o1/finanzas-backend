from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.application.api.v1.routers.transaction_router import router as transactions_router
from app.application.api.v1.routers.auth_router import router as auth_router

app = FastAPI(title="Finanzas Personales API")

# --- Configuración CORS ---
origins = [
    "http://localhost:5173",  # puerto típico de Flutter Web, ajusta si es distinto
    "http://127.0.0.1:5173",
    "http://localhost:8000",  # opcional
    "*",  # permite cualquier origen, útil solo en desarrollo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # permite POST, GET, OPTIONS, PUT, DELETE...
    allow_headers=["*"],  # permite Authorization, Content-Type, etc.
)

# --- Routers ---
app.include_router(auth_router)
app.include_router(transactions_router)

@app.get("/")
def root():
    return {"message": "API de Finanzas Personales funcionando"}
