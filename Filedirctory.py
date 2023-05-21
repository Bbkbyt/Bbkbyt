import os
import shutil
os.chdir(r'C:\Users\babak\Desktop\python programs\filedirectory')
if(os.path.isdir('path')==False):
    os.mkdir('path')
file=open('sample.txt', mode='a')
file.write('hell yeah ')
file.close()
s=os.getcwd()
source=r'C:\Users\babak\Desktop\python programs\filedirectory\sample.txt'
destination=r'C:\Users\babak\Desktop\python programs\filedirectory\path'
shutil.copy2(source,destination)
if(os.path.exists('spl.txt')==True):
    os.rename('spl.txt','spl2.txt')
    os.remove('spl2.txt')
