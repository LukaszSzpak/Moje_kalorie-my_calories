def upper_first_letter(sentence):
    return sentence[0].upper()+sentence[1:]


def get_number_from_wolfram_response(text):
    text_number = text.split()[1]
    return float(text_number)
