from pkg.topic import Topic
import itchat


def send_group(group, msg):
    rooms = itchat.get_chatrooms(update=True)
    rooms = itchat.search_chatrooms(name=group)
    if not rooms:
        print("None group found")
    else:
        itchat.send(msg, toUserName=rooms[0]["UserName"])


if __name__ == '__main__':
    a, b, c, d = Topic().start()
    msg = "今日学位英语: (难度" + d + ")\n\n" + a + "\n\n" + b
    # print(msg)
    # print(a,"\n",b,"\n",c,"\n",d)
    itchat.auto_login(hotReload=False)
    send_group(u"爱吃早餐群", msg)
    itchat.run()



