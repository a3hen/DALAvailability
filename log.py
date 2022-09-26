import logging
import logging.handlers
import datetime
import sys
import socket




class Log(object):
    def __init__(self):
        now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.log_path = sys.path[0]
        self.file_name = self.log_path + str(now_time) + '.log'

    def get_host_ip(self):
        "查询本机ip地址"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            self.ip = s.getsockname()[0]
        finally:
            s.close()
        return self.ip



    def write_to_log(self,data1,data2,level=10):
        logger = logging.getLogger()
        if level == 10:
            level = logging.debug
        elif level ==20:
            level = logging.INFO
        elif level == 30:
            level = logging.WARNING
        elif level == 40:
            level = logging.ERROR
        elif level == 50:
            level = logging.CRITICAL
        else:
            print('The level must be 10,20,30,40,50')

        logger.setLevel(level)
        fh = logging.FileHandler(filename=self.file_name,mode='a',encoding="UTF-8")
        formatter = logging.Formatter(f"%(asctime)s - %(levelname)s -{self.ip}-{data1}-{data2}")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger