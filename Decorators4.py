def greet(name):
    return f'Hello {name}!'

def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

@bold
def greet(name):
    return f'Hello {name}!'

print(greet('Timur'))

def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

@bold
def greet1(name):
    return f'Hello {name}!'

@bold
def greet2():
    return 'Hello world!'

@bold
def greet3(name, surname):
    return f'Hello {name} {surname}!'

print(greet1('Timur'))
print(greet2())
print(greet3('Timur', 'Guev'))


