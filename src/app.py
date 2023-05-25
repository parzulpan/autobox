# -*- coding: utf-8 -*-
"""


@author: panpan
@since: 2023/5/25
"""

import os
import ssl

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.memory import ChatMessageHistory

from utils import config_parser

os.environ['OPENAI_API_KEY'] = config_parser.get('ApiKey', 'openai')

ssl._create_default_https_context = ssl._create_unverified_context

# llm = OpenAI(model_name="text-davinci-003", max_tokens=1024)
# print(llm("使用 python 读取配置文件"))

chat = ChatOpenAI(temperature=0)

# 初始化 MessageHistory 对象
history = ChatMessageHistory()

# 给 MessageHistory 对象添加对话内容
history.add_ai_message("你好！")
history.add_user_message("中国的首都是哪里？")

# 执行对话
ai_response = chat(history.messages)
print(ai_response)
