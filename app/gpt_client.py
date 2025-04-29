# app/gpt_client.py

import openai
from app import config


def load_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_tweets(prompt_text, number_of_tweets=15):
    """
    Genera una lista de tweets usando OpenAI a partir de un texto de entrada.
    """

    try:
        system_prompt = load_prompt("input/prompt_instructions.txt")
        user_prompt = load_prompt("input/prompt_style.txt")

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": (
                        f"{user_prompt}\n\n"
                        "Basado en el siguiente texto, genera un máximo de 15 ideas estructuradas "
                        "(cada una de máximo 250 caracteres) que cumplan con el análisis descrito anteriormente "
                        "sobre el tema:\n\n"
                        "\"cómo se desarrolló el proyecto, tecnologías usadas, cómo se hizo el MVP, qué se hizo para lanzar el MVP\"\n\n"
                        f"{prompt_text}"
                    )
                }
            ],
            temperature=0.75,
            max_tokens=1500
        )

        tweets_text = response.choices[0].message.content.strip()
        tweets_list = tweets_text.split("\n")
        tweets = [tweet.strip("- ").strip() for tweet in tweets_list if tweet.strip()]

        return tweets[:number_of_tweets]

    except Exception as e:
        print(f"Error al generar tweets: {e}")
        return []
