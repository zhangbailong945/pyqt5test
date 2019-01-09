#SMTP发送邮件
'''
SMTP(simple mail transfer protocol)即简单邮件传输协议，
它是一组由原地址到目的地址传送邮件的规则，由它来控制的中转方式。
python的smtplib提供了一种很方便的途径发送电子邮件。
'''

import smtplib

#1.创建SMTP对象
''''
smtpObj=smtplib.SMTP([host,port,local_hostname])
host.SMTP 服务器主机，可以指定主机IP或者域名
prot SMTP服务使用的端口号，一般SMTP端口号为25
local_hostname 如果SMTP服务器在本机上，指定服务器为localhost

'''

#2.发送邮件
'''
STMP.sendmail(from_addr,to_addrs,msg[mail_options,rcpt_options])
#from_addr:邮件发送者diZHi
#to_addrs:字符串列表，邮件发送地址
#msg:发送消息,msg是字符串，表示邮件。邮件一般由标题，发行人，收件人，邮件内容，附件扥构成。
'''
from email.mime.text import MIMEText
from email.header import Header

sender='long@amiam.com' #发送者，
receivers=['1207549344@qq.com'] #接收者列表

#三个参数：第一个为文本内容，第二个为文本格式，第三个为编码
message=MIMEText('python smtplib邮件发送测试','plain','utf-8')
message['From']=Header('smtplib测试','utf-8')
message['To']=Header('测试','utf-8')

subject='Python SMTP邮件测试'


try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功!')
except smtplib.SMTPException:
    print('Error:无法发送邮件')