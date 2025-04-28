# app/tweet_generator.py

import os
from app import config
from app.gpt_client import generate_tweets

INPUT_FILE_PATH = "input/tweets_source.txt"

def read_input_file(file_path=INPUT_FILE_PATH):
    """
    Lee el contenido de un archivo de texto.

    Args:
        file_path (str): Ruta del archivo a leer.

    Returns:
        str: Contenido del archivo.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return content

def create_tweets_from_input():
    """
    Lee el archivo de entrada, genera los tweets y los devuelve.

    Returns:
        list: Lista de tweets generados.
    """
    prompt_text = read_input_file()
    tweets = generate_tweets(prompt_text, number_of_tweets=config.NUMBER_OF_TWEETS)
    return tweets
