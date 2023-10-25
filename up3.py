import readline
import rlcompleter
import os

histfile = os.path.join(os.path.expanduser("~"), ".tab_history")

try:
    readline.read_history_file(histfile)
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

#Tab补全配置
readline.parse_and_bind("tab: complete")

def my_input(prompt=">>> "):
    try:
        #读取输入，这里可以使用tab补全&查看历史命令
        return input(prompt)
    except KeyboardInterrupt:
        #如果使用Ctrl+C，会抛出KeyboardInterrupt，我们捕获这个异常并退出
        print("\nKeyboardInterrupt")
        return None

while True:
    #获取输入
    command = my_input()
    if command in [None, "exit", "quit"]:
        break
    if command.strip() == "":
        continue  #也考虑一下未输入的情况
    try:
        exec(command)
    except Exception as e:
        #如果执行时出现异常，就输出异常信息
        print("Error:", e)

readline.write_history_file(histfile)
