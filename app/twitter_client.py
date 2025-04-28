# app/twitter_client.py

import tweepy
from app import config

def create_twitter_client():
    """
    Crea y autentica un cliente de Twitter usando Tweepy.

    Returns:
        tweepy.Client: Cliente autenticado de Tweepy.
    """
    try:
        client = tweepy.Client(
            consumer_key=config.TWITTER_API_KEY,
            consumer_secret=config.TWITTER_API_SECRET_KEY,
            access_token=config.TWITTER_ACCESS_TOKEN,
            access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET
        )
        return client
    except Exception as e:
        print(f"Error al crear el cliente de Twitter: {e}")
        return None

def post_tweet(client, tweet_text):
    """
    Publica un tweet en Twitter.

    Args:
        client (tweepy.Client): Cliente autenticado.
        tweet_text (str): Texto del tweet.

    Returns:
        dict: Respuesta de la API o error.
    """
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet publicado: {tweet_text[:30]}... ✅")
        return response
    except Exception as e:
        print(f"Error al publicar tweet: {e}")
        return None
