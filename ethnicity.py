import requests
import json
import sys

apiKey = "**API KEY**"

# https://www.haystack.ai/docs?python#analyze
def getEthnicity(imageData1):
	outputType = "json"
	requestUri = "https://api.haystack.ai/api/image/analyze?output={}&apikey={}&model=ethnicity".format(outputType, apiKey)
	apiResponse = requests.post(requestUri, data=imageData1)
	response = json.loads(apiResponse.text)
	
	ethnicity = response["people"][0]["ethnicity"]["ethnicity"]
	confidence = response["people"][0]["ethnicity"]["confidence"]

	print(ethnicity, confidence)

image1 = sys.argv[1]

with open(image1, "rb") as imageData1:
	getEthnicity(imageData1)