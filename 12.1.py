import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
            continue
        if char == '>':
            inside_tag = False
            continue
        if not inside_tag:
            clean_text += char

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)
