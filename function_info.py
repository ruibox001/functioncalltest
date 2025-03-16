
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_time",
      "description": "当你想知道现在的时间时非常有用。"
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "当你想查询指定城市的天气时非常有用。",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "城市或县区，比如北京市、杭州市、余杭区等。"
          }
        },
        "required": [
          "location"
        ]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "speaker_control",
      "description": "机器人的扬声器音量",
      "properties": {
        "volume": {
          "description": "当前音量值",
          "type": "number"
        }
      },
      "methods": {
        "SetVolume": {
          "description": "设置扬声器音量",
          "parameters": {
            "volume": {
              "description": "0到100之间的整数",
              "type": "number"
            }
          }
        }
      }
    }
  }
]
# tool_name = [tool["function"]["name"] for tool in tools]
# print(f"创建了{len(tools)}个工具，为：{tool_name}\n")


# 步骤3:创建messages数组
# 请将以下代码粘贴到步骤2 代码后
# messages = [
#     # {
#     #     "role": "system",
#     #     "content": """你是一个很有帮助的助手。如果用户提问关于天气的问题，请调用 ‘get_current_weather’ 函数;
#     #  如果用户提问关于时间的问题，请调用‘get_current_time’函数。
#     #  请以友好的语气回答问题。""",
#     # },
#     {
#         "role": "user",
#         # "content": "现在几点？"
#         # "content": "上海的天气怎么样？"
#         # "content": "你是哪个大模型？"
#         "content": "上海的天气怎么样？还有现在几点？"
#     }
# ]

