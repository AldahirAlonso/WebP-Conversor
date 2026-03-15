from fastapi import FastAPI

app = FastAPI(title="Image to WebP converter")

@app.get("/test")
def health_check():
    return {"status": "ok", "message": "Convertidor app funcionando!"}