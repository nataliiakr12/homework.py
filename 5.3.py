import string
def make_hashtag(text):
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words = text.title().split()
    hashtag = "#" + "".join(words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    print(hashtag)

make_hashtag ('Python Community')
make_hashtag ('i like python community!')
make_hashtag ('Should, I. subscribe? Yes!')
make_hashtag('python learning hashtag test very very long string to check the hashtag cutting after one hundred and forty characters with many repeating words python python python community community community learning learning learning')