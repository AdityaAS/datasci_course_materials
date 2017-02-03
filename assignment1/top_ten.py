import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    scores = {}
    hashtag = {}
    cnt = 0
    for line in tweet_file:
    	tweets = json.loads(line)
        sentiment = 0
    	keys = tweets.viewkeys()
    	if len(keys) != 1:
            words = tweets['entities']['hashtags']
            if len(words) > 0:
                for word in words:
                    t = word['text'] 
                    if len(t) > 0:
                        if t in hashtag.viewkeys():
                            hashtag[t] += 1
                        else:
                            hashtag[t] = 1

    sorted_x = sorted(hashtag.items(), key=operator.itemgetter(1))
    sorted_x.reverse()
    length = min(10, len(sorted_x))
    i = 0

    while (i < length):
        print sorted_x[i][0] + " " + str(sorted_x[i][1])
        i+=1

if __name__ == '__main__':
    main()

