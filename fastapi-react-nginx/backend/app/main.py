from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/length/")
def get_text_length(data: TextInput):
    return {"length": len(data.text)}
