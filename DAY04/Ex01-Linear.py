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

# 삽입
    def insert_data(self, position, data) :
        linear = self.linear
        
        if position < 0 or position> len(linear): #유효성 검사
            print('데이터를 삽입할 범위를 벗어났습니다.')
            return
        
        linear.append(None) # 빈칸 추가
        linearSize = len(linear) # 리스트의 현재 크기
        
        # 삽입 위치 이후 요소들을 한칸씩 뒤로 이동
        for i in range(linearSize - 1, position, -1):
            linear[i] = linear[i -1]
            linear[i -1] = None
         
        linear[position] = data # 리스트에 데이터 삽입 

# 삭제
    def delete_data(self, postion): # 리스트에서 데이터 삭제
        linear = self.linear
        
        if postion <0 or postion > len(linear) : # 유효성 검사
            print('데이터를 삽입할 범위를 벗어났습니다.')

        linear[postion] = None # 해당위치 데이터 삭제
        linearSize = len(linear)
        
        # 삭제 이후 요소들 한칸씩 앞으로 이동
        for i in range(postion + 1, linearSize):
            linear[i - 1] = linear[i]
            linear[i] = None
            
        del(linear[linearSize - 1]) # 빈칸제거    

    
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

linear.insert_data(3, 99)

linear.delete_data(2)

linear.print_list(); # 리스트 출력
    