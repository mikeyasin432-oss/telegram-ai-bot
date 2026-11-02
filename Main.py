
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from google import genai

# Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = """
You are an intelligent AI assistant and Medical Laboratory Science tutor.

Your responsibilities:
1. Explain Medical Laboratory Science topics accurately.
2. Help with hematology, bacteriology, parasitology,
   clinical chemistry, immunology, and laboratory techniques.
3. Explain laboratory procedures step by step.
4. Answer general knowledge and everyday questions.
5. Help students prepare for examinations using MCQs.
6. Explain difficult concepts using simple English.

Be accurate, clear, educational, and honest.
Never invent laboratory results, references, or medical facts.
If uncertain, say so.
Distinguish educational information from medical diagnosis.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! 👋\n\n"
        "I'm your AI Laboratory Assistant.\n"
        "I can help with Medical Laboratory Science, "
        "exam preparation, and general questions.\n\n"
        "Send me any question to get started!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "How can I help?\n\n"
        "• Ask laboratory science questions.\n"
        "• Request explanations.\n"
        "• Practice MCQs.\n"
        "• Ask general questions.\n\n"
        "Just type your question!"
    )

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    question = update.message.text

    if not question:
        return

    await update.message.chat.send_action("typing")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question,
            config={
                "system_instruction": SYSTEM_INSTRUCTION,
                "temperature": 0.4,
            },
        )

        answer = response.text or "I couldn't generate an answer. Please try again."

        # Telegram message limit is 4096 characters
        for i in range(0, len(answer), 4000):
            await update.message.reply_text(answer[i:i + 4000])

    except Exception:
        logger.exception("AI response failed")
        await update.message.reply_text(
            "Sorry, I encountered a problem generating your answer. "
            "Please try again."
        )

def main():
    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        raise RuntimeError(
            global client
client = genai.Client(api_key=GEMINI_API_KEY).
        )

    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    logger.info("Telegram AI Laboratory Assistant is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
