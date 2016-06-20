# -*- coding: utf-8 -*-
import json, random, MeCab
import detection
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
        res = m.parse(encode_text)
        return res.decode('utf-8')

def vec(arr):
	from sklearn.feature_extraction.text import CountVectorizer
	vectorizer = CountVectorizer(min_df=1)
	X = vectorizer.fit_transform(arr)
	return X.toarray()



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

	vec_corpus = vec(tmp)	
	np.save('../processed_data/AP_patient.npy', vec_corpus)


