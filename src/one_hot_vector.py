# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs
import collections
import numpy as np

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def parse_text(text, tagger):
	encode_text = text.encode('utf-8')
        res = tagger.parse(encode_text)
        return res.decode('utf-8')

def vec(arr):
	print arr[0]
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer(min_df=1)
	X = vectorizer.fit_transform(arr)
	index = vectorizer.get_feature_names()
	return X.toarray(), index

def return_vector(arr_index, text):
	return arr_index.index(text)

def neighbor_matrix(arr_text, index_corpus):
	s_matrix = np.zeros((len(index_corpus), len(index_corpus)))	
	arr_text = arr_text.split(" ")
	del arr_text[-1]
	for t in xrange(len(arr_text)):
		try:
			i = index_corpus.index(arr_text[t])
			if t > 0:
		        	m1 = index_corpus.index(arr_text[t-1])
                        	s_matrix[i][m1] += 1
                	if t < len(arr_text)-1:
                        	m2 = index_corpus.index(arr_text[t+1])
                        	s_matrix[i][m2] += 1
		except:
			pass
	return s_matrix
		
	

if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	print "Number of Patient is %s"%num_patients

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")

	
	tmp = []
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		tmp.append(parse_text(text, m))

	vec_corpus, index_corpus = vec(tmp)
	np.save('../processed_data/AP_patient.npy', vec_corpus)

	f = codecs.open("../processed_data/word_index.txt","w","utf-8")
	for word in index_corpus:
		f.write(word)
		f.write(",")
	f.close()

	print return_vector(index_corpus, index_corpus[55])
	w_range = 5
	sm_tensor = []
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		arr_text = parse_text(text, m)
		mat = neighbor_matrix(arr_text, index_corpus)
		sm_tensor.append(mat)


