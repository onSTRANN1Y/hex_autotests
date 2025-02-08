
def capitalize(text):
    if text == '':
      return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'ERROR{first_char}{rest_substring}'
