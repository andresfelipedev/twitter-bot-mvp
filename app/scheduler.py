# app/scheduler.py

import schedule
import time
import random
from datetime import datetime, timedelta
from app.twitter_client import create_twitter_client, post_tweet

def schedule_tweets(tweets, tweets_per_day=5):
    """
    Programa la publicación de tweets durante el día en horarios aleatorios.

    Args:
        tweets (list): Lista de tweets a publicar.
        tweets_per_day (int): Número de tweets a publicar por día.
    """

    client = create_twitter_client()
    if client is None:
        print("No se pudo crear el cliente de Twitter. Cancelando programación.")
        return

    # Definir el rango horario permitido (7am a 9pm)
    start_hour = 7
    end_hour = 21

    # Limitar la cantidad de tweets disponibles
    tweets_to_post = tweets[:tweets_per_day]

    # Crear una lista de horarios aleatorios para cada tweet
    scheduled_times = generate_random_times(start_hour, end_hour, tweets_per_day)

    for tweet, post_time in zip(tweets_to_post, scheduled_times):
        schedule.every().day.at(post_time).do(post_tweet, client=client, tweet_text=tweet)
        print(f"Tweet programado a las {post_time}: {tweet[:30]}...")

def generate_random_times(start_hour, end_hour, quantity):
    """
    Genera una lista de horarios aleatorios en formato 'HH:MM'.

    Args:
        start_hour (int): Hora mínima (24h).
        end_hour (int): Hora máxima (24h).
        quantity (int): Número de horarios a generar.

    Returns:
        list: Lista de strings en formato 'HH:MM'.
    """

    times = set()

    while len(times) < quantity:
        hour = random.randint(start_hour, end_hour)
        minute = random.randint(0, 59)
        times.add(f"{hour:02d}:{minute:02d}")

    return sorted(times)

def run_scheduler():
    """
    Mantiene corriendo el programador de tareas.
    """

    print("Programador de tweets iniciado. Esperando eventos...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Verificar cada minuto
