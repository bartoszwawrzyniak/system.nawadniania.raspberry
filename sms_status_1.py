import requests

v_url='https://ssl.smsapi.pl/sms.do?username=username_sms_api&password=md5_smsapi&from=TFP IT&to=48603780613&message=Potrzebuje wody !'

r = requests.get(v_url)

page_source = r.content

print(page_source)
