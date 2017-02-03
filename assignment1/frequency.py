import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	tweet_file = open(sys.argv[1])
	term_count = {}
	cnt = 0
	for line in tweet_file:
		tweets = json.loads(line)
		terms = term_count.viewkeys()
		keys = tweets.viewkeys()
		text = 'text'
		if text in keys:
			words = tweets['text'].split(' ')
			for word in words:
				cnt += 1
				if word in term_count.viewkeys():
					term_count[word] += 1
				else:
					term_count[word] = 1


	for term in term_count.viewkeys():
		freq = term_count[term]/(1.0*cnt)
		if not (not freq):
			newterm = term.replace("\n","")
			# print len(newterm)
			print str(newterm) + " " + str(freq)


if __name__ == '__main__':
    main()