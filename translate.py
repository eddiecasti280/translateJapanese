import requests
from sys import argv

def search_item(input):
	query_site = 'https://jisho.org/api/v1/search/words?keyword='+input
	response = requests.get(query_site)
	input_dictionary = response.json()
	
	print('Showing results for:', input)
	
	for definition in range(len(input_dictionary['data'])):
		try:
			print('Word:', input_dictionary['data'][definition]['japanese'][0]['word'])
		except KeyError:
			pass
		try: 
			print('Reading:', input_dictionary['data'][definition]['japanese'][0]['reading'])
		except KeyError:
			pass

		print('English Translation:', ', '.join(input_dictionary['data'][definition]['senses'][0]['english_definitions']), '\n')

search_item(*argv[1:])