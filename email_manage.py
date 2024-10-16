# 邮件发送
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:

    def send_emial(self):
        # 定义SMTP服务器
        smtpserver = 'smtp.163.com'
        # 发送邮件的客户名和授权码
        username = "18344186993@163.com"
        password = "RW32NSPcsn5kFRep"
        # 接收邮箱
        receiver = "825510546@qq.com"
        # 邮件对象
        message = MIMEMultipart('related')
        subject = "接口自动化测试报告"  # 邮件主题
        fujian = MIMEText(open('./report/index.html', 'rb').read(), 'html', 'utf-8')  # 附件
        # 把邮件信息组装到邮件对象
        message['from'] = username
        message['to'] = receiver
        message['subject'] = subject
        message.attach(fujian)
        # 登录stmp服务器发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(username, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    EmailManage().send_emial()
