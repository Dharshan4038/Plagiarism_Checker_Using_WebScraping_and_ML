import math
# import retrieve
def cosine_similarity(text1, text2):
    # tokenizing the texts
    tokens1 = text1.split()
    tokens2 = text2.split()
    
    # creating a set of unique words from both the texts
    unique_words = set(tokens1 + tokens2)
    
    # calculating frequency of words in each text
    freq1 = {word: tokens1.count(word) for word in unique_words}
    freq2 = {word: tokens2.count(word) for word in unique_words}
    
    # calculating dot product of the frequencies
    dot_product = sum(freq1[word] * freq2[word] for word in unique_words)
    
    # calculating the magnitude of frequency vectors
    magnitude1 = math.sqrt(sum(freq1[word]**2 for word in unique_words))
    magnitude2 = math.sqrt(sum(freq2[word]**2 for word in unique_words))
    
    # calculating cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)
