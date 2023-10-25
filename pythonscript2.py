import os
import shlex
import subprocess

# 获取用户主目录
home_directory = os.path.expanduser("~")
history_file = os.path.join(home_directory, "yourshellname_history")

# 加载历史命令
history = []
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        history = file.read().splitlines()

# 当前工作目录
current_directory = os.getcwd()

while True:
    command = input("输入：")

    args = shlex.split(command)

    # 如果输入为空，则继续循环，这个是新增加的优化内容！
    if not args:
        continue

    # 将命令添加到历史记录
    history.append(command)

    # 调用其他程序
    try:
        subprocess.run(args)
    except FileNotFoundError:
        print(f"命令 '{args[0]}' 没找到捏")
    except Exception as e:
        print(f"An error occurred: {e}")

    # 保存历史命令到文件
    with open(history_file, "w") as file:
        file.write("\n".join(history))
