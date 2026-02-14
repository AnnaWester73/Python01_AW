
def count_words(sentence):
    if not sentence:
        return 0

    words = sentence.strip().split(" ")
    words = [word for word in words if word != ""]

    return len(words)
