from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # TODO: 추후 자동업데이트 필요
BLOG_NAME = os.getenv("BLOG_NAME")
API_URL = os.getenv("API_URL")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
