def greet(name):
    print('Hello, ' + name + '!')
    greet2(name)
    bye()


def greet2(name):
    print('getting ready to say bye..')


def bye():
    print('ok bye')


greet('name')
