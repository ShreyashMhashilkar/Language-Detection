from langdetect import detect

def language_detection():
    text = input("Enter any text in any language: ")
    language = detect(text)
    return language

if __name__=="__main__":
    result = language_detection()
    print(result)

