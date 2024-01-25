def outer_func():
    print('call outer func')

    def inner_func():
        return 'call inner func'
    
    print(inner_func)

outer_func()

def html_creator(tag):
    def text_wrapper(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))    
    return text_wrapper

h1_html_creator = html_creator('h1')
h1_html_creator('H1 태그는 타이틀을 표시하는 태그입니다.')
print(h1_html_creator)

def calc_power(n):
    def power(digit):
        return digit ** n
    return power
    
power2 = calc_power(2)
power3 = calc_power(3)
power4 = calc_power(4)
# print(power2(2))
# print(power3(2))
# print(power4(2))

list_data = list()
for num in range(1, 6):
    list_data.append(calc_power(num))

for func in list_data:
    print(func(2))

import datetime

def datetime_decorator(func):
    def wrapper():
        print('time ' + str(datetime.datetime.now()))
        func()
        print(datetime.datetime.now())
    return wrapper

@datetime_decorator
def logger_login_david():
    print('David login')

logger_login_david()


def type_checker(function):
    def inner_func(digit1, digit2):
        if (type(digit1) != int or type(digit2 != int)):
            print('only integer support')
            return
        return function(digit1, digit2)
    return inner_func

@type_checker
def multiplexer(digit1, digit2):
    return digit1 * digit2

multiplexer(1, 2)

def mark_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, **kwargs) +'</b>'
    return wrapper

def mark_italic(function):
    def wrapper(*args, **kwargs):
        return '<i>' + function(*args, **kwargs) +'</i>'
    return wrapper

@mark_bold
@mark_italic
def add_html(string):
    return string

print(add_html('안녕하세요....'))

def decorator1(num):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            print('decorator1 {0}'.format(num))
        return inner_wrapper
    return outer_wrapper

def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' +function(*args, **kwargs)+'</'+tag+'>'
        return inner_wrapper
    return outer_wrapper

@mark_html(tag='b')
def print_hello():
    print('hello')