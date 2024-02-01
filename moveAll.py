import os

currFiles = os.listdir('./')
targetDirImg = 'Images/'
targetDirPaper = 'Questions/'

for file in currFiles:
    if file.endswith('.png'):
        os.rename(file, targetDirImg+file)
        print(file, 'moved to', targetDirImg+file)
    elif file.endswith('.md') and file.split('.')[0].isdigit():
        os.rename(file, targetDirPaper+file)
        print(file, 'moved to', targetDirPaper+file)
print('Done!')