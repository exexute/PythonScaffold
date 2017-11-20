'''''
Created on 2017-11-20

@author: Execute
'''
from email.mime.text import MIMEText
from email.utils import formatdate, make_msgid
from smtplib import SMTP_SSL

class E_Mail:
    def __init__(self, server, username, pwd, _from, _tos, _subject, _content, _type = None):
        self.__server = server
        self.__username = username
        self.__pwd = pwd

        self._from = _from
        self._tos = _tos
        self._subject = _subject
        self._content = _content
        self._type = _type
    def __login_server(self):
        self.smtp = SMTP_SSL(self.__server)
        self.smtp.login(self.__username, self.__pwd)
    def __logout_server(self):
        self.smtp.quit()
    def __send_mail(self):
        msg = None
        if self._type:
            msg = MIMEText(self._content, _subtype=self._type, _charset='utf-8')
        else:
            msg = MIMEText(self._content)
        msg["From"] = self._from
        msg["Subject"] = self._subject
        msg["Date"] = formatdate(localtime=1)
        for _to in self._tos:
            msg["To"] = _to
            msg["Message-ID"] = make_msgid()
            self.smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    def sendmail(self):
        self.__login_server()
        self.__send_mail()
        self.__logout_server()

'''
Example 1:发送html格式的邮件:
    mail_content = "<span>This is a auto-send mail.</span>"
    mail = E_Mail("smtp.qq.com", "execute@qq.com", password, "send_user@qq.com", ["recv1@qq.com", "recv2@qq.com"], "Test Moudle", mail_content, "html")
    mail.sendmail()

 Example 2:发送文本格式的邮件：
    mail_content = '''
      Hi,
        This is a auto-send mail.
    '''
    mail = E_Mail("smtp.qq.com", "execute@qq.com", password, "send_user@qq.com", ["recv1@qq.com", "recv2@qq.com"], "Test Moudle", mail_content)
    mail.sendmail()
'''
