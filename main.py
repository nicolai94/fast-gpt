from fastapi import FastAPI
from pydantic import BaseModel

from gpt import ask_gpt

app = FastAPI()


class RequestText(BaseModel):
    text: str


class GPTResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=GPTResponse, summary="Задать вопрос")
def ask(data: RequestText) -> GPTResponse:
    result = ask_gpt(data.text)
    return GPTResponse(answer=result)
