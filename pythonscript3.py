import os
import shlex
import subprocess

home_directory = os.path.expanduser("~")
history_file = os.path.join(home_directory, "yourshellname_history")

history = []
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        history = file.read().splitlines()

# 别名字典
aliases = {}

current_directory = os.getcwd()

while True:
    command = input("$ ")

    args = shlex.split(command)

    if not args:
        continue

    # 处理内建命令
    if args[0] == "exit":
        # 保存历史命令到文件
        with open(history_file, "w") as file:
            file.write("\n".join(history))
        break
    elif args[0] == "which":
        if len(args) > 1:
            # 查找别名
            alias_cmd = aliases.get(args[1])
            if alias_cmd:
                print(f"{args[1]} 是别名，对应的命令是 '{alias_cmd}'")
            else:
                try:
                    # 查找系统命令
                    cmd_path = subprocess.check_output(["which", args[1]], text=True)
                    print(cmd_path, end="")
                except subprocess.CalledProcessError as e:
                    # 如果命令不存在，显示错误信息
                    print(f"系统命令 '{args[1]}' 是不存在的")
                    # 尝试显示类似命令
                    try:
                        similar_cmds = subprocess.check_output(["apropos", args[1]], text=True)
                        print(similar_cmds)
                    except subprocess.CalledProcessError:
                        pass
        else:
            print("Usage: which <command>")
    elif args[0] == "alias":
        if len(args) > 2:
            # 添加别名
            aliases[args[1]] = args[2]
        elif len(args) == 2 and args[1] in aliases:
            # 显示别名
            print(f"{args[1]} 是别名，对应的命令是 '{aliases[args[1]]}'")
        else:
            # 列出所有别名
            for alias, cmd in aliases.items():
                print(f"{alias} 是别名，对应的命令是 '{cmd}'")
    elif args[0] == "unalias":
        if len(args) == 2 and args[1] in aliases:
            # 删除别名
            del aliases[args[1]]
        else:
            print("Usage: unalias <alias>")
    elif args[0] == "history":
        # 显示命令历史记录
        for idx, cmd in enumerate(history, start=1):
            print(f"{idx}: {cmd}")
    else:
        # 将命令添加到历史记录
        history.append(command)

        try:
            subprocess.run(args)
        except FileNotFoundError:
            print(f"命令 '{args[0]}' 没找到捏")
        except Exception as e:
            print(f"发生了这样的错误: {e}")

    with open(history_file, "w") as file:
        file.write("\n".join(history))
