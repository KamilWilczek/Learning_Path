import shutil

shutil.copy('D:\\Kursy\\Automate the boring stuff\\S11-Files\\X\\spam.txt',
            'D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y')

shutil.copy('D:\\Kursy\\Automate the boring stuff\\S11-Files\\X\\spam.txt',
            'D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y\\spamspamspam.txt')

shutil.copytree('D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y',
                'D:\\Kursy\\Automate the boring stuff\\S11-Files\\Y_backup')

# shutil.move('D:\\Kursy\\Automate the boring stuff\\S11-Files\\X\\spam.txt',
#            'D:\\Kursy\\Automate the boring stuff\\S11-Files\\XY')

# shutil.move('D:\\Kursy\\Automate the boring stuff\\S11-Files\\XY\\spam.txt',
#            'D:\\Kursy\\Automate the boring stuff\\S11-Files\\XY\\eggs.txt')
