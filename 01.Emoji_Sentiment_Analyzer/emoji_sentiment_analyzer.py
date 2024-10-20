import re
import json

# Load emoji sentiment dictionary
with open(r'C:\Users\Alagammai\Alagu\Projects\Github\Python\Python\Emoji_Sentiment_Analyzer\emoji_sentiment_dict.json', 'r', encoding='utf-8') as file:
    emoji_sentiments = json.load(file)


def extract_emojis(text):
    emoji_pattern = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F]", flags=re.UNICODE)
    return emoji_pattern.findall(text)

def analyze_sentiment(emojis):
    positive, negative, neutral = 0, 0, 0
    sentiment_score = 0
    
    for emoji in emojis:
        sentiment = emoji_sentiments.get(emoji, 'neutral')
        if sentiment == 'positive':
            positive += 1
            sentiment_score += 1
        elif sentiment == 'negative':
            negative += 1
            sentiment_score -= 1
        else:
            neutral += 1
    
    return sentiment_score, positive, negative, neutral

def sentiment_summary(text):
    emojis = extract_emojis(text)
    if not emojis:
        return "No emojis detected."
    
    sentiment_score, positive, negative, neutral = analyze_sentiment(emojis)
    
    result = (f"Sentiment Score: {sentiment_score}\n"
              f"Positive Emojis: {positive}\n"
              f"Negative Emojis: {negative}\n"
              f"Neutral Emojis: {neutral}")
    return result

if __name__ == "__main__":
    user_text = input("Enter text with emojis: ")
    summary = sentiment_summary(user_text)
    print(summary)
