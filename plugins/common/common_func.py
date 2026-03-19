
    
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