# 1. Single 중고물품종합사이트

  ### pre)작동하기 위해서
    네이버 아이디, 비밀번호가 있어야 하며 중고나라 사이트에 가입이 되어있어야 함
    chromedriver를 설치 및 경로지정 필요
    python3, BeautifulSoup4, Selenium 라이브러리 설치가 되어있어야 함

  ### project 핵심 부분
    - AWS 리눅스 환경에서 서버를 열어, 사용자에게 제공
    - 사용자에게 중고물품 종합 사이트를 제공

  ### 기능  
    - 사용자가 원하는 물품을 검색하여 중고나라, 당근마켓, G마켓 중고마켓을 종합하여 사용자에게 보여준다.
      원하는 물품을 검색하여 각 사이트별로 사진과 가격등을 출력하여 주고 url를 제공하여 
      사용자가 원하면 해당사이트로 연결시켜 준다.

  ### 크롤링을 위한 기법들
    (1) BeautifulSoup 라이브러리 사용
    - BeautifulSoup 모듈은 HTML 및 XML을 파싱하는 데 사용되는 파이썬 라이브러리
    (2) Selenium 이용한 크롤링
    - BeautifulSoup은 사용자 행동을 특정해서 데이터를 가져올 수 없어서, 사용자의 행동을 동적으로 추가하려면 selenium이 필요
    - 한마디로 브라우저에서의 액션을 테스트 할 수 있게 해주는 테스팅 도구

# 2. 사용법

 ### 사이트 주소 
    http://54.152.209.23:8000/
    
 ### 검색창에 원하는 물품을 사용자가 입력하여 검색을 한다.
![1](https://user-images.githubusercontent.com/47201943/70450955-ecc01400-1ae7-11ea-919a-05f5dd793bda.jpg)
 ### 검색결과
 ![2](https://user-images.githubusercontent.com/47201943/70450952-ecc01400-1ae7-11ea-9d10-95481651f060.jpg)
 ### 검색결과가 없을시, 출력결과
![3](https://user-images.githubusercontent.com/47201943/70450954-ecc01400-1ae7-11ea-95a4-d378d3c5261a.jpg)

# 3. 설치

### 셀리니움 설치
```python
sudo apt-get install python3-pip

pip3 install selenium

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

sudo apt install google-chrome-stable
#오류시 apt-get update 혹은 apt-get install --fix-broken && apt-get update && apt-get upgrade

#google-chrome --version
#크롬 버전 확인후 크롬 드라이버 다운로드

unzip chromedriver_linux64.zip

chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
  
### django 설치
```python
pip3 intsall djgango
(manage.py가 있는 프로젝트 설치 된 경로로 이동)
python3 manage.py runserver0.0.0.0:8000
```
    
### bs4 설치
```python
pip3 install bs4
```
       
# 4.주의할 점
    - 실시간으로 검색을 하여 검색이 느립니다.
