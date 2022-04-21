# import imaplib
# pip install imapclient
# pip install --upgrade setuptools
# pip install pyzmail

import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('wilczekkamil314@gmail.com', 'Nowehaslo880!')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['ALL'])
print(UIDs)

raw_message = conn.fetch([41], ['BODY[]', 'FLAGS'])
print(raw_message)
message = pyzmail.PyzMessage.factory(raw_message[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

print(message.text_part)
print(message.html_part)
print(message.text_part.charset)

print(message.text_part.get_payload().decode('UTF-8'))

conn.list_folders()

conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['ON 24-Sep-2020'])
print(UIDs)
# conn.delete_messages([47474])
# conn.delete_messages([UIDs])
