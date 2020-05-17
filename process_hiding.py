import psutil
import wmi

#查看所有的进程
def search_pid():
    print("进程列表：")
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if pid<500:
            print("进程ID: {0:3},  进程名: {1:10}".format(pid,p.name()))
    print("…………………")
    print("--------进程总数：{}--------".format(len(pids)))

#列出正在运行的服务和已停止的服务
def service():
    c = wmi.WMI()
    print("正在运行的服务：")
    num1 = 0
    for s in c.Win32_Service():
        num1 += 1
        if num1<10:
            print("ID：{0:5}    服务名：{1:10}    描述：{2:10}".format(s.ProcessId,s.Name,s.Caption))
    print("…………………")
    print("--------正在运行服务总数为:{}--------".format(num1))
    stopped_services=c.Win32_Service(State="Stopped")
    num2 = 0
    print("已停止的服务：")
    for s in stopped_services:
        num2 += 1
        if num2<10:
            print("ID：{0:5}    服务名：{1:10}    描述：{2:10}".format(s.ProcessId,s.Name,s.Caption))
    print("……………………")
    print("--------已停止的服务总数为:{}--------".format(num2))

search_pid()
service()
