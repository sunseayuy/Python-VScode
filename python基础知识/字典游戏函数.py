def translate(message):
    words = message.split(' ')
    print(words)
    emojis = {
        ":)":"(✪ω✪)",
        ":(":"(•́へ•́╬)"
    }
    output = ''
    for word in words:
         output += emojis.get(word,word)+" "
    return output


message = input('>')
print(translate(message))