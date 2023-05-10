import os
from dotenv import load_dotenv
from pathlib import Path

# 環境変数のファイルパス取得
credential_file_path: str = f"{Path(__file__).resolve().parent.parent}/.env"

load_dotenv(credential_file_path)
KEY = os.getenv("KEY")
