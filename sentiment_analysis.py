import requests
import json
# def <function_name>(<input_args>):
#     url = '<relevant_url>'
#     headers = {<header_dictionary>}
#     myobj = {<input_dictionary_to_the_function>}
#     response = requests.post(url, json = myobj, headers=header)
#     return response.text

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    respone = requests.post(url, json = myobj, headers=header)
    return respone.text
