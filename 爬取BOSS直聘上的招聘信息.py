from DrissionPage import ChromiumPage
from pprint import pprint
import json
import pandas as pd
import os
dp = ChromiumPage()
dp.listen.start('zhipin.com/wapi/zpgeek/search/joblist.json?')
all_data=[]
dp.get('https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&city=101280600')
for page in range(1,11):
    print(f'正在采集第{page}页数据')
    dp.scroll.to_bottom()
    resp = dp.listen.wait()
    json_data = resp.response.body
    jobList = json_data['zpData']['jobList']
    data = []
    for index in jobList:
        dit = {
            '公司': index.get('brandName'),
            '公司规模': index.get('brandScaleName'),
            '职位': index.get('jobName'),
            '地区': index.get('areaDistrict'),
            '地点': index.get('businessDistrict'),
            '学历': index.get('jobDegree'),
            '薪资': index.get('salaryDesc'),
            '技能要求': ''.join(index.get('skills', []))
            }
        data.append(dit)
    all_data.extend(data)
    dp.ele('css:.options-pages a:last-of-type').click()
    df = pd.DataFrame(all_data)
    file_path = 'xxxxxxx'
    df.to_excel(file_path, index=False)
    print(f"Data has been saved to {file_path}")

