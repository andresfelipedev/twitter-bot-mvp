
# 🐍 Twitter Bot MVP con OpenAI + Tweepy + Render

Este proyecto es un **bot automatizado de Twitter** que:
- Lee un archivo `.txt` de entrada
- Usa **OpenAI (GPT-3.5)** para generar 15 tweets breves
- Publica automáticamente 5 tweets diarios en horarios aleatorios de 7:00 AM a 9:00 PM
- Está desplegado en **Render.com** usando **Docker**

---

## 🛠️ Tech Stack

- Python 3.11
- OpenAI API (gpt-3.5-turbo)
- Tweepy (API de Twitter/X)
- Schedule (automatización de tareas)
- Docker (contenedorización)
- Render.com (despliegue en la nube)

---

## 📂 Estructura del Proyecto

```
twitter-bot-mvp/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── gpt_client.py
│   ├── tweet_generator.py
│   ├── twitter_client.py
│   └── scheduler.py
│
├── input/
│   └── tweets_source.txt
│
├── scripts/
│   └── run_bot.py
│
├── tests/          # (Pendiente de implementar unit tests)
├── .env.example    # (Ejemplo de variables de entorno)
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Cómo correr el proyecto localmente

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd twitter-bot-mvp
```

2. Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # en Linux/macOS
venv\Scripts\activate   # en Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura tus variables de entorno creando un archivo `.env`:

```env
OPENAI_API_KEY=tu_clave_openai
TWITTER_API_KEY=tu_api_key
TWITTER_API_SECRET_KEY=tu_api_secret
TWITTER_ACCESS_TOKEN=tu_access_token
TWITTER_ACCESS_TOKEN_SECRET=tu_access_secret
```

5. Ejecuta el bot:

```bash
python scripts/run_bot.py
```

---

## ☁️ Cómo desplegarlo en Render.com

1. Sube el proyecto a GitHub.
2. Crea un **Background Worker** en Render.com.
3. Usa el `Dockerfile` como entorno de ejecución.
4. Agrega las variables de entorno desde tu `.env`.
5. Deploy automático.

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

---

> **Desarrollado como un MVP limpio, escalable y listo para producción.** 🚀
