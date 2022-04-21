import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)

resume = '''JESSE KENDALL 123 Elm Street, Fall River, MA 02723, Cell: 508-555-5555, 508-555-1234, twemel@charter.net 
SUMMARY OF QUALIFICATIONS Dedicated cell phone sales professional with demonstrated success in retail management, 
product presentation, and customer service. Proven ability to assess client needs; establish rapport, build trust, 
and close deals. Meet and exceed sales objectives and challenging goals. Proficient in Microsoft Office (Word, Excel, 
PowerPoint, Access), and H/O billing systems. SALES SUCCESS RETAIL STORE SALES MANAGER, 20xx – 20xx ABC CELLULAR, 
Fall River, MA Recruited, hired, trained, developed, and directed retail sales teams for two retail ABC Wireless 
dealer stores. Oversaw client relations, new account development, and customer service. Supervised administrative 
functions, inventory, cash flow, merchandising, and operations. Conducted ongoing staff development and personal 
growth planning for employees. Implemented a sales-tracking spreadsheet to replace a manual form writing process to 
increase efficiency. Developed innovative and effective marketing programs; exceeded store sales quotas. Successfully
 managed one of the highest-producing ABC Wireless dealer locations in the San Diego market. Received several “Sales 
 Manager of the Month” Awards. Created a team spirit within the stores that resulted in increased sales, long-term 
 employees, and customer satisfaction. CELL PHONE SALES REPRESENTATIVE, 20xx – 20xx BCD CELL PHONE HUT, Fall River, 
 MA Partnered with a high-performing sales staff to provided quality customer service. Served as a customer advocate; 
 interfaced with the clients’ designated program administrators to provide product and service solutions and meet 
 individual customer needs. Assisted customers with billing and expense management, post sale customer education on 
 wireless service and equipment, issue resolution, and technical troubleshooting. Effectively delivered post-sale care 
 services, exceeding clients’ expectations in a cost-effective manner. Obtained significant business by delivering 
 presale presentations to demonstrate new phone features. CUSTOMER SERVICE REPRESENTATIVE, 20xx – 20xx CDE CELLULAR 
 SERVICES, Fall River, MA Responded to billing inquiries, assisted in technical troubleshooting, and performed rate 
 plan analysis. Provided friendly and professional customer service while answering over 90 inbound calls per day. 
 Chosen to facilitate training in an outsourced call center. EDUCATION Bachelor of Arts in Communication 
 (Major: Advertising), 20xx XYZ UNIVERSITY, Milwaukee, WI REFERENCES Excellent references provided upon request.'''

print(phoneRegex.search(resume))
print(phoneRegex.findall(resume))
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume))

digitRegex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)')

lyrics = '''12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
5 golden rings
4 calling birds
3 french hens
2 turtle doves, and
1 partridge in a pear tree'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u|...)
print(vowelRegex.findall('Robocop eats baby food.'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food.'))

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocopo eats baby food.'))
