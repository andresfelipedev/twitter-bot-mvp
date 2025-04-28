# app/gpt_client.py

import openai
from app import config

# Inicializar el cliente de OpenAI
openai.api_key = config.OPENAI_API_KEY

def generate_tweets(prompt_text, number_of_tweets=15):
    """
    Genera una lista de tweets usando OpenAI a partir de un texto de entrada.

    Args:
        prompt_text (str): Texto base para generar los tweets.
        number_of_tweets (int): Número de tweets a generar.

    Returns:
        list: Lista de tweets generados.
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Usamos un modelo rápido y económico para MVP
            messages=[
                {"role": "system", "content": "Eres un experto en marketing que escribe tweets breves y atractivos."},
                {"role": "user", "content": f"Basado en el siguiente texto, genera {number_of_tweets} tweets breves (máximo 280 caracteres cada uno):\n\n{prompt_text}"}
            ],
            temperature=0.7,  # Nivel medio de creatividad
            max_tokens=1000  # Máximo de tokens generados
        )

        tweets_text = response.choices[0].message.content.strip()
        tweets_list = tweets_text.split("\n")  # Asumimos que cada tweet estará en una nueva línea

        # Limpiar lista por si vienen numerados o con espacios extra
        tweets = [tweet.strip("- ").strip() for tweet in tweets_list if tweet.strip()]

        return tweets[:number_of_tweets]  # Solo devolver la cantidad necesaria

    except Exception as e:
        print(f"Error al generar tweets: {e}")
        return []
