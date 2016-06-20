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


if __name__ == "__main__":
        #count, index = load_sample()

	p_text, p_json = read_json("output/one_json_time_series_patient.json")

        #Unidentified two spaces
        num_patients = len(p_json)

	m = MeCab.Tagger ("-Owakati")
	#m = MeCab.Tagger ("-Ochasen")
	text = p_json["0"]["0"]["A/P"]
	print parse_text(text, m)
