import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.

    cnt = 0
    for i in scores.items():
    	print i
    	cnt += 1

    print cnt

    tweet_file = open("output_Test.txt")
    tweets = {}
    cnt = 0
    score_keys = scores.viewkeys()
    for line in tweet_file:
    	tweets[cnt] = json.loads(line)
    	keys = tweets[cnt].viewkeys()
    	if len(keys) == 1:
    		sentiment = 0
    		print sentiment
    	else:
    		sentiment = 0
    		words = tweets[cnt]['text']
    		for word in words:
    			if isinstance(word, unicode):
    				word_encode = word.encode('utf-8')
    				if word_encode in score_keys:
    					sentiment += scores[word_encode]
    			else:
    				if word in score_keys:
    					sentiment += scores[word]
    			# sentiment += scores[word.decode('ascii')]
    		print sentiment
    		`
    print len(tweets.items())

if __name__ == '__main__':
    main()
