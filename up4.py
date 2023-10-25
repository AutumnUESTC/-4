import logging

#配置日志系统,包括名称\级别\格式
logging.basicConfig(filename='不堪往事.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#创建一个日志记录器
logger = logging.getLogger('不堪往事')

#创建处理器并添加到记录器
console_handler = logging.StreamHandler()  #输出到控制台
file_handler = logging.FileHandler('不堪往事.log')  #输出到文件

#创建格式化器并将其附加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

#记录不同级别的日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
