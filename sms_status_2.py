import requests

v_url='https://ssl.smsapi.pl/sms.do?username=username_smsapi&password=md5_smsapi&from=TFP IT&to=48603780613&message=Jestem szczesliwa roslina'

r = requests.get(v_url)

page_source = r.content

print(page_source)
