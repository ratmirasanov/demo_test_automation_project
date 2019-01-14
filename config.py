"""Module Config with applicable configuration information."""

import os


DOMAIN = os.environ.get("DOMAIN", "https://youtube.com")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DELAY1 = 30
DELAY2 = 5
WIDTH = 1440
HEIGHT = 900
USER1 = {
    "email": "ratmir.asanov.demo@gmail.com",
    "password": "xxn3omk5iar23fdr1yxx",
}
SCROLL_PAUSE_TIME = 2
