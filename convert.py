import sys,re
oweb=''
tweb=''
t=[]
p=[]
print('请输入源网站')
while True:
    line1 = sys.stdin.readline().strip().replace('server_name','')
    if line1 == '':
        break
    line1=re.findall(r'(?:[-\w.]|(?:%[\da-fA-F]{2}))+',line1)
    t.append(line1[0])
    oweb=', '.join(t)
print('请输入要代理的网站')
while True:
    line2 = sys.stdin.readline().strip().replace('server_name','')
    if line2 == '':
        break
    line2=re.findall(r'((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))',line2)
    p.append(line2[0])
    tweb=' '.join(p)
if oweb !='' and tweb !='':
    oweb=oweb.replace("-",".")
    c=''
    c+=oweb + ' { \n'
    c+='tls steamcommunity.crt steamcommunity.key \n'
    c+='reverse_proxy '+tweb+' { \n'
    c+='header_up Host {host} ' +'\n'
    if True:
        c+='transport http_ntlm { \n'
        c+='tls_insecure_skip_verify \n'
        c+='} \n'

    c+='} \n'
    c+='} \n'
    print('\ncaddy file is \n \n')
    print(c)
# f=open(r'C:\Users\Public\Desktop\CaddyFileNew','w+')
# f.write(c)
# f.close()