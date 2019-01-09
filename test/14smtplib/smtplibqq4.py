'''
python3利用smtplib发送邮件
使用qq邮箱发送附件给
首先创建MIMEMultipart(实例，构造附件，如果有多个附件可以依次构建)

'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

QQ_SMTP_SERVER='smtp.qq.com'
QQ_SMTP_PORT=465
QQ_MAIL_AUTH=''

from_user='zhangbailong945@qq.com'
from_user_pass=QQ_MAIL_AUTH
to_user='long@amiam.com'

def mail():
    ret=True
    try:
        #创建邮件发送服务器
        server=smtplib.SMTP_SSL(QQ_SMTP_SERVER,QQ_SMTP_PORT)
        #登录到服务器
        server.login(from_user,from_user_pass)
        #写邮件
        #邮件的内容
        content='''
        <h1>发送附件</h1>
        <h3>python3 测试</h3>
        <div style="border:1px solid blue;">
        <span>from email.mime.multipart import MIMEMultipart</span>
        </div>
        '''
        msg=MIMEMultipart()
        #发送者
        msg['From']=formataddr(['loach',from_user])
        #接收者
        msg['To']=formataddr(['long',to_user])
        #主题
        msg['Subject']='发送附件!'
        #邮件内容
        msg.attach(MIMEText(content,'html','utf-8'))

        #构造附件1
        att1=MIMEText(open('python3.txt','rb').read(),'base64','utf-8')
        att1['Content-Type']='application/octet-stream'
        #文件名称，邮件中显示的名字
        att1['Content-Disposition']='attachment;filename="python3.txt"'
        msg.attach(att1)

        #构造附件2
        att2=MIMEText(open('test.txt','rb').read(),'base64','utf-8')
        att2['Content-Type']='application/octet-stream'
        #文件名称，邮件中显示的名字
        att2['Content-Disposition']='attachment;filename="test.txt"'
        msg.attach(att2)

        #发送邮件
        server.sendmail(from_user,[to_user,],msg.as_string())
        server.quit()
    except smtplib.SMTPException:
        ret=False
    return ret

ret=mail()
if ret:
    print('发送附件成功!')
else:
    print('发送失败!')

