import openai
import os

openai.api_key = os.getenv(key="API_KEY")

# MAX TOKENS
max_tokens = 1024

# Defina o modelo e o prompt
model_engine = "text-davinci-003"

def send_response(prompt):
    try:
        conclusion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens = max_tokens
        )
    except Exception as e:
        print("Erro: " + str(e))

    return conclusion.choices[0].text