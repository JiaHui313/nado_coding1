#서비스 요금과 부가세 계산하는 프로그램

def service_price():
    service = input('서비스 종류를 입력하세요, a/b/c: ')
    valueAdded = input('부가가치세를 포함합니까? y/n: ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1    
    if valueAdded == 'n':
        if service == 'a':
            result = 23
        if service == 'b':
            result = 40 
        if service == 'c':
            result = 67
    print(round(result, 1), '만원입니다.')

service_price()
