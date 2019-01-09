import smtplib

'''
内容smtplib 发送html格式的邮件
'''

from email.mime.text import MIMEText
from email.utils import formataddr


smtp_server='smtp.qq.com'
smtp_port=465
QQ_MAIL_AUTH=''

from_user='zhangbailong945@qq.com'
from_user_pass=QQ_MAIL_AUTH

to_users='long@amiam.com'

def mail():
    ret=True
    try:
        #指定SMTP服务器
        server=smtplib.SMTP_SSL(smtp_server,smtp_port)
        #登录
        server.login(from_user,from_user_pass)
        #写邮件并格式化
        content='''
        <h1>测试python发送html格式的邮件</h1>
        <br/>
        <hr/>
        <span color='red'>python3<span>
        <div style="border:1px solid blue">smtplib</div>
        '''
        msg=MIMEText(content,'html','utf-8')
        msg['From']=formataddr(['bailong',from_user])
        msg['To']=formataddr(['longge',to_users])
        #邮件标题
        msg['Subject']='python3模块smtplib'

        #发送邮件
        server.sendmail(from_user,[to_users,],msg.as_string())
        #退出
        server.quit()

    except smtplib.SMTPException:
        ret=False
    return ret
ret=mail()

if ret:
    print('发送html格式邮件成功！')
else:
    print('发送失败！')