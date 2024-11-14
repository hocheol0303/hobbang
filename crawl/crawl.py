import requests
from bs4 import BeautifulSoup

# 웹사이트 URL
url = 'https://paperswithcode.com/task/semantic-segmentation'  # 여기에 원하는 URL을 넣으세요.

# 페이지 요청
response = requests.get(url)
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 특정 클래스를 가진 태그 선택 (예: 클래스 이름이 'target-class'인 태그들)
target_class = 'dataset black-links'
elements = soup.find_all(class_=target_class)

# 결과 출력
i=0
with open('./names.txt', 'w') as f:

    for element in elements:
        f.write(element.get_text(strip=True)+', ')  # 텍스트만 가져오기 (공백 제거 옵션 포함)
        i+=1
print(i)