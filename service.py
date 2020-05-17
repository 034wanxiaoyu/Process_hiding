import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect

class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService" #服务名
    _svc_display_name_ = "Python Service Test" #服务在windows系统中显示的名称
    _svc_description_ = "This code is a Python service Test"

    #_init_()函数执行完后，系统服务开始启动，windows系统会自动调用SvcDoRun函数
    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        self.run = True

    def _getLogger(self):
        logger=logging.getLogger('[PythonService]')
        this_file=inspect.getfile(inspect.currentframe())
        dirpath=os.path.abspath(os.path.dirname(this_file))
        handler=logging.FileHandler(os.path.join(dirpath,"service.log"))
        formatter=logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    #SvcDoRun()函数可以写自己要写的代码
    def SvcDoRun(self):
        import time
        self.logger.info("service is run ....")
        while self.run:
            self.logger.info("I am running ....")
            time.sleep(2)
        #win32event.WaitForSingleObject(self.hWaitStop,win32event.INFINITE)

    #当停止服务时，系统会调用SvcStop函数，该函数通过设置标志位等方式让SvcDoRun函数退出，就是正常的停止服务
    def SvcStop(self):
        self.logger.info("service is stop ....")
        #先告诉SCM停止这个过程
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        #设置事件
        win32event.SetEvent(self.hWaitStop)
        self.run = False

if __name__=='__main__':
    win32serviceutil.HandleCommandLine(PythonService)
