import cmudict
import json
import time

"""
	Number of syllables corresponds to the number of lexical stress marks there are
	given in the phonemes.

	Input:
		input_phonemes  List of the phonemes that make up the word

	Output:
		syllable_count  Number of syllables for that word
"""
def calculate_number_of_syllables(input_phonemes):
	phonemes_string = "".join(input_phonemes[0])
	syllable_count = 0
	for letter in phonemes_string:
		if (letter.isdigit()):
			syllable_count += 1
	return syllable_count

if __name__ == "__main__":
	pronunciation_dictionary = cmudict.dict()

	word_count = 0
	output_dictionary = {}
	start_time = time.time()
	for key, value in pronunciation_dictionary.items():
		# Check if it has valid letters (Ignore words with apostrophe's in them)
		is_valid = True
		for index in key:
			if (not index.islower()):
				is_valid = False
				break
		
		number_of_syllables = calculate_number_of_syllables(value)

		# Ignore unwanted words
		if (number_of_syllables == 0 | number_of_syllables >= 4):
			is_valid = False

		if (not is_valid):
			continue
		
		word_count += 1
		output_dictionary[key] = 1
	end_time = time.time()

	# Write results to a json file
	# Format follows same format as https://github.com/dwyl/english-words
	with open('short_word_dictionary.json', 'w') as output_file:
		json.dump(output_dictionary, output_file, sort_keys=True)
	print("Word count: ", word_count)
	print("Calculation time: ", end_time-start_time)
