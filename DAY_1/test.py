import csv
import json

'''生成json文件函数'''


def create_json_file(file_name, request_method, request_api, request_name):
    with open("E:\python_learn\data/" + file_name + ".json", 'w', encoding="utf-8") as f:
        data = {
            "request_method": request_method,
            "request_api": request_api,
            "request_name": request_name,
            "request_data": {}
        }
        f.write(json.dumps(data, indent=2, separators=(',', ': '), ensure_ascii=False))


'''读取CSV文件，依照关键字批量生成json文件'''

with open("E:\python_learn\data/python.csv", 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        create_json_file(file_name=row['file_name'],
                         request_method=row['request_method'],
                         request_api=row['request_api'],
                         request_name=row['request_name'])
