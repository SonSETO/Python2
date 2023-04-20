'''
파일명 Ex01-Linear.py

선형 리스트(LinearList)
   간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것이다.
'''
class LinearList():
    def __init__(self):
     self.linear = [] # 빈 리스트 생성
        
    def add_data(self, data): # 리스트에 데이터 추가
        linear = self.linear
        linear.append(None) # 빈칸 추가
        lLen = len(linear) # 리스트의 현재 크기   
        linear[lLen - 1] = data # 리스트에 데이터 삽입


    def print_list(self):
        linear = self.linear
        for list in linear:
            print(list)    
    
# 실행코드
linear = LinearList()
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)



#linear.insert_data(3, 99)

linear.print_list(); # 리스트 출력
    