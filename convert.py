import sys
oweb=''
tweb=''
print('请输入源网站')
while True
    line1 = sys.stdin.readline().strip()
    if line1 == ''
        break
    oweb+=line1
print('请输入要代理的网站')
while True
    line2 = sys.stdin.readline().strip()
    if line2 == ''
        break
    tweb+=line2
if oweb !='' and tweb !=''
    c=''
    c+=oweb + ' { n'
    c+='tls steamcommunity.crt steamcommunity.key n'
    c+='reverse_proxy '+tweb+' { n'
    c+='header_up Host '+oweb +'n'
    if True
        c+='transport http_ntlm { n'
        c+='tls_insecure_skip_verify n'
        c+='} n'

    c+='} n'
    c+='} n'
    print('n n caddy file is n n')
    print(c)
# f=open(r'CUsersPublicDesktopCaddyFileNew','w+')
# f.write(c)
# f.close()