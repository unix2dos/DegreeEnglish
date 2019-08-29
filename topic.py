import requests


class Topic(object):
    def __init__(self):
        self.imei = "6f2252fcb3ed40bd90a618735970a2a9"

    def start(self):
        knowId = self.get_knowId()
        res = self.get_topic(knowId)
        self.do_topic(res)
        return self.send(res)


    def get_knowId(self):
        url = "http://adenglish.sikai.net.cn/xwenglish/na/exercise/getStudyPath"
        params = {"imei":self.imei, "itemType": 1}

        resp = requests.post(url, params=params).json()
        if resp["error"] != None :
            return

        return resp["result"]["tkId"]


    def get_topic(self, knowId):
        url = "http://adenglish.sikai.net.cn/xwenglish/na/exercise/getAdaptivePraxis"
        params = {"imei":self.imei, "knowId": knowId}

        resp = requests.post(url, params=params).json()
        if resp["error"] != None:
            return

        return resp["result"]

    def do_topic(self, res):
        url = "http://adenglish.sikai.net.cn/xwenglish/na/exercise/submitTest4OnePraxis"
        item_id = res["content"][0]["itemId"]
        answer_index = res["content"][0]["answerIndex"]
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        data = "answers=%5B%0A%20%20%7B%0A%20%20%20%20%22doPraxisTime%22%20%3A%2013101%2C%0A%20%20%20%20%22itemType%22%20%3A%201%2C%0A%20%20%20%20%22standerAns%22%20%3A%20%224%22%2C%0A%20%20%20%20%22itemId%22%20%3A%20%22{}%22%2C%0A%20%20%20%20%22userAnsIndex%22%20%3A%20%22{}%22%0A%20%20%7D%0A%5D&exerciseType=1&imei=6f2252fcb3ed40bd90a618735970a2a9&paperId=&status=1".format(item_id,answer_index)
        requests.post(url, data=data, headers=headers)


    def send(self, res):
        content = res["content"][0]
        topic = content["topic"]
        options = ""
        for k, v in enumerate(content["options"]):
            options += chr(k+65) + ".   " +  v["content"] + "\n\n"
        analysis = content["analysis"]["analysisContent"]
        difficulty = content["difficulty"]
        return topic, options, analysis, difficulty
