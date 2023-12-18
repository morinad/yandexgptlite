import requests
import json

class YandexGPTLite:
    def __init__(self, folder: str , token: str):
        self.iamtoken = self.generate_iamtoken(token)
        self.folder = folder

    def generate_iamtoken(self, token: str):
        token_url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
        token_data = {"yandexPassportOauthToken": token}
        token_response = requests.post(token_url, data=json.dumps(token_data))
        iamToken = token_response.json()['iamToken']
        return iamToken

    def create_completion(self, prompt: str, temperature):
        headers={"Authorization" : "Bearer " + self.iamtoken, "x-folder-id" : self.folder }
        body = {"modelUri": f"gpt://{self.folder}/yandexgpt-lite/latest",  "completionOptions":
            {"stream": False,    "temperature": str(temperature),    "maxTokens": "100000"},
                  "messages": [{"role": "user", "text": prompt}]}
        jsondata = json.dumps(body, ensure_ascii=False).encode("utf8")
        web = requests.post("https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                           headers = headers, data = jsondata)
        try:
            try: result = web.json()['result']['alternatives'][0]['message']['text']
            except: result = web.json()['error']['message']
        except: result = web.text
        return result


