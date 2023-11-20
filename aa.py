import requests

url = "https://emdatah5.eastmoney.com/dc/zjlx/stock?fc=0.000656&fn=%E9%87%91%E7%A7%91%E8%82%A1%E4%BB%BD"

response = requests.get(url)

if response.status_code == 200:
    print("请求成功！")
    print(response.text)
else:
    print(f"请求失败，状态码：{response.status_code}")
