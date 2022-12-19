def speak(text):
    def whisper(t):                      # объявляем вложенную функцию
        return t.lower() + '...'
    return whisper(text)                 # вызываем вложенную функцию и возвращаем ее результат


print(speak('Hello, World'))


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper

whisper = get_speak_func(0.3)
yell = get_speak_func(0.7)

print(whisper('Hello'))
print(yell('Hello'))


def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper

yell = get_speak_func('Hello, World', 0.7)

print(yell())