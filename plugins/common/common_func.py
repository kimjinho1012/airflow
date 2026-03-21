
    
def outer_func(target_func):
    def inner_func():
        print('target 함수 실행 전 입니다.')
        target_func()
        print('target 함수 실행 후 입니다.')
    
    return inner_func

@outer_func
def get_sftp():
    print('sftp 작업을 시작합니다.')

a = outer_func(get_sftp)
a()

get_sftp()

def regist(name, sex, *args):
    print(type(args))
    
    country = args[0] if len(args) >= 1 else None
    city = args[1] if len(args) >= 2 else None
    
def some_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    
    name = kwargs.get('name') or ''
    country = kwargs.get('country') or ''
    print(f'name: {name}')
    
def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    
    
def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    
    if email:
        print(email)
    if phone:
        print(phone)
    