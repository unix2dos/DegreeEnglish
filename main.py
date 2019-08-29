import time
import datetime
import threading
import itchat
from topic import Topic


def send_group(group, msg):
    rooms = itchat.get_chatrooms(update=True)
    rooms = itchat.search_chatrooms(name=group)
    if not rooms:
        print("None group found")
    else:
        itchat.send(msg, toUserName=rooms[0]["UserName"])



def tomorrow(fmt):
    now_time = datetime.datetime.now()
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    str_time = "{}-{}-{} {}".format(next_year,next_month,next_day,fmt)
    next_time = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    diff = (next_time - now_time).total_seconds()
    return diff


def today(fmt):
    diff = datetime.datetime.strptime(fmt, '%H:%M:%S') - datetime.datetime.strptime(time.strftime("%H:%M:%S"), '%H:%M:%S')
    return diff.seconds


def topic():
    # group = u"爱吃早餐群"
    group = u"养老区交流协会V2.0"
    a, b, c, d = Topic().start()
    msg = "今日学位英语: (难度" + d + ")\n\n" + a + "\n\n" + b
    send_group(group, msg)
    time.sleep(60)
    send_group(group, c)
    timer = threading.Timer(86400, topic)
    timer.start()


if __name__ == '__main__':
    # timer = threading.Timer(today("22:10:00"), topic)
    timer = threading.Timer(tomorrow("09:00:00"), topic)
    timer.start()
    itchat.auto_login(hotReload=True)
    itchat.run()