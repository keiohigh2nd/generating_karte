# -*- coding: utf-8 -*-
import json_time_series_generate_patients
import json
import detection

def read_json():
	f = open('tmp/json_time_series_patient.json', 'r')
	jsonData = json.load(f,"utf-8")
	text = json.dumps(jsonData)
	f.close()
	return text, jsonData

def maker_json(base, t_base, sec_base, t_sec_base):
	marker = [{
    			"date": "2016-02-%s"%t_base,
    			"type": "1st Change",
    			"version": base
  		},
  		{
    			"date": "2016-02-%s"%t_sec_base,
    			"type": "2nd Change",
    			"version": sec_base
  		}]

	f = open("output/marker_wc_processed_data.json", "w")
        json.dump(marker, f, ensure_ascii=False)


def convert_to_json(MD, Tri, Chief):
	p_dict = {}
	marker_dict = {}
        i = 0
	base = 0
	sec_base = 0
	t_base = 0
	t_sec_base = 0

	for (m,t,c) in zip(MD,Tri,Chief):
		tmp_dict = {
    				"date": "2016-02-%s" % i,
    				"pct05": m,
    				"pct25": t,
    				"pct50": c,
    				"pct75": m-t,
    				"pct95": m-c
			}
		p_dict[i] = tmp_dict
		#maker's part
		if int(m-t) > base:
			base = m-t
			t_base = i
		elif int(m-t) > sec_base:
			sec_base = m-t
			t_sec_base = i		
		print t_base
		print t_sec_base
		i += 1
		maker_json(base, t_base, sec_base, t_sec_base)

	print p_dict.values()
	f = open("output/json_wc_processed_data.json", "w")
    	json.dump(p_dict.values(), f, ensure_ascii=False)
	return p_dict

if __name__ == "__main__":
	p_text, p_json  = read_json()
	tokens, text = detection.text_to_tokens(p_text)
	tmp = detection.word_count(tokens)

	MD_wc_list = []
	Triage_wc_list = []
	Chief_wc_list = []

	## Only one sample patient
	for t in xrange(len(p_json["0"])):
		MD_wc_list.append(detection.word_count(p_json["0"]["%s"%t]["MDcomments"]))
		Triage_wc_list.append(detection.word_count(p_json["0"]["%s"%t]["TriageAssessment"]))
		Chief_wc_list.append(detection.word_count(p_json["0"]["%s"%t]["ChiefComplaint"]))

	convert_to_json(MD_wc_list, Triage_wc_list, Chief_wc_list)
