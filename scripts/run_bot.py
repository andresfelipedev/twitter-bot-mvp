# scripts/run_bot.py

from app.tweet_generator import create_tweets_from_input
from app.scheduler import schedule_tweets, run_scheduler

def main():
    """
    Función principal para ejecutar el bot:
    - Lee el archivo de entrada.
    - Genera los tweets.
    - Programa su publicación.
    - Ejecuta el scheduler.
    """

    print("Iniciando generación de tweets... 🚀")
    tweets = create_tweets_from_input()

    if not tweets:
        print("No se generaron tweets. Verifica el archivo de entrada o la conexión con OpenAI.")
        return

    print(f"{len(tweets)} tweets generados exitosamente.")

    print("Programando tweets... 🗓️")
    schedule_tweets(tweets)

    # Ejecutar el programador de tareas (se queda corriendo)
    run_scheduler()

if __name__ == "__main__":
    main()
