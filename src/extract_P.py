# -*- coding: utf-8 -*-
import json, random, MeCab
import detection, codecs, math
import collections
import numpy as np
import one_hot_vector

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
	index = vectorizer.get_feature_names()
	return X.toarray(), index

def find_P(text, index_corpus, file, m):
	arr = text.split(" ")
	P_list = []
	for word in arr:
		if int(word.find("#")) != -1:
			print word
			fw.write(word)
			fw.write(",")
			tmp = one_hot_vector.parse_text(word, m)
			#P_list.append(tmp)
			#病気名をベクトル化するかはまた別に考えよう
	return tmp

def vectorlize_Plist(patient_plist):
	#病気名を形態素分析してベクトル化した
	#ただしindexは病名だけで有効である
        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(min_df=1)
        X = vectorizer.fit_transform(patient_plist)
        index = vectorizer.get_feature_names()
        return X.toarray(), index		

def find_similar_patients(matrix, query):
	sim_patients = []
	for row_id in xrange(len(matrix)):
		#類似患者の定義
		tmp_dist = matrix[query] - matrix[row_id]
		tmp = np.power(tmp_dist, 2).sum()
		if tmp < 2:
			sim_patients.append(row_id)
	return sim_patients

def find_coexist_words(similar_patients):
	vec_corpus = np.load('processed_data/AP_patient.npy')
	r,c  = len(vec_corpus), len(vec_corpus[0])
	arr = np.zeros((1,c), dtype=np.int)
	for sim in similar_patients:
		arr = vec_corpus[sim] + arr
	print arr

	N = 20
	max_N_list = []
	for i in xrange(N):
		tmp = np.argmax(arr)
		max_N_list.append(tmp)
		arr[0][tmp] = 0	 
	return max_N_list

if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)
	print "Number of Patient is %s"%num_patients

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")

	f = codecs.open("processed_data/word_index.txt","r","utf-8")	
	index_corpus = f.read().split(",")
	f.close()

	patient_plist = []
	fw = codecs.open("processed_data/patinet_plist.txt","w","utf-8")
	for i in xrange(num_patients):
		text = p_json["%s"%i]["0"]["A/P"]
		fw.write(p_json["%s"%i]["0"]["patient_id"])
		fw.write(",")
		patient_plist.append(find_P(text, index_corpus, fw, m))
		fw.write("\n")
	fw.close()


	plist_mat, plist_index =  vectorlize_Plist(patient_plist)
	#4番目の患者に類似する患者群を集める
	similar_patients = find_similar_patients(plist_mat, 4)

	#共起単語の発見
	max_N_list = find_coexist_words(similar_patients)
	max_N_words = []
	tmp = ""
	for i in max_N_list:
		max_N_words.append(index_corpus[i])
		tmp += index_corpus[i]
	#名詞のみ
	print tmp
	encode_text = tmp.encode('utf-8')
        res = m.parseToNode(encode_text)
	while res:
        	print res.feature.decode('utf-8')
		res = res.next
