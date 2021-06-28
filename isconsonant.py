def isconsonant(i : str)-> bool:

    return i not in 'aeiou'

def double_consonant(word : str)->str:
    word1 = word
    for i in word1:
        if isconsonant(i):
            new = word
            new = new.replace(i,i+"o"+i)
            
    return new
print(double_consonant('hoijj'))



        
