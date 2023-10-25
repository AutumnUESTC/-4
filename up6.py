import re
import sys

class SimpleShellParser:
    def __init__(self):
        self.variables = {}

    def parse_line(self, line):
        #去除空白符
        line = line.strip()

        #解析变量赋值
        assignment_match = re.match(r'^([a-zA-Z_]\w*)=(.*)$', line)
        if assignment_match:
            var_name, var_value = assignment_match.groups()
            #移除任何引号
            var_value = var_value.strip('"\'')
            self.variables[var_name] = var_value
            return f"{var_name} set to {var_value}"

        #解析echo语句
        echo_match = re.match(r'^echo\s+(.*)$', line)
        if echo_match:
            to_echo = echo_match.group(1).strip()
            if to_echo.startswith('$'):
                var_name = to_echo[1:]
                return self.variables.get(var_name, f"{var_name} is not set")
            else:
                return to_echo

        return "no dollar." #检查命令是否以"$"开头是为了判断是否是一个环境变量的引用

    def parse_script(self, script_lines):
        for line in script_lines:
            print(self.parse_line(line))

def main():
    #检查命令行参数
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [path to shell script]")
        sys.exit(1)

    script_path = sys.argv[1]

    try:
        with open(script_path, 'r') as file:
            script_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {script_path}")
        sys.exit(1)

    parser = SimpleShellParser()
    parser.parse_script(script_lines)

if __name__ == "__main__":
    main()
