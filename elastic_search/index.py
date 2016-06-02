import sys, json, yaml
from elasticsearch import Elasticsearch

def read_json(filename):
        f = open(filename, 'r')
        jsonData = json.load(f,"utf-8")
        text = json.dumps(jsonData)
        f.close()
        return text, jsonData


if __name__ == "__main__":
        #count, index = load_sample()

        p_text, p_json = read_json("output/one_json_time_series_patient.json")


	es = Elasticsearch()
	index = "oa"
	doc_type = "Patient"
	i = 1

	setting = yaml.load(open('elastic_search/mapping.yaml'))
	properties = setting["mappings"]["Patient"]["properties"].keys()
	print es.create(index=index, doc_type=doc_type, body=setting)

	for p in xrange(len(p_json)):
    		es.index(index=index, doc_type=doc_type, id=i, body=p_json["%s"%p]["0"]["Plan"].split(" "))
    		i += 1
