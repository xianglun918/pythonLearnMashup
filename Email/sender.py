from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# 转换成标准格式（因为包含中文）
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 获取登录信息
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

# formataddr的意义是装换成特定格式例如: '=?utf-8?q?python?= <xianglun@qq.com>'
# 以便于服务器理解
# 把plain换成html可以发送网页格式邮件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

### 发送附件的方法：
# # 邮件对象:
# msg = MIMEMultipart()
# msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
# with open('/Users/michael/Downloads/test.png', 'rb') as f:
#     # 设置附件的MIME和文件名，这里是png类型:
#     mime = MIMEBase('image', 'png', filename='test.png')
#     # 加上必要的头信息:
#     mime.add_header('Content-Disposition', 'attachment', filename='test.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来:
#     mime.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)

# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +      # 将照片添加的附件之后嵌入到邮件正文中
#     '<p><img src="cid:0"></p>' +
#     '</body></html>', 'html', 'utf-8'))

# 如果需要备选文本显示方案，在构建时输入'alternative'
# msg = MIMEMultipart('alternative')
###

# smtp默认端口25
server = smtplib.SMTP(smtp_server, 25)
# 对于有些需要SSL加密的服务器，指定端口并使用starttls()方法
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
# 输出所有与服务器的交互信息
server.set_debuglevel(1)
# 登录服务器
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, [to_addr], msg.as_string())
# 退出
server.quit()