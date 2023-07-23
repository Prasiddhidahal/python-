#girraff language
''''comment for multiple line
'''
def translate(phrase):
    traslations= ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            traslations = traslations + "g"
        
        else:
            traslations = traslations+ letter
        
    return traslations
print(translate(input("enter a phrase")))



