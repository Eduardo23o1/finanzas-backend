## Configuración del Backend

## Requisitos

* Python 3.13.5
* pip (viene con Python)
* MongoDB corriendo localmente

1. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=finanzas_db
FIREBASE_API_KEY=AIzaSyCHdoiJl-dGIFoGskCxDG2OdRt2pG4tZNE
FIREBASE_CREDENTIALS_PATH=C:/ruta/a/serviceAccountKey.json
```

* Ajusta `FIREBASE_CREDENTIALS_PATH` según la ubicación real del JSON descargado de Firebase.

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar Firebase en backend:

* Crear un proyecto en [Firebase Console](https://console.firebase.google.com/).
* Habilitar **Authentication** con Email/Password.
* Crear una **Service Account** y descargar el JSON (`serviceAccountKey.json`).
* Colocar el JSON en la ruta indicada en la variable de entorno `FIREBASE_CREDENTIALS_PATH`.

---

## Cómo ejecutar

### Backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Esto correrá la API en `http://localhost:8000`.
* El flag `--reload` permite que los cambios en el código se reflejen automáticamente.


## Configuración CORS (Backend)

En `main.py` ya está configurado para permitir peticiones desde:

* `http://localhost:5173` (Flutter Web)
* `http://127.0.0.1:5173`
* `http://localhost:8000`
* `*` (cualquier origen, útil solo en desarrollo)

---

## Notas finales

* Asegúrate de que MongoDB esté corriendo antes de iniciar el backend.
* Las rutas principales son:

  * `/` : Verifica que la API está funcionando
  * `/auth/...` : Endpoints de autenticación
  * `/transactions/...` : Endpoints para transacciones
* Para pruebas de autenticación, se pueden crear usuarios directamente en Firebase Console.
* Este README sirve para ejecutar tanto la app Flutter como el backend local en cualquier máquina.
