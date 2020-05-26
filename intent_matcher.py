from web_scraper import find_data_for_country

def process_input(user_input):
	#Convert input sentence into a list of words, and capitalise first letter of each word
	input_words = user_input.split()
	input_words = [x[0].upper()+x[1:] for x in input_words]

	for word in input_words:
		output_dict,output_str,found = find_data_for_country(word)

		if found:
			for key in output_dict.keys():
				if set(key.split()) <= set(input_words): 	#Checks if any of the dictionary keys are present in users input, eg: Active Cases in tell me the no of active cases in india 
					output_str = '{} of COVID 19 in {} are {}'.format(key,word,output_dict[key])
					return output_str
			return output_str #Print all stats of the country if no intent is matched
	return 'Please try again' #In case no matching country is found