import os
import shutil

for folderName, subfolders, filenames in os.walk('D:\\Kursy\\Automate the boring stuff\\S11-Files\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    # from this subfolders delete ones with 'fish' in name
    for subfolder in subfolders:
        if 'fish' in subfolders:
            os.rmdir(subfolder)

    # from this filenames copy '.py' files to other place
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))

