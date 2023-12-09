import requests
import json

# Read File
def __ReadFile(pPath):
    f = open(pPath, 'r')
    data = f.read()
    j = json.loads(str(data))
    f.close()
    return j

BaseURL = 'https://translation.googleapis.com/language/translate/v2'
def GetSupportLanguage(pKey):
    formData = { 'key': pKey, 'target': 'zh-TW' }
    try:
        response = requests.post(BaseURL + '/languages', formData)
        return json.loads(response.text)['data']['languages']
    except:
        print('GetSupportLanguage(): Something went wrong')
    return None

def DetectLanguage(pKey, pText):
    formData = { 'key': pKey, 'q': pText }
    try:
        response = requests.post(BaseURL + '/detect', formData)
        # Example of return
        # {'data': {'detections': [[{'confidence': 1, 'isReliable': False, 'language': 'zh-TW'}]]}}
        return json.loads(response.text)['data']['detections'][0][0]['language']
    except:
        print('DetectLanguage(): Something went wrong')
    return None

def Translate(pKey, pText, pSourceLanguage, pTargetLanguage):
    formData = { 'key': pKey, 'q': pText, 'source': pSourceLanguage, 'target': pTargetLanguage, 'format': 'text' }
    try:
        response = requests.post(BaseURL, formData)
        # Example of return
        # {'data': {'translations': [{'translatedText': 'pText'}]}}
        return json.loads(response.text)['data']['translations'][0]['translatedText']
    except:
        print('Translate(): Something went wrong')
    return None

JsonData = __ReadFile('GoogleAPIKey/GoogleAPIKey.box')

# Google Translate V2
# 1. Get Support Language
# 2. Detect Language
# 3. Translate
key = JsonData['Key']
result1 = GetSupportLanguage(key)
print(f'GetSupportLanguage (Count: {len(result1)})')
print(result1)
print()

testText = '我想要大便，測試'
result2 = DetectLanguage(key, testText)
print(f'DetectLanguage: "{testText}"')
print(result2)
print()

result3 = Translate(key, '我想要大便，測試', 'zh-TW', 'en')
print(f'Traslate: "{testText}"')
print(result3)
print()