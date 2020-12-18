import vk_api
from datetime import datetime, timedelta
import time
 
vk_session = vk_api.VkApi() # provide your login data here, like "+phoneNumber", "Password"
vk_session.auth()
vk = vk_session.get_api()
 
 
print('robit')
 
while True:
    time.sleep(60)
    user = vk.account.getCounters(filter='friends, messages')
    getMSGtime = user['messages']
    vk.status.set(text='💍Всегда онлайн :).\n📖Непрочитанных сообщений: ' + str(getMSGtime) + '\nВсе будет прочитано')
