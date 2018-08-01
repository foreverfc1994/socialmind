import logging

class Logger():
    def __init__(self,userid):
        self.logger = logging.getLogger(userid)
        self.logger.setLevel(logging.DEBUG)
        sh = logging.StreamHandler(stream=None)
        sh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s-%(filename)s-%(funcName)s-%(module)s-%(message)s-%(name)s-%(pathname)s')
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)
        pass

    def getlogger(self):
        return self.logger