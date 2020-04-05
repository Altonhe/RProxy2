import zipfile
import sys,os
startdir =r'path\to\RProxy2' 
print(startdir)
file_news = startdir +'.zip' 
z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
for dirpath, dirnames, filenames in os.walk(startdir):
    fpath = dirpath.replace(startdir,'') 
    fpath = fpath and fpath + os.sep or ''
    for filename in filenames:
        z.write(os.path.join(dirpath, filename),fpath+filename)
z.close()
print ('build suceess')