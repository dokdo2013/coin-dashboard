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

        link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=xeon-320G&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
        requests.get(link)
        print(link)

        obj_Disk = psutil.disk_usage('G:/')
        disk_use = obj_Disk.used / (1024.0 ** 3)

        plot_count = 0
        for root, dirs, files in os.walk("G:/"):
            for filename in files:
                tmp = filename.split('.')
                extension = tmp[1]
                if extension == 'plot':
                    plot_count += 1

        link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=xeon-2T&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
        requests.get(link)
        print(link)

        obj_Disk = psutil.disk_usage('H:/')
        disk_use = obj_Disk.used / (1024.0 ** 3)

        plot_count = 0
        for root, dirs, files in os.walk("H:/"):
            for filename in files:
                tmp = filename.split('.')
                extension = tmp[1]
                if extension == 'plot':
                    plot_count += 1

        link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=xeon-200G&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
        requests.get(link)
        print(link)

        obj_Disk = psutil.disk_usage('I:/')
        disk_use = obj_Disk.used / (1024.0 ** 3)

        plot_count = 0
        for root, dirs, files in os.walk("I:/"):
            for filename in files:
                tmp = filename.split('.')
                extension = tmp[1]
                if extension == 'plot':
                    plot_count += 1

        link = 'https://do.yatchacha.com/index.php/api/chia_data/update?key=xeon-8T&plots=' + str(plot_count) + '&capacity=' + str(format(disk_use, ".2f"))
        requests.get(link)
        print(link)

    except:
        time.sleep(120)
    else:
        time.sleep(120)
