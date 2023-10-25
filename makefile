# 目标名称
hey: what

# 规则：构建目标
what: nonexist.c
    gcc -o what nonexist.c

# 清理规则：用于删除生成的文件
clean:
    rm -f what
