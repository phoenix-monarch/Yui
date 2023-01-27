# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("23890262"))
    API_HASH = os.environ.get("da7e86cf57b0e6220b8a9e0aed228a68

API")
    BOT_TOKEN = os.environ.get("5841568185:AAFODqetoPeeBhBsXDyRVT7KIniZDnpWOY8")
    OWNER_ID = int(os.environ.get("1488316798"))
    # Chat bot's name
    CHAT_BOT_NAME = os.environ.get("CHAT_BOT_NAME", "Yui")
    # Your OpenAI API key
    OPENAI_KEY = os.environ.get("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")
    # Your ARQ API Key
    ARQ_API_URL = "http://arq.hamker.dev"
    ARQ_KEY = os.environ.get("NHVTTY-XEDFPD-XXCGHQ-UMQWZU-ARQ")
    # Default Chatbot engine you want to use after OpenAI
    DEFAULT_CHATBOT = os.environ.get("DEFAULT_CHATBOT", "affiliateplus")
    # Set ON_HEROKU to False if you aren't on heroku
    ON_HEROKU = bool(os.environ.get("ON_HEROKU", False))
    HEROKU_API = os.environ.get("HEROKU_API")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
