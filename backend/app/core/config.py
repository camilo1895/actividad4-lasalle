from dotenv import load_dotenv
import os

ENV = os.getenv("ENVIRONMENT", "DEV").lower()

if ENV == "test":
    load_dotenv(".env.test")
elif ENV == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.dev")

DATABASE_URL = os.getenv("DATABASE_URL")
ENVIRONMENT = os.getenv("ENVIRONMENT")