import requests

v_url='https://ssl.smsapi.pl/sms.do?username=username_SMSAPI&password=PASSWORD_FROM_SMS_API_MD5&from=TFP IT&to=48603780613&message=Rozpoczeto proces podlewania rosliny'

r = requests.get(v_url)

page_source = r.content

print(page_source)
