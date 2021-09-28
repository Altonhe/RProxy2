import zipfile
import os
import requests
import tarfile
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

filename = ''
resp = requests.get('https://api.github.com/repos/caddyserver/caddy/releases/latest')
assets = resp.json()["assets"]
for i in assets:
    if i["name"].endswith('linux_arm64.tar.gz'):
        filename = download_file(i["browser_download_url"])
        
tar = tarfile.open(filename)
names = tar.getnames()
for name in names:
  tar.extract(name,path="./tmp")
tar.close()

shutil.move(r'./tmp/caddy', r'./RProxy2/caddy2/caddy')

startdir =r'./RProxy2' 
file_news = startdir +'.zip' 
z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
for dirpath, dirnames, filenames in os.walk(startdir):
    fpath = dirpath.replace(startdir,'') 
    fpath = fpath and fpath + os.sep or ''
    for filename in filenames:
        z.write(os.path.join(dirpath, filename),fpath+filename)
z.close()
print ('build suceess')