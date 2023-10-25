import os
import shlex
import subprocess
import sys

def run_in_background(command):
    command_list = shlex.split(command)

    if "|" in command:
        #获取管道前后的命令
        left_command, right_command = command.split("|", 1)

        #创建管道
        pipe_read, pipe_write = os.pipe()

        #创建子进程来执行左侧的命令，并将输出重定向到管道
        left_pid = os.fork()
        if left_pid == 0:  
            os.close(pipe_read)  #关闭管道的读端
            os.dup2(pipe_write, sys.stdout.fileno())  #将标准输出重定向到管道写端
            os.execvp(left_command.strip(), shlex.split(left_command.strip()))
        else:  
            os.close(pipe_write)  #关闭管道的写端
            os.waitpid(left_pid, 0)  #等待左侧命令的子进程执行完毕

            #创建子进程来执行右侧的命令，并将输入重定向自管道
            right_pid = os.fork()
            if right_pid == 0:  
                os.close(pipe_read)  #关闭管道的读端
                os.dup2(pipe_read, sys.stdin.fileno())  #将标准输入重定向到管道读端
                os.execvp(right_command.strip(), shlex.split(right_command.strip()))
            else:  
                os.close(pipe_read)  #关闭管道的读端
                os.waitpid(right_pid, 0)  #等待右侧命令的子进程执行完毕
    else:
        #没有管道符时，直接运行命令
        subprocess.Popen(command_list, shell=True)
