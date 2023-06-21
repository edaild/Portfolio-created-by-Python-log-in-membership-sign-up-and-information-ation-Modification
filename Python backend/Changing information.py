# 정보수정

print('정보수정은 로그인이 필요합니다.')

#추후 DB 생성후 추가 예정

id = 'id123'
pwd = 'pwd123'

while True:
    input_id = input('id : ')
    input_pwd = input('pwd : ')
    
    if id == input_id and pwd == input_pwd:
        break
               
    if id != input_id :
        print('잘못된 ID 입니다.')
    if pwd != input_pwd :
        print('잘못된 비밀번호 입니다.')

print('확인되었습니다. 지금부터 정보수정을 해주시기 바람니다.')        
        
idb = input('아이디를 생성해 주세요.')

while True:
    print('비밀번호 생성시 최소 6자 이상 입력하고 대소문자와 특수문자 사용을 해주세요.')
    pwdb1 = input('비밀번호를 생성해 주세요')
    pwdb2 = input('생성된 비밀번호를 확인해 주세요.')

    if pwdb1 == pwdb2:
        break
    
    if pwdb1 != pwdb2:
        print('생성하신 비밀보호와 다름니다.')
        
    
name = input('이름을 임력해 주세요.')
email = input('이메일을 입력해 주세요.')

print(f'{idb}님 정보수정이 정상적으로 완료 되었습니다.')