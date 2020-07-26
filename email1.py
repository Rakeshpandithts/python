import imaplib
import pprint
import email
import getpass
import email.header
import datetime
import sys
import pprint
subject = 'Security alert'

imap_host = 'imap.gmail.com'
imap_user = 'rakeshpandith.ts@gmail.com'
imap_pass = 'pandith1234$'

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

# tmp, messages = imap.search(None, 'UNSEEN SUBJECT "{}"'.format(subject))
# ids = messages[0].split()

# print(type(ids))
# for num in ids:
#     print('d')
#     typ, data = imap.fetch(num, '(RFC822)')
#     print('f')
#     print(data[0][1])
#     typ, data = imap.fetch(num, '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')
#     message = data[0][1].lstrip('Subject: ').strip() + ' '
#     print (message)
typ, data = imap.search(None, '(SUBJECT "'+ subject + '")')
# for num in data[0].split():
#     typ, data = imap.fetch(num, '(RFC822.SIZE BODY[HEADER.FIELDS (SUBJECT)])')
#     num=int(num)+1
#     message = data[0][1].lstrip('Subject: ').strip() + ' '
#     print(message.encode())
# imap.close()

for num in data[0].split():
    rv, data = imap.fetch(num, '(RFC822)')
    pprint.pprint(data[0][1])
    # msg = email.message_from_string(data[0][1])
    # sub = msg['Subject']
    # print(sub)
    # decode = email.header.decode_header(str(msg['Subject']))[0]
    # subject = unicode(decode[0])
    # print ('Message %s: %s' % (num, subject))
    # print(decode)