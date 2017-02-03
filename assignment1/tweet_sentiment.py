import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    return str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # print str("Sentiment file lines = ") + lines(sent_file)
    # print str("Tweet file lines = ") + lines(tweet_file)
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.

    tweet_file = open(sys.argv[2])
    cnt = 0
    score_keys = scores.viewkeys()
    for line in tweet_file:
    	tweets = json.loads(line)
        sentiment = 0
        # print tweets['text']
    	keys = tweets.viewkeys()
    	if len(keys) == 1:
    		sentiment = 0
    		print sentiment
    	else:
            # print tweets
            words = tweets['text'].split(' ')
            for word in words:
                # print word
                if isinstance(word, unicode):
                    word_encode = word.encode('utf-8')
                    if word_encode in score_keys:
                        sentiment += scores[word_encode]
                    else:
                        if word in score_keys:
                            sentiment += scores[word]

            print sentiment

if __name__ == '__main__':
    main()

