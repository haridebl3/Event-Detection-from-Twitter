import os
import json
from segmenter import segmenter
from seg_extract import seg_extract

class segment_genarator:

	def __init__(self,clean_tweet_dir):
		total_segs=0
		seg_freq={}
		seg_cou={}

		
		seg_prob_file='data/seg_file'
		tw_seg = segmenter(wiki_titles_file='data/enwiki-titles-unstemmed.txt', hashtag_wt=1, entities_only=False)
		f=open(clean_tweet_dir,'r')
		for line in f:

		    line = line.replace('\n','')
		    if line=='':
		    	break
		    json_tweet=json.loads(line)
		    jb=eval(line)
		    segmentation=tw_seg.tweet_segmentation(json_tweet)
		    total_segs+=len(segmentation)
		    for seg in segmentation:
		        seg_freq[seg] = seg_freq.get(seg,0) + 1
		        seg_cou[seg]=[jb['user']['followers_count'],jb['retweet_count']]




		print('Done')



		print('Total Segments:',total_segs)
		print('Total Unique Segments:',len(seg_freq))

		

		for k,v in seg_freq.items():
			seg_cou[k].append(v/total_segs)
			seg_cou[k].append(v)

		

		with open(seg_prob_file,'w') as f:
		    json.dump(dict(sorted(seg_cou.items())), f)


		seg_extract(seg_prob_file,clean_tweet_dir)