def null_decorator(func):
    return func

def say():
    print('Привет Мир!')

say = null_decorator(say)      # декорируем функцию

say()

def sample_decorator(func):          # определяем декоратор
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

def say():
    print('Привет Мир!')

say = sample_decorator(say)          # декорируем функцию

say()                                # вызываем декорированную функцию

