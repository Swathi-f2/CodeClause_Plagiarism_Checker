import string
from collections import Counter
import math

# Function to calculate cosine similarity between two texts
def cosine_similarity(text1, text2):
    # Remove punctuation and convert to lowercase
    text1 = text1.translate(str.maketrans('', '', string.punctuation)).lower()
    text2 = text2.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split texts into words and count word occurrences
    word_counts1 = Counter(text1.split())
    word_counts2 = Counter(text2.split())

    # Create a set of all unique words in both texts
    words = set(word_counts1.keys()).union(set(word_counts2.keys()))

    # Calculate dot product and magnitudes of each text's word vector
    dot_product = sum(word_counts1.get(word, 0) * word_counts2.get(word, 0) for word in words)
    mag1 = math.sqrt(sum(word_counts1.get(word, 0) ** 2 for word in words))
    mag2 = math.sqrt(sum(word_counts2.get(word, 0) ** 2 for word in words))

    # Calculate cosine similarity
    if mag1 == 0 or mag2 == 0:
        return 0
    else:
        return dot_product / (mag1 * mag2)

# Sample usage
text1 = "The quick brown fox jumps over the lazy dog"
text2 = "A quick brown dog jumps on the log"
similarity = cosine_similarity(text1, text2)
print(f"Cosine similarity: {similarity:.2f}")
