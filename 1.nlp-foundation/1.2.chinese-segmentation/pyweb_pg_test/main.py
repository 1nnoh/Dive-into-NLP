import web
import sys

sys.path.append("./")
import jieba
import jieba.posseg
import jieba.analyse

urls = (
    '/', 'index',
    '/test', 'test',
)

app = web.application(urls, globals())


class index:
    def GET(self):
        params = web.input()
        content = params.get('content', '')

        result_list = []
        for x, w in jieba.analyse.extract_tags(content, withWeight=True):
            result_list.append(':'.join([x, str(round(w, 3))]))

        res_str = ' '.join(result_list)
        print("res_str: ", res_str)

        return res_str

class test:
    def GET(self):
        print(web.input())
        return '222'

if __name__ == "__main__":
    app.run()
