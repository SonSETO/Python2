'''
 파일명 :Ex03-appendHello.py
 
open 함수모드
     a(append mode) : 추가모드
'''
file = open('hello.txt', 'at', encoding='UTF-8')
file.write('Hello\n')
file.write('Nice to meey you\n')
print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')
file.close()   