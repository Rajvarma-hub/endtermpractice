from fastapi import FastAPI

app=FastAPI(title="Endterm Practical")

@app.get("/")
def get_health():
    return "Server is healthy"