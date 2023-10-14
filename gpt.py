import g4f


def ask_gpt(text: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    result_text = ''
    for message in response:
        result_text += message

    return result_text
