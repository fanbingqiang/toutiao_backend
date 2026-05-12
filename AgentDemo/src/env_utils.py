"""
环境变量工具模块
"""
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")