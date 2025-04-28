# scripts/test_config.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# scripts/test_gpt_client.py

# scripts/test_tweet_generator.py

# scripts/test_twitter_client.py

from app.twitter_client import create_twitter_client, post_tweet

client = create_twitter_client()

if client:
    texto_de_prueba = "Este es un tweet de prueba generado automáticamente. 🚀"
    post_tweet(client, texto_de_prueba)
