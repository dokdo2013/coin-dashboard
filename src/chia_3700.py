import psutil
import requests
import os
import time

while True:
    try:
        obj_Disk = psutil.disk_usage('E:/')
        disk_use = obj_Disk.used / (1024.0 ** 3)

        plot_count = 0
        for root, dirs, files in os.walk("E:/"):
            for filename in files:
                tmp = filename.split('.')
                extension = tmp[1]
                if extension == 'plot':
                    plot_count += 1

        link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=3700-10T&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
        requests.get(link)
        print(link)
    except:
        time.sleep(120)
    else:
        time.sleep(120)
