import requests

v_url='https://ssl.smsapi.pl/sms.do?username=username_sms_api&password=smsapi_md5&from=TFP IT&to=48603780613&message=exec(open('last_watered').read())'

r = requests.get(v_url)

page_source = r.content

print(page_source)
