import json
__version__ = "0.01"
def init_config():
    """
    初始化配置文件
    :return:
    """
    default_config = {
        "version": __version__,
        "gameDir":".minecraft",
        "verList":[],
        "accountList":[]
    }
    with open("config.json","w+") as config_file:
        json.dump(default_config,config_file)
    return True
def get_config(key):
    """
    获取键值
    :param key:键
    :return:
    """
    with open("config.json","r") as config_file:
        config = json.load(config_file)
    return config.get(key)
def write_config(key,value):
    """
    直接修改键值
    :param key:
    :param value:
    :return:
    """
    with open("config.json","r") as config_file:
        config = json.load(config_file)
    if key not in config:
        return False
    config[key] = value
    with open("config.json","w") as config_file:
        json.dump(config,config_file)
    return True
def new_config(key,value):
    """
    新增键值
    :param key:
    :param value:
    :return:
    """
    with open("config.json","r") as config_file:
        config = json.load(config_file)
    config.setdefault(key,value)
    with open("config.json","w") as config_file:
        json.dump(config,config_file)
    return True
def del_config(key):
    """
    删除键值
    :param key:
    :return:
    """
    with open("config.json","r") as config_file:
        config = json.load(config_file)
    if key not in config:
        return False
    del config[key]
    with open("config.json","w") as config_file:
        json.dump(config,config_file)
    return True