import smtplib
from email.mime.text import MIMEText

def send_mail(recipient,subject,message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender_email_id='aduser.movie30@gmail.com'
    sender_email_id_password="test@1234"
    receiver_email_id=recipient
    s.login(sender_email_id, sender_email_id_password)
    msg = MIMEText(message, 'plain')
    msg['Subject']=subject
    s.sendmail(sender_email_id, receiver_email_id, msg.as_string())
    s.quit()
    
