from modules.bot import run_bot
import logging

logging.basicConfig(filename="loggings/bot.log", level=logging.DEBUG)
logger = logging.getLogger("bot")

class OpenAiBot():

    def __init__(self):
        try:
            logger.info("Bot rodando...")
            run_bot()
        except Exception as e:
            logger.warning("Ocorreu um erro: " + str(e))


OpenAiBot()