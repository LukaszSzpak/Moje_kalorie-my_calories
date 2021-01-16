from google_trans_new import google_translator as Translator


def translate_polish_to_english(polish_sentence):
    return __my_translate(sentence=polish_sentence,
                          source_lang='pl',
                          dest_lang='en')


def translate_english_to_polish(english_sentence):
    return __my_translate(sentence=english_sentence,
                          source_lang='en',
                          dest_lang='pl')


def __my_translate(sentence, source_lang, dest_lang):
    translator = Translator()
    return translator.translate(text=sentence, lang_src=source_lang, lang_tgt=dest_lang)[:-1]
