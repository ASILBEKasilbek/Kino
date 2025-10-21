from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN =os.getenv("BOT_TOKEN")  # Telegram bot tokeni
ADMIN_IDS = [5306481482,6802314624]
DB_PATH = "database/bot.db" 
REFERRAL_BONUS = 5 