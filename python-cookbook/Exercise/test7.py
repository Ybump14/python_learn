import json
import sys

python_version = sys.version[0]

if python_version == '3':
    basestring = str


def format_json(content):
    """
    格式化JSON
    """
    if isinstance(content, basestring):
        content = json.loads(content)

    if python_version >= '3':
        result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
            encode('latin-1').decode('unicode_escape')
    else:
        result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
            decode("unicode_escape")

    return result


class AnalysisJson:
    """解析接口返回json，根据key拿到value"""

    def __init__(self, data):
        self.data = data
        if isinstance(self.data, str):
            print('*****log :data is str')
            self.data = json.loads(self.data)
            print('*****log :data is converted to dict')

    key_list = []

    def analysis_json(self, key):
        """
        :param key:需要查找的key
        :return:返回查找结果list
        """
        if isinstance(self.data, dict):
            for keys in self.data.keys():
                # print('*****log :keys %s' % keys)
                # print('*****log :value type is %s and value is %s' % (type(self.data.get(keys)), self.data.get(keys)))
                # print(data_key, data_value)
                if isinstance(self.data.get(keys), (dict, list)):
                    AnalysisJson(self.data.get(keys)).analysis_json(key)
                else:
                    if key == keys:
                        # print('*****log :key "%s"+ is exist,value is "%s"' % (keys, self.data.get(keys)))
                        self.key_list.append(self.data.get(keys))
                        # print('*****log :key_list value is "%s"' % self.key_list)
        elif isinstance(self.data, list):
            for array in self.data:
                AnalysisJson(array).analysis_json(key)
        return self.key_list
