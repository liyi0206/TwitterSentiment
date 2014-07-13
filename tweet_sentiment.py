import sys
import json

sentimentData = sys.argv[1] #AFIN-111.txt
twitterData = sys.argv[2] #output.txt

def tweet_dict(twitterData): 
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
        #twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict
    #return data_read["text"]
    
def sentiment_dict(sentimentData):
    afinnfile = open(sentimentData)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.

    return scores # Print every (term, score) pair in the dictionary
    
def main():
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    for index in range(len(tweets)):
        tweet_word = tweets[index]["text"].split()
        sent_score = 0
        for word in tweet_word:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "").encode('utf-8', 'ignore')
            
            if not (word == ""):
                if word.encode('utf-8') in sentiment.keys():
                    sent_score = sent_score + float(sentiment[word])
        print float(sent_score)
  
if __name__ == '__main__':
    main()