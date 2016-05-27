import json, random
import detection
import collections
import numpy as np

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData

def get_index(word, index):
        i = 0
	for w in index:
          if w == word:
            return i
          i += 1

def dictionarize_text(arr):
	#Need preprocessing of texts
        cl = collections.Counter(arr)
	from sklearn.feature_extraction import DictVectorizer
	v = DictVectorizer()
	count = v.fit_transform(cl)
        index = v.get_feature_names() 
        return count, index

def get_cov(text, index):
	s_matrix = np.zeros((len(index), len(index)))
	for i_tex in xrange(len(text)):
          i = get_index(text[i_tex], index)
          if i_tex > 0:
              m1 = get_index(text[i_tex-1], index)
              s_matrix[i][m1] += 1
          if i_tex < len(text)-1:
              m2 = get_index(text[i_tex+1], index)
              s_matrix[i][m2] += 1
        return s_matrix
	

def load_sample():
        c = ['a', 'b', 'a', 'd', 'a'] 
        count, index = dictionarize_text(c)
	sm = get_cov(c, index)
        print c
        print sm
        return count, index

if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/small/small_json_time_series_patient.json")

        #Unidentified two spaces
        texts = p_json["0"]["3"]["Plan"].split("  ")
	count_m, index = dictionarize_text(texts)

	sm = get_cov(texts, index)
	print sm

