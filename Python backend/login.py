# 로근인

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

if id == input_id :
    if input_pwd == input_pwd:
        print(f'{id} 님 방문을 환영합니다.')