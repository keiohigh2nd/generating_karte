# -*- coding: utf-8 -*-

import random, codecs
def make_object():
	texts = "身長は%s"%(str(random.randint(150,175)))
	f = codecs.open("sample_karte/es_sample_Object.txt","w","utf-8")
	f.write(texts)
	f.close()

if __name__ == "__main__":
	make_object()

	
