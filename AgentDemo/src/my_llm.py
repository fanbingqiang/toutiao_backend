"""
LLM 配置模块，从环境变量读取配置初始化模型
"""
from langchain_deepseek import ChatDeepSeek

from src.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.6,
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)



