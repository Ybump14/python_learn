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

    key_list = []

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, str):
            self._data = json.loads(value)
        self._data = value

    def analysis_json(self, key):
        """
        :param key:需要查找的key
        :return:返回查找结果list
        """
        if isinstance(self.data, dict):
            for keys in self.data.keys():
                if isinstance(self.data.get(keys), dict):
                    AnalysisJson(self.data.get(keys)).analysis_json(key)
                elif isinstance(self.data.get(keys), list):
                    tag = False
                    for array in self.data.get(keys):
                        if isinstance(array, dict):
                            AnalysisJson(array).analysis_json(key)
                        else:
                            tag = True
                    if tag:
                        if key == keys:
                            self.key_list.append(self.data.get(keys))
                else:
                    if key == keys:
                        self.key_list.append(self.data.get(keys))
        elif isinstance(self.data, list):
            for array in self.data:
                if isinstance(array, dict):
                    AnalysisJson(array).analysis_json(key)
        return self.key_list


case1 = {
    "classify": "剧情1",
}
case2 = {
    "classify": ["剧情2", "爱情2"],
}
case3 = {
    "classify": [{"classify": "剧情3", "classify1": "爱情3"}],
}
case4 = {
    "classify": {"classify": [{"classify": "剧情4", "classify1": "爱情4"}]},
}

# print(AnalysisJson(case1).analysis_json('classify'))
# print(AnalysisJson(case2).analysis_json('classify1'))
print(AnalysisJson(case3).analysis_json('classify1'))
# print(AnalysisJson(case4).analysis_json('classify1'))
