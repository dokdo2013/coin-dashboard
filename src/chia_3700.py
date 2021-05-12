import psutil
import requests
import os
import time
from telegram_bot import tgBot

directory_list = [
    {
        "directory": "E:/",
        "name": "3700-10T"
    }
]

while True:
    try:
        for drc in directory_list:
            before_plot_count = 0
            before_capacity = 0.0

            obj_Disk = psutil.disk_usage(drc['directory'])
            disk_use = obj_Disk.used / (1024.0 ** 3)

            plot_count = 0
            for root, dirs, files in os.walk(drc['directory']):
                for filename in files:
                    tmp = filename.split('.')
                    extension = tmp[1]
                    if extension == 'plot':
                        plot_count += 1

            if before_plot_count != plot_count or str(before_capacity) != str(format(disk_use, ".2f")):
                before_plot_count = plot_count
                before_capacity = format(disk_use, ".2f")

                link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=' + str(
                    drc['name']) + '&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
                requests.get(link)
                txt = "플롯 생성 완료! 장비명 : " + str(drc['name']) + " (총 플롯 수 : " + str(plot_count) + " / 총 용량 : " + str(
                    int(disk_use)) + "GB)"
                tgBot.send(txt)
                print(link)
    except Exception as e:
        print(e)
        time.sleep(120)
    else:
        time.sleep(120)