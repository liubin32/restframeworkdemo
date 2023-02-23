import requests
import json

cookies = {
    'qgqp_b_id': 'f17d5415a30e368a9a326292bdb20b2b',
    'st_si': '98441134133811',
    'st_pvi': '10433408100586',
    'st_sp': '2023-01-16%2013%3A02%3A49',
    'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
    'st_sn': '23',
    'st_psi': '20230223163959920-113300300813-9532996020',
    'st_asi': '20230223163959920-113300300813-9532996020-dfcfwsy_dfcfwxsy_ycl_ewmxt-3',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': 'https://data.eastmoney.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'qgqp_b_id=f17d5415a30e368a9a326292bdb20b2b; st_si=98441134133811; st_pvi=10433408100586; st_sp=2023-01-16%2013%3A02%3A49; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=23; st_psi=20230223163959920-113300300813-9532996020; st_asi=20230223163959920-113300300813-9532996020-dfcfwsy_dfcfwxsy_ycl_ewmxt-3',
}

response = requests.get(
    # 'https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112306599580786479728_1677141653429&fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124%2Cf1%2Cf13',
    'https://push2.eastmoney.com/api/qt/clist/get?fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124%2Cf1%2Cf13',
    cookies=cookies,
    headers=headers,
)

# 数据清洗
print(response.text)
print(type(response.text))

res_dict = json.loads(response.text)
print(res_dict)
print(type(res_dict))