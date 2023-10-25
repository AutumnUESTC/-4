import shlex
import subprocess

while True:
    # 读取输入的命令
    my_input = input("输入命令: ")

    # 解析命令行输入
    args = shlex.split(my_input)

    # 执行命令
    if args:
        try:
            # 使用 subprocess 运行命令
            subprocess.run(args, check=True)
        except FileNotFoundError:
            print(f"Command '{args[0]}' 没找到捏")
        except subprocess.CalledProcessError as e:
            print(f"执行的时候出现了一个错误: {e}")
    else:
        print("请输入命令：")
