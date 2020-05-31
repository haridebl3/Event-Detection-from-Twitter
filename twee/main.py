import json
import math
import re
from segment_genarator import segment_genarator


#program starts here

if __name__ == '__main__':
    
    clean_tweet_dir = 'data/05_hour.json'
    seg_file='data/seg_file'
    l=segment_genarator(clean_tweet_dir)
	
		