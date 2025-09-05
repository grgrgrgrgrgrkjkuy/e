from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
queue = []

class ToRoblox(BaseModel):
    action: str
    payload: dict | None = None

@app.post("/to-roblox")
def to_roblox(body: ToRoblox):
    queue.append(body.dict())
    return {"queued": len(queue)}

@app.get("/poll")
def poll():
    global queue
    if not queue:
        return []
    out, queue = queue.copy(), []
    return JSONResponse(out)
