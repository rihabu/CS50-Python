import emoji
#prompt the user for a str in English
text= input("Input: ")

#output the “emojized” version of that str convert any codes (or aliases) therein to their corresponding emoji
print(f"Output: {emoji.emojize(text)}")