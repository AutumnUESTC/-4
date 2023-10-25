import os
import re

def set_env_variable(key, value):
    """
    模仿'export'命令来设置环境变量
    """
    os.environ[key] = value

def get_env_variable(key):
    """
    解析环境变量,相当于在shell中使用'$'
    """
    return os.environ.get(key)

def parse_shell_exports(file_path):
    """
    从shell配置文件中解析'export'命令
    """
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return {}

    with open(file_path, 'r') as file:
        shell_content = file.read()

    exports = {}
    #正则表达式来找出所有'export KEY=VALUE'行
    for match in re.finditer(r'\bexport\s+([A-Za-z_][A-Za-z0-9_]*)=(\S+)', shell_content):
        key, value = match.groups()
        #解析可能使用的环境变量引用
        value = re.sub(r'\$([A-Za-z_][A-Za-z0-9_]*)', lambda m: os.getenv(m.group(1), ''), value)
        exports[key] = value

    return exports

def main():
    #设置环境变量
    set_env_variable('MY_VAR', 'value')

    #获取环境变量
    print("MY_VAR:", get_env_variable('MY_VAR'))

    #解析shell配置文件的exports
    config_path = os.path.expanduser('~/.bashrc') 
    exports = parse_shell_exports(config_path)
    
    for key, value in exports.items():
        print(f"从 {config_path} 解析 {key}={value}")

if __name__ == "__main__":
    main()
    main()
