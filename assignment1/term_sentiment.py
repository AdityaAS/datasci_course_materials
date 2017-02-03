import sys
import json
def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def main():
	tweet_file = open(sys.argv[2])
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	unindexed_sum = {}
	unindexed_cnt = {}
	for line in afinnfile:
		term, score  = line.split("\t")
		scores[term] = int(score)
	cnt = 0
	score_keys = scores.viewkeys()
	for line in tweet_file:
		tweets = json.loads(line)
		sentiment = 0
		keys = tweets.viewkeys()
		if len(keys) == 1:
			sentiment = 0
		else:
			words = tweets['text'].split(' ')
			temp = []
			for word in words:
				if word in score_keys:
					sentiment += scores[word]
				else:
					temp.append(word)

			for t in temp:
				if t in unindexed_sum.viewkeys():
					unindexed_sum[t] += sentiment
					unindexed_cnt[t] += 1
				else:
					unindexed_cnt[t] = 1
					unindexed_sum[t] = sentiment

	unindexed_keys = unindexed_sum.viewkeys()

	for key in unindexed_keys:
		score = unindexed_sum[key] / unindexed_cnt[key]
		print key + " " + str(int(score))

if __name__ == '__main__':
    main()
