import sys
import json
from collections import Counter

def main():
    hashtags = []
    for line in open(sys.argv[1]):
        tweet_json = json.loads(line)
        if "entities" in tweet_json.keys() and "hashtags" in tweet_json["entities"]:
            if tweet_json['entities']['hashtags']!= []:
                for hashtag in tweet_json["entities"]["hashtags"]:
                    unicode_hashtag = hashtag["text"].encode('utf-8')
                    hashtags.append(unicode_hashtag)
    top_ten = Counter(hashtags).most_common(10)
    for key, value in top_ten:
        print key, float(value)

if __name__ == '__main__':
  main()