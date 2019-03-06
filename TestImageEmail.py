#-*- coding:utf-8 -*-
import smtplib
from email.mime.image import MIMEImage

class TestImageEmail():
    def imageEml(self):
        smtpServer="smtp.163.com"
        user="l901121w@163.com"
        password="901121"
        sender="l901121w@163.com"
        receiver="l901121w@163.com"

        subject=u"发送图片邮件"

        #发送1张图片
        imageFile=open(r"C:\Users\Administrator\Desktop\1.PNG","rb").read()
        msg=MIMEImage(imageFile)
        msg.add_header('Content-ID','<image1>')#图片ID
        msg["Subject"]=subject
        msg["To"]=receiver

        smtp=smtplib.SMTP()
        smtp.connect(smtpServer)
        smtp.login(user,password)
        smtp.sendmail(sender,receiver,msg.as_string())

if __name__ == '__main__':
    TestImageEmail().imageEml()