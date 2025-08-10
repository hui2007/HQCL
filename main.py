from lib import *

#configManager.init_config()

#print(configManager.get_config("version"))
#print(configManager.get_config("verson"))
#configManager.new_config("verson","114514")
#print(configManager.get_config("verson"))
#configManager.write_config("verson","1919810")
#print(configManager.get_config("verson"))
configManager.del_config("verson")
print(configManager.get_config("verson"))
