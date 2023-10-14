from fastapi import FastAPI
from pydantic import BaseModel

from gpt import ask_gpt

app = FastAPI()


class GPTResponse(BaseModel):
    answer: str


@app.get("/ask")
def ask(text: str) -> GPTResponse:
    result = ask_gpt(text)
    print(f'{result=}')
    return GPTResponse(answer=result)
