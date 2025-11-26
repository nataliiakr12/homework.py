def first_word(text):
    text = text.strip ('.,\'')
    for ch in text:
        if not (ch.isalpha() or ch == '\''):
            text = text.replace(ch, ' ')
    return text.split()[0]

assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"

print('OK')