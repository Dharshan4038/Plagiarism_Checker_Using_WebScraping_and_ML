import re

def clean_text(txt):
    text = txt.lower()
    # Remove punctuation
    pattern = r'[^\w]+'
    words = re.sub(pattern, ' ', text)
    # Remove extra whitespace
    words = re.sub(r'\s+', ' ', words)
    # Remove numbers
    words = re.sub(r'\d+', '', words) 
    return words

def stopwordremove(text):
    # text1 = text.lower()
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in text if not w in stop_words]
    return filtered_sentence


def tokenize_text(text):
    from nltk.tokenize import word_tokenize
    return word_tokenize(text)

def keywordextract(text):
    import spacy
    from collections import Counter
    from string import punctuation
    nlp = spacy.load("en_core_web_sm")
    def get_hotwords(text):
        result = []
        pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
        doc = nlp(text.lower()) 
        for token in doc:
            if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
                continue
            if(token.pos_ in pos_tag):
                result.append(token.text)
        return result

    output = set(get_hotwords(text))
    most_common_list = Counter(output).most_common(15)
    return most_common_list
        
def monkeyword(text):
    from monkeylearn import MonkeyLearn

    ml = MonkeyLearn('322ad90b7d7fe912f8da3904c0da25e53561d861')
    model_id = 'ex_YCya9nrn'
    data =[text]
    result = ml.extractors.extract(model_id, data)

    # extract only the keyword and the relevance from the extractions list
    keywords = [(kw['parsed_value'], kw['score']) for kw in result.body[0]['extractions']]

    dict ={}
    # print the extracted keywords and relevance
    for keyword, relevance in keywords:
        print(f"{keyword}: {relevance}")
        dict[keyword]=relevance
    return dict
 