import smtplib

from email.mime.text import MIMEText
from email.utils import formataddr
'''
python 用qqmail发送纯文本邮件
'''

'''
qlzzyfqtpvvlgcje
'''
QQ_MAIL_AUTH='qlzzyfqtpvvlgcje'

my_sender='1207549344@qq.com'
my_pass=QQ_MAIL_AUTH
to_users='long@amiam.com'

def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(['loach',my_sender])
        msg['To']=formataddr(['long',to_users])
        msg['subject']='邮件主题'
        #发送邮件服务器
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        #登录
        server.login(my_sender,my_pass)
        #发送邮件
        server.sendmail(my_sender,[to_users,],msg.as_string())
        server.quit()
    except smtplib.SMTPException:
        ret=False
    return ret


ret=mail()
if ret:
    print('邮件发送成功!')
else:
    print('邮件发送失败!')