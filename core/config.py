import json

from core.log import LogManager


class ConfigIo:
    def __init__(self):
        self.origin_value = None
        self.c_logger = LogManager.get_logger(1)
        self.config_file = open('config.json', 'r+', encoding='utf-8')
        self.config = json.load(self.config_file)
        self.c_logger.debug("配置读写模块实例化完毕")

    def __update_config(self):
        self.config_file.seek(0)
        self.config_file.truncate()
        json.dump(self.config, self.config_file)
        self.c_logger.debug("已更新配置文件")
        return True

    def add_key(self, key, value):
        self.config.setdefault(key, value)
        self.c_logger.debug(f"已添加键值对{{{key}:{value}}}")
        self.__update_config()
        return True

    def del_key(self, key):
        self.config.pop(key)
        self.c_logger.debug(f"已删除键{{{key}}}")
        self.__update_config()
        return True

    def change_key(self, key, value):
        self.origin_value = self.config[key]
        self.config[key] = value
        self.c_logger.debug(f"已修改键值{key}:{self.origin_value}->{key}")
        self.__update_config()
        return True

    def read_key(self, key):
        read_value = self.config[key]
        self.c_logger.debug(f"已读取键值{{{key}:{read_value}}}")
        return read_value

    def __del__(self):
        self.config_file.close()
        self.c_logger.debug("配置读写模块已关闭")
