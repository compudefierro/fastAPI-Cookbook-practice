from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def leer_libro():
    return "Hola usuario, no hay libro"


@app.get("/list")
async def lista_cmd(year: str = None):
    if year:
        return f"Ingresaste el comando '{year}'"
    return "Sin comandos"
