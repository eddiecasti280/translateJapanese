import requests

def search_item(input):
	query_site = 'https://jisho.org/api/v1/search/words?keyword='+input
	response = requests.get(query_site)
	input_dictionary = response.json()
	result = []

	for definition in range(len(input_dictionary['data'])):
		temp = []
		try:
			temp.append('Word: ' + input_dictionary['data'][definition]['japanese'][0]['word'])
		except KeyError:
			pass
		try: 
			temp.append('Reading: ' + input_dictionary['data'][definition]['japanese'][0]['reading'])
		except KeyError:
			pass

		temp.append('English Translation: ' + ', '.join(input_dictionary['data'][definition]['senses'][0]['english_definitions']))
		result.append(temp)
	return result