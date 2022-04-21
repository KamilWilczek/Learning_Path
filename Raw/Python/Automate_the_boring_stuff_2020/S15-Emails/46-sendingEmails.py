import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
print(conn)

print(conn.ehlo())
print(conn.starttls())

print(conn.login('wilczekkamil314@gmail.com', 'Nowehaslo880!'))

# conn.sendmail('od', 'do', 'tresc')
conn.sendmail('wilczekkamil314@gmail.com', 'wilczekkamil314@gmail.com', 'Subject: So long...\n\nDear Kamil,\nSo long, '
                                                                        'and thanks for all the fish.\n\n-Kamil')

conn.quit()