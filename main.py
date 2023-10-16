from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from gpt import ask_gpt

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestText(BaseModel):
    text: str


class GPTResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=GPTResponse, summary="Задать вопрос")
def ask(data: RequestText) -> GPTResponse:
    result = ask_gpt(data.text)
    return GPTResponse(answer=result)
