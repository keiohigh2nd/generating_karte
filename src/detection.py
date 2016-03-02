import nltk

def text_to_tokens(raw):
	tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)
	return tokens, text

def frequent_words(tokens, text):
	fdist = nltk.FreqDist(w.lower() for w in text)
	return fdist.keys()[:5]

def word_count(tokens):
	tokens_l = [w.lower() for w in tokens]
	return len(set(tokens_l))



