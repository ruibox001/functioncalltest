# 步骤5:运行工具函数
# 请将以下代码粘贴到步骤4 代码后
import importlib
import json
from datetime import datetime
from typing import Any

module_name = __name__

def get_current_weather(args: dict):
    location = args.get("location")
    return f"{location}的天气晴朗，温度为25度。"

def get_current_time():
    # 获取当前日期和时间
    current_datetime = datetime.now()
    # 格式化当前日期和时间
    formatted_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    # 返回格式化后的当前时间
    return f"当前时间：{formatted_time}。星期{current_datetime.weekday()+1}"

def speaker_control(args: dict):
    voice = args.get("volume")
    return f"成功设置音量到{voice}"

def run_functions(tool_call: dict) -> dict[str, str | Any] | None:
    # 从返回的结果中获取函数名称和入参
    function_name = tool_call["function"]["name"]
    arguments_string = tool_call["function"]["arguments"]
    print(function_name, arguments_string)

    module = importlib.import_module(module_name)
    function = None
    if hasattr(module, function_name):
        function = getattr(module, function_name)

    if function is None:
        print("未找到该函数")
        return None

    # 使用json模块解析参数字符串
    arguments = json.loads(arguments_string)
    # 创建一个函数映射表
    # function_mapper = {
    #     "get_current_weather": get_current_weather,
    #     "get_current_time": get_current_time,
    #     "speaker_control": speaker_control
    # }
    # 获取函数实体
    # function = function_mapper[function_name]
    # 如果入参为空，则直接调用函数
    if arguments == {}:
        function_output = function()
    # 否则，传入参数后调用函数
    else:
        function_output = function(arguments)
    # 打印工具的输出

    print(f"执行函数={function_name} 参数={arguments_string} 结果输出={function_output}\n")
    return {
        "role": "tool",
        "name": function_name,
        "content": function_output
    }


def run_function(tool_calls: list[dict]):
    if not tool_calls or len(tool_calls) == 0:
        print("没有工具函数需要执行")
        return
    result = []
    for tool_call in tool_calls:
        result.append(run_functions(tool_call))
    return result