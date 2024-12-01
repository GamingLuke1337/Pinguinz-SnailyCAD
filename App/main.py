from fastapi import FastAPI
from app.routers import users
from app.database import engine, Base
from app.config import SERVER_CONFIG

# Datenbanktabellen erstellen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registriere Router
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "SnailyCAD API in Python läuft!"}

# Starte den Server basierend auf der Konfiguration
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=SERVER_CONFIG["host"],
        port=SERVER_CONFIG["port"],
        reload=SERVER_CONFIG["reload"],
    )
