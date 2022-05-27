# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(story):
    f = open('story.txt','r')
    file = f.read()
    f.close()
    return (file)

txt = read_file_content("story")
print (txt)


def count_words():
    text = read_file_content("./story.txt")
    word_count = dict ()
    tale = text.split()
    for word in tale:
        if word in word_count:
            word_count[word] += 1
        else:
           word_count[word] = 1

    return (word_count)
print (count_words())