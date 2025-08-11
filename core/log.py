import logging
import logging.config
id_dict = {0:"日志",1:"配置文件读写",2:"配置读写",3:"<UNK>",4:"<UNK>"}
logging.basicConfig(level=logging.DEBUG)
class logManager:
    def __init__(self):
        self.l_logger = logging.getLogger('日志')
        self.l_logger.debug("日志模块实例化完毕")
    @classmethod
    def get_logger(cls,id):
        return logging.getLogger(id_dict[id])