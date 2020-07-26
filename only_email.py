import imaplib
import email

server = '104.200.16.198'
serveruser = 'support@medilenz.com'
serverpassword = 'enVadyef3#Lof'
conn = imaplib.IMAP4_SSL(server)
retcode, capabilities = conn.login(serveruser, serverpassword)
conn.select(readonly=1)
print('email conn = {}'.format(conn))


(retcode, messages) = conn.uid('search', None, "UID", '6000:7000')
print(retcode, messages)

