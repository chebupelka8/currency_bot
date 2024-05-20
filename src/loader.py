import dotenv
import os

from typing import Optional


class Loader:

    @staticmethod
    def get_token() -> Optional[str]:
        dotenv.load_dotenv("./data.env")

        return os.getenv("TOKEN")
