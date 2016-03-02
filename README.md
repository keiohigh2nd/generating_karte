# Generating_karte
This repository is for the purpose of research in medical records processing.

#Patient History View
1st step:
	Generate Patinets -> python src/json_time_series_generate_patients.py n
	n - number of patinets

2nd step:
	Generate Graphs -> python src/dump_to_graph.py 

#Generate Dataset for validating patient similarity
1st step:
	python make_dataset/generate_validation_data.py n
2nd step:
	python patient_similarity/calc_similarity.py

