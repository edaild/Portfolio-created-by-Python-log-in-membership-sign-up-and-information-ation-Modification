# 회원가입
id = input('아이디를 생성해 주세요.')

while True:
    print('비밀번호 생성시 최소 6자 이상 입력하고 대소문자와 특수문자 사용을 해주세요.')
    pwd1 = input('비밀번호를 생성해 주세요')
    pwd2 = input('생성된 비밀번호를 확인해 주세요.')

    if pwd1 == pwd2:
        break
    
    if pwd1 != pwd2:
        print('생성하신 비밀보호와 다름니다.')
        
    
name = input('이름을 임력해 주세요.')
email = input('이메일을 입력해 주세요.')

print(f'{id}님 회원가입이 정상적으로 완료 되었습니다.')