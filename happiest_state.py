import sys
import json
import re

def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    initial_state_sentiment = {}
    for line in open(sys.argv[2]):
        score = 0
        tweet_json = json.loads(line)
        if tweet_json.get('text') and tweet_json.get('place') and tweet_json['place']['country_code']=='US':
            city_state = tweet_json['place']['full_name'].encode('utf8').split(',')
            if city_state[1] != 'US':
                tweet_text = tweet_json['text'].encode('utf8').split()
                for word in tweet_text:
                    if re.match("^[A-Za-z0-9_-]*$", word):
                        score += scores.get(word, 0)
                initial_state_sentiment.setdefault(city_state[1], []).append(score)
    state_sentiment = {}
    for key, value in initial_state_sentiment.items():
        average = sum(value)/len(value)
        state_sentiment[key]= average
    print max(state_sentiment, key=state_sentiment.get)

if __name__ == '__main__':
  main()