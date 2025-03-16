from openai import OpenAI
from function_info import tools
from function_run import run_function

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-d0b31c0192e14edda1f42397008ea18a",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def llm_calling(messages, tools) -> dict:
    """
    为了提升用户体验和减少等待时间，您可以使用流式输出快速获取所需调用的工具函数名称。其中：
    工具函数名称：仅在第一个流式返回的对象中出现。
    入参信息：以持续的流式方式输出。
    """
    print(f"大模型请求：{messages}")
    completion = client.chat.completions.create(
        model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=messages,
        tools=tools,
        # stream=True,
        #上文中的问题“上海天气”只需经过一次工具调用即可得到准确回复，如果输入问题需要调用多次工具，如“四个直辖市的天气如何”或“杭州天气，以及现在几点了”
        parallel_tool_calls=True,

        # 默认值auto，默认情况下，如果模型认为工具函数的调用是有必要的，则调用工具函数。
        tool_choice = "auto",

        # 强制调用工具函数get_current_weather
        # tool_choice={"type": "function", "function": {"name": "get_current_weather"}},

        # 强制调用工具函数
        # tool_choice = "required"

        # 不调用工具函数
        # tool_choice = "none"
    )

    # content = completion.choices[0].message
    # print("返回对象：", content)
    return completion.model_dump()


def run_main(msg) -> str:
    chat_messages = [{
        "role": "user",
        "content": msg
        # "content": "你是谁？"
    }]
    assistant_output: dict = llm_calling(messages=chat_messages, tools=tools)
    message = assistant_output["choices"][0]['message']
    chat_messages.append(message)
    # print("第一轮返回：", message)
    if message['tool_calls'] is None:
        print("不需要调用工具回答：", message["content"])
        return message["content"]
    print("需要调用工具回答: ", type(message['tool_calls']), message['tool_calls'])
    result = run_function(message['tool_calls'])
    if result is None:
        return ""
    chat_messages.extend(result)
    print("最后记录: ", len(chat_messages), chat_messages)
    assistant_output: dict = llm_calling(messages=chat_messages, tools=tools)
    message = assistant_output["choices"][0]['message']
    return message["content"]

if __name__ == '__main__':
    print("正在发起function calling...")
    c = run_main("今天是星期几？深圳的天气怎么样？")
    # c = run_main("你是谁？")
    print(c)


