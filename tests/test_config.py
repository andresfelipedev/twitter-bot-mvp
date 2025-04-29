# scripts/test_config.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# scripts/test_gpt_client.py

# scripts/test_tweet_generator.py

# scripts/test_twitter_client.py

# scripts/test_full_flow.py

from app.tweet_generator import create_tweets_from_input

def main():
    """
    Ejecuta una prueba completa:
    - Lee el archivo de entrada
    - Genera los tweets
    - Muestra los tweets generados
    """

    print("\n🚀 Iniciando prueba completa del bot...\n")

    try:
        tweets = create_tweets_from_input()

        if not tweets:
            print("⚠️ No se generaron tweets. Verifica tu conexión a OpenAI o el contenido del archivo de entrada.")
            return

        print(f"\n✅ Se generaron {len(tweets)} tweets:\n")
        for idx, tweet in enumerate(tweets, start=1):
            print(f"{idx}. {tweet}\n")

        print("\n🎯 Flujo completo de generación de tweets ejecutado con éxito.\n")

    except Exception as e:
        print(f"❌ Error durante la ejecución de la prueba: {e}")

if __name__ == "__main__":
    main()
