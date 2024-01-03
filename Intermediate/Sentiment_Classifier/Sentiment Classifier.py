"""
We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. 
We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. 
At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word

"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, 
and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive.
 The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, 
so you’ll need to convert all the words in the input string to lower case as well
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("./Intermediate/Sentiment_Classifier/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word
    
def get_pos(sentence):
    sentence = strip_punctuation(sentence)
    sentence = sentence.lower()
    print(sentence)
    words = sentence.split()
    print(words)
    positive_count = 0
    for word in words:
        if word in positive_words:
            positive_count += 1
    return positive_count 

"""
Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. 
Use the list, negative_words to determine what words will count as negative. 
The function should return a positive integer - how many occurrences there are of negative words in the text.
 Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well
"""   

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("./Intermediate/Sentiment_Classifier/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word

def get_neg(sentence):
    sentence = strip_punctuation(sentence)
    sentence = sentence.lower()
    words = sentence.split()
    negative_count = 0
    for word in words:
        if word in negative_words:
            negative_count += 1
    return negative_count 
       
"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). 
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv,
 which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
 Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. 
 The file should have those headers in that order. Remember that there is another component to this project. 
 You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. 
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("./Intermediate/Sentiment_Classifier/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word
negative_words = []
with open("./Intermediate/Sentiment_Classifier/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(sentence):
    sentence = strip_punctuation(sentence)
    sentence = sentence.lower()
    words = sentence.split()
    positive_count = 0
    for word in words:
        if word in positive_words:
            positive_count += 1
    return positive_count 

def get_neg(sentence):
    sentence = strip_punctuation(sentence)
    sentence = sentence.lower()
    words = sentence.split()
    negative_count = 0
    for word in words:
        if word in negative_words:
            negative_count += 1
    return negative_count 
    
with open("./Intermediate/Sentiment_Classifier/project_twitter_data.csv","r") as fhand:
    lines = fhand.readlines()
    data_lst = []
    for line in lines[1:]:
        line = line.strip()
        words = line.split(",")
        text = strip_punctuation(words[0])
        negative_score = get_neg(text) 
        positive_score = get_pos(text)
        number_of_replies = words[-1]
        number_of_retweets = words[-2]
        net_score = positive_score - negative_score
        data_lst.append([number_of_retweets,number_of_replies,positive_score,negative_score,net_score])
       
        
with open("./Intermediate/Sentiment_Classifier/resulting_data.csv","w") as fhand:
    fhand.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
    for line in data_lst:
        	fhand.write("{},{},{},{},{} \n".format(line[0],line[1],line[2],line[3],line[4]))
    