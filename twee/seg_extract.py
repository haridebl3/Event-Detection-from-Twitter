from collections import OrderedDict
import json
from math import exp, sqrt, log10



class seg_extract():

	def __init__(self,seg_file,c_dir):
		segm=[]
		f=open(c_dir,'r')
		c=0
		for i in f:
			c+=1
		tweet_count=c
		k=int(sqrt(tweet_count))
		f=open(seg_file,'r')
		for i in f:
			js=eval(i)
			for l,j in js.items():
				'''
					j=[]
				'''
				seg_mean = tweet_count *j[2]
				seg_std_dev = sqrt(tweet_count * j[2] * (1 - j[2]))
				score=self.sigmoid(10 * (j[2] - seg_mean - seg_std_dev)/(seg_std_dev)) * log10(1+j[3])
				score*= log10(1+j[1])
				score*= log10(1 + log10(1 +j[0]))
				segm.append((l,score))
			print('Total Segments:',len(segm))
			print('Bursty Segments:',k)
			bursty_segment_weights = OrderedDict()
			segment_newsworthiness = {}
			for seg,b_score in sorted(segm, key = lambda x : x[1], reverse=True)[:k]:
				bursty_segment_weights[seg] = b_score
				segment_newsworthiness[seg]=b_score
			with open('data/weight_','w') as f:
				json.dump(dict(bursty_segment_weights.items()), f)

		


			
	def sigmoid(self, x):
		try:
			return 1/(1+exp(-x))
		except:
			print('SIGMOID ERROR:', x)
			return 0
