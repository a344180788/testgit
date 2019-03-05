#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class TestTextEmail():
    def textEml(self):
        smtpServer="smtp.163.com"
        user="l901121w@163.com"
        password="901121"
        sender="l901121w@163.com"
        receiver="l901121w@163.com"
        subject=u"发送文本格式的邮件测试"

        text="hasdufiheuhfajhdjk"
        msg=MIMEText(text,"plain","utf-8")
        msg["Subject"]=subject
        msg["To"]=receiver


        smtp=smtplib.SMTP()
        smtp.connect(smtpServer)
        smtp.login(user,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    TestTextEmail().textEml()