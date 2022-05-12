from random import randrange

def get_jokes(n):
    jokes = []
    for _ in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))],
                         adjectives[randrange(len(adjectives))]])
        jokes.append(joke)
    print(jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(5)

