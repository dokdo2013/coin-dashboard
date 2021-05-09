import GPUtil
import requests
import time

while True:
    try:
        temp = GPUtil.getGPUs()[0].temperature

        link = 'https://do.yatchacha.com/index.php/api/gpu/update?key=2070s&temperature=' + str(temp)
        requests.get(link)
        print(link)
    except:
        time.sleep(10)
    else:
        time.sleep(10)

