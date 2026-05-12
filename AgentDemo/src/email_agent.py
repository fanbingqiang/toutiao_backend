"""
邮件 Agent：使用 LLM 生成邮件内容，当前输出到控制台（可扩展为真实发送）
"""
import sys
from typing import Optional

from langchain_core.messages import HumanMessage, SystemMessage

from src.my_llm import llm

# Windows 终端 UTF-8 支持
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


SYSTEM_PROMPT = """你是一个专业的邮件助手。根据用户的需求，生成一封格式规范的邮件。

请按以下格式输出：
【收件人】<收件人描述>
【主题】<邮件主题>
【正文】
<邮件正文内容>

正文要求：语气专业得体，条理清晰。"""


class EmailAgent:
    """邮件 Agent，负责生成并发送邮件（当前为控制台输出）"""

    def __init__(self):
        self.llm = llm

    def compose(self, instruction: str) -> str:
        """
        根据指令生成邮件内容
        :param instruction: 用户提供的邮件需求描述
        :return: 生成的邮件文本
        """
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=instruction),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def send(self, email_content: str, recipient: Optional[str] = None) -> None:
        """
        发送邮件（当前版本输出到控制台）
        :param email_content: 邮件内容
        :param recipient: 收件人（预留参数，后续可扩展）
        """
        print("=" * 60)
        print("[邮件内容已生成 - 控制台模式]")
        print("=" * 60)
        if recipient:
            print(f"收件人: {recipient}")
        print()
        print(email_content)
        print("=" * 60)

    def run(self, instruction: str, recipient: Optional[str] = None) -> str:
        """
        一键执行：生成邮件并输出
        :param instruction: 邮件需求描述
        :param recipient: 收件人（可选）
        :return: 生成的邮件内容
        """
        content = self.compose(instruction)
        self.send(content, recipient)
        return content


def main():
    """命令行入口：交互式生成邮件"""
    agent = EmailAgent()
    print("[邮件 Agent - 控制台模式]")
    print("输入你的需求，例如：通知学生明天课程暂停")
    print("输入 exit 退出\n")

    while True:
        instruction = input("\n请输入邮件需求 > ").strip()
        if instruction.lower() in ("exit", "quit", "q"):
            print("再见！")
            break
        if not instruction:
            continue
        print("\n正在生成邮件...\n")
        agent.run(instruction)


if __name__ == "__main__":
    main()
