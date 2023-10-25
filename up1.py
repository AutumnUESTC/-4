import signal
import os
import sys
import time
import subprocess

def signal_handler(sig, frame):
    print("\n程序已安全终止")
    sys.exit(0)

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
        print(f"进程 {pid} 已被终止")
    except ProcessLookupError:
        print(f"没有找到进程 {pid}")

def pkill_process(process_name):
    try:
        subprocess.run(["pkill", process_name])
        print(f"进程 '{process_name}' 已被终止")
    except subprocess.CalledProcessError:
        print(f"没有找到进程 '{process_name}'")

def run_in_background(command):
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        command = input("请输入命令: ")

        if command.startswith("kill "):
            try:
                pid = int(command.split(" ")[1])
                kill_process(pid)
            except ValueError:
                print("请输入有效的PID")
        elif command.startswith("pkill "):
            process_name = command.split(" ")[1]
            pkill_process(process_name)
        elif command.endswith("&"):
            run_command = command[:-1].strip()
            run_in_background(run_command)
            print(f"命令 '{run_command}' 正在后台运行...")
        else:
            os.system(command)
