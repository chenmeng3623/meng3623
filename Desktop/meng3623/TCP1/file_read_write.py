##文件读写
# coding=utf-8
from datetime import date

class FileReadWrite():
    ##初始化
    def __init__(self,speakername,chatcontent):
        self.speaker = speakername        ##说话人名字
        self.chat = chatcontent           ##聊天内容
        self.year = date.today().year     ##年
        self.month = date.today().month   ##月
        self.day = date.today().day       ##日
        self.filename = str(self.year)+'_'+str(self.month)+'_'+str(self.day)+'.txt' ##文件名字
        return

    ##保存聊天记录
    def save(self):
        t =''
        with open(self.filename, "a") as f:
            t = t + self.speaker + ":" +self.chat
            f.write(t)
            f.write('\n')
            t = ''
