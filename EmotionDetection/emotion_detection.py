import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    raw_output = requests.post(url, json = myobj, headers=headers)
    json_output = json.loads(raw_output.text)

    response_code = raw_output.status_code

    if response_code == 200:
        anger_score = json_output['emotionPredictions'][0]['emotion']['anger']
        disgust_score = json_output['emotionPredictions'][0]['emotion']['disgust']
        fear_score = json_output['emotionPredictions'][0]['emotion']['fear']
        joy_score = json_output['emotionPredictions'][0]['emotion']['joy']
        sadness_score = json_output['emotionPredictions'][0]['emotion']['sadness']
    elif response_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

    emotion_dictionary = {
        'anger': anger_score, 
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    if response_code == 200: 
        dominant_emotion = max(emotion_dictionary, key=emotion_dictionary.get)
    elif response_code == 400:
        dominant_emotion = None
    emotion_dictionary['dominant_emotion'] = dominant_emotion
    return emotion_dictionary