import random


if __name__ == "__main__":
    f = open("91K nouns.txt", "r")
    g = open("31K verbs.txt", "r")
    h = open("28K adjectives.txt", "r")
    i = open("6K adverbs.txt", "r")
    #get files with slang words

    a=[]
    b=[]
    c=[]
    d=[]
    '''need to add an array for articles and conjugates
    and things like that'''

    for y in f:
        a.append(y)
    f.close()

    for y in g:
        b.append(y)
    g.close()

    for y in h:
        c.append(y)
    h.close()
    
    for y in i:
        d.append(y)
    i.close()

    
    for x in range(0, 2):
        print random.randrange(0, len(a))

    
    finalString = ""
    for x in range(0, 12):
        
        u = random.randrange(0, 5) #0-5 since only 4 cases the period case has more probability
        if u == 0:
            j = random.randrange(0, len(a))
            z = a[j].rstrip()
            finalString = finalString + " " + z
        elif u == 1:
            q = random.randrange(0, len(b))
            z = b[q].rstrip()
            finalString = finalString + " " + z
        elif u == 2:
            j = random.randrange(0, len(c))
            z = c[j].rstrip()
            finalString = finalString + " " + z
        elif u == 3:
            q = random.randrange(0, len(d))
            z = d[q].rstrip()
            finalString = finalString + " " + z
        else:
            finalString = finalString + ". "

    print finalString

        
    
    
