'''
利用smtplib 发送邮件
追加附件和图片显示

'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.header import Header

#发送服务器信息
QQ_SMTP_SERVER='smtp.qq.com'
QQ_SMTP_PORT=465
QQ_SMTP_AUTH=''


#发送者
from_user='zhangbailong945@qq.com'
from_user_pass=QQ_SMTP_AUTH

#接收者
to_user='long@amiam.com'

def mail():
    ret=True
    try:
        #创建发送服务器对象
        server=smtplib.SMTP_SSL(QQ_SMTP_SERVER,QQ_SMTP_PORT)
        #登录
        server.login(from_user,from_user_pass)
        #编写邮件
        msg=MIMEMultipart('related')
        msg['From']=Header('本地loach','utf-8')
        msg['To']=Header('amiam','utf-8')
        subject='python SMTP 邮件测试'
        msg['Subject']=Header(subject,'utf-8')

        msgalternative=MIMEMultipart('alternative')
        msg.attach(msgalternative)

        content='''
        <div style="border:1px solid red;">
        <div style="border:1px solid green;"><h1>python 发送email图片测试</h1></div>
        <div style="border:1px solid blue;"><span><a href="https://www.baidu.com" target="_blank"></a></span></div>
        <div style="border:1px solid yellow;"><img src="cid:image1" /></div>
        </div>
        '''
        msgalternative.attach(MIMEText(content,'html','utf-8'))
        #发送图片
        fp=open('logo.png','rb')
        msgImage1=MIMEImage(fp.read())
        fp.close()
        #定义ID
        msgImage1.add_header('Content-ID','<image1>')
        msg.attach(msgImage1)
        
        #发送邮件
        server.sendmail(from_user,[to_user,],msg.as_string())
        server.quit()
    except smtplib.SMTPException:
        ret=False
    return ret

ret=mail()

if ret:
    print('发送图片成功!')
else:
    print('发送失败！')