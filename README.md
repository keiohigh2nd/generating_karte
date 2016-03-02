# Generating_karte
This repository is for the purpose of research in medical records processing.

#Patient History View
1st step:
	Generate Patinets -> python src/json_time_series_generate_patients.py n
	n - number of patinets

2nd step:
	Generate Graphs -> python src/dump_to_graph.py 

#Generate Dataset for validating patient similarity
1st step:Generating validation dataset
	python make_dataset/generate_validation_data.py n
	n - number of patients

2nd step:Vectorize the dataset
	python patient_similarity/make_dictionary.py
	-> output is dic_out
 
3rd step:Validating dataset
	python patient_similarity/main.py

