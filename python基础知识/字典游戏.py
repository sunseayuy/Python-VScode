message = input('>')
words = message.split(' ')
print(words)
emojis = {
    ":)":"(✪ω✪)",
    ":(":"(•́へ•́╬)"
}
output = ''
for word in words:
     output += emojis.get(word,word)+" "
print(output)