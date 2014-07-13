import sys
import json
import re
sentimentData = sys.argv[1] #AFINN-111.txt
twitterData = sys.argv[2] #output.txt

def tweet_dict(twitterData):  
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict   
    
def sentiment_dict(sentimentData):
    afinnfile = open(sentimentData)
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = float(score)
    return scores 
    
def main():
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    accum_term = dict()
    for index in range(len(tweets)):
        if tweets[index].get("text"):
            tweet_word = tweets[index]["text"].encode('utf-8').split()
            sent_score = 0
            term_list = []            
            for word in tweet_word:          
                if re.match("^@|[@A-Za-z0-9_-]*$", word):
                    if word in sentiment.keys():
                        sent_score = sent_score + float(sentiment[word])
                    else:
                        term_list.append(word)
            for word in term_list:
                #if word not in accum_term.keys():
                if not accum_term.has_key(word):
                    accum_term[word] = []
                accum_term[word].append(sent_score)

    for key in accum_term.keys():
        term_value =sum(accum_term[key])/len(accum_term[key])        
        adjusted_score = "%.3f" %term_value
        print key,adjusted_score

if __name__ == '__main__':
    main()