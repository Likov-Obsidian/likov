def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper

@make_bold
def say_hello():
    return "Привет, мир!"

@make_bold
def get_message():
    return "Это важное сообщение!"

print("базовый декоратор")
print(say_hello())
print(get_message())

def simple_text():
    return "Простой текст"

bold_text = make_bold(simple_text)
print("\nБез использования @:")
print(bold_text())