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
                if isinstance(self.data.get(keys), dict):
                    AnalysisJson(self.data.get(keys)).analysis_json(key)
                elif isinstance(self.data.get(keys), list):
                    if key == keys:
                        self.key_list.append(self.data.get(keys))
                    for arr in self.data.get(keys):
                        if isinstance(arr, dict):
                            AnalysisJson(self.data.get(keys)).analysis_json(key)
                else:
                    if key == keys:
                        self.key_list.append(self.data.get(keys))
        elif isinstance(self.data, list):
            for array in self.data:
                AnalysisJson(array).analysis_json(key)
        return self.key_list


data = {"url": "https://movie.douban.com/subject/1295865/", "title_chinese": "\u71c3\u60c5\u5c81\u6708",
        "title_others": ["Legends of the Fall", "\u79cb\u65e5\u4f20\u5947", "\u771f\u7231\u4e00\u4e16\u60c5(\u53f0)"],
        "director": "\u5bfc\u6f14: \u7231\u5fb7\u534e\u00b7\u5179\u5a01\u514b Edward Zwick\u00a0\u00a0\u00a0",
        "year": 1994, "country": "\u7f8e\u56fd",
        "classify": ["\u5267\u60c5", "\u7231\u60c5", "\u6218\u4e89", "\u897f\u90e8"], "rating_num": 8.8,
        "rating_people": 232262,
        "quote": "\u4f20\u5947\uff0c\u4e0d\u662f\u6bcf\u4e2a\u4eba\u90fd\u53ef\u4ee5\u62e5\u6709\u3002",
        "title": [{"title_others": "testhuoqu"}]}
print(AnalysisJson(data).analysis_json('title_others'))
