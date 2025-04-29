# scripts/test_config.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import config
import openai
import tweepy

def test_openai():
    print("🧪 Testeando OPENAI_API_KEY...")
    try:
        openai.api_key = config.OPENAI_API_KEY
        response = openai.models.list()
        print("✅ OpenAI: conexión exitosa.")
    except Exception as e:
        print(f"❌ Error en OpenAI: {e}")

def test_twitter():
    print("🧪 Testeando credenciales de Twitter...")
    try:
        client = tweepy.Client(
            consumer_key=config.TWITTER_API_KEY,
            consumer_secret=config.TWITTER_API_SECRET_KEY,
            access_token=config.TWITTER_ACCESS_TOKEN,
            access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET
        )
        user = client.get_me()
        print(f"✅ Twitter: conectado como @{user.data.username}")
    except Exception as e:
        print(f"❌ Error en Twitter: {e}")

if __name__ == "__main__":
    test_openai()
    print()
    test_twitter()
