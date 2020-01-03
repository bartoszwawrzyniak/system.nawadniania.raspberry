import requests

v_url='https://ssl.smsapi.pl/sms.do?username=dzial.it@tfp.com.pl&password=1d1a99f96b751938e01762377c4f8697&from=TFP IT&to=48603780613&message=exec(open('last_watered').read())'

r = requests.get(v_url)

page_source = r.content

print(page_source)