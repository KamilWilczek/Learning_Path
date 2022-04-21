import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))


namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1******', 'Agent Alice gave the secret documents to Agent Bob.'))


# re.compile(r'\(\d\d\d)(-)?\d\d\d-\d\d\d\d') # (415) 555-5555, 415-555-5555
re.compile(r'''
(\d\d\d-)|    # area code (without parens, with dash)
(\(\d\d\d))   # -or- area code with parens and no dash
\d\d\d        # first 3 digits
-             # second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}    # extension, like x1234''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

