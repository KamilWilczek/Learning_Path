import os

print(os.getcwd())

# deletes single file permanently
# os.unlink('bacon.txt')

# deletes directory permanently, must be empty
# os.rmdir('D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y')

import shutil
# deletes directory and files with everything inside, permanently
# shutil.rmtree('D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y')

# # DRY RUN
# os.chdir(r'D:\\Kursy\\Automate the boring stuff\\temp')
#
# for filename in os.listdir():
#     if filename.endswith('.rxt'):
#         # os.unlink(filename)
#         print(filename)


import send2trash
send2trash.send2trash('D:\\Kursy\\Automate the boring stuff\\temp\\important_file.rxt')