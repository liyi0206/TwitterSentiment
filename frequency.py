import sys
import json
import re
from collections import Counter

def main():
    all_words = []
    for line in open(sys.argv[1]):
        tweet_json = json.loads(line)
        if tweet_json.get('text'):
            tweet_text = tweet_json['text'].encode('utf8').split()
            for word in tweet_text:
                if re.match("^@|[@A-Za-z0-9_-]*$", word):
                    all_words.append(word)
    words_hash = Counter(all_words)
    denominator = float(sum(words_hash.values()))
    frequency_dict = {}
    for (key, value) in words_hash.items():
        frequency_dict[key] = float(value/denominator)
    for (key, value) in frequency_dict.items():
        print key, value

if __name__ == '__main__':
    main()