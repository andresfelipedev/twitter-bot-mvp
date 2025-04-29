# scripts/run_bot.py

import os
print("🪪 UID:", os.getuid())
print("📁 Working dir:", os.getcwd())

from app.tweet_generator import create_tweets_from_input
from app.scheduler import schedule_tweets, run_scheduler

def main():
    print("🚀 Bot iniciado")  # primer punto visible

    tweets = create_tweets_from_input()
    if not tweets:
        print("⚠️ No se generaron tweets")
        return

    print(f"✅ {len(tweets)} tweets generados")
    schedule_tweets(tweets)
    run_scheduler()

if __name__ == "__main__":
    print("📦 Lanzando main()")
    main()
