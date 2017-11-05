from rake_nltk import Rake 

r = Rake()
text = "RAKE short for Rapid Automatic Keyword Extraction algorithm, is a domain independent keyword extraction algorithm which tries to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurance with other words in the text."
r.extract_keywords_from_text(text)
key = r.get_ranked_phrases()

print(key)