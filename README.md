# CulturelandPython
컬쳐랜드에 로그인하고 문화상품권을 충전하는 파이썬 라이브러리입니다. 

A Python library that logs in to Cultureland website and redeem giftcode.
## Disclaimer - 사전고지
### KR
- 해당 프로그램을 사용하며 생기는 모든 문제의 책임은 사용자 본인에게 있습니다.
- 해당 프로그램은 교육 목적으로 제작된 프로그램입니다. 
- 해당 프로그램은 영리를 추구하지 않습니다.
- **만일 컬쳐랜드 직원분들이 레포지토리를 제거하라는 요청이 오면 내리도록 하겠습니다.**
### EN
- The user takes all responsibility for any outcomes by using this library.
- This library is for educational purpose only.
- This library is non-profit
- **If cultureland official requests to take this repository down, I will do so.**

## Installation - 설치
### KR
### 1. PIP Installation
`pip install CulturelandPython` 로 간단하게 설치가 가능합니다. 이 라이브러리는 다음의 라이브러리에 의존합니다. 라이브러리들은 자동으로 설치됩니다.
- selenium
- webdriver-manager
- anticaptchaofficial
- PILLOW

### 2. AntiCaptcha 로그인 후 API Key 생성
컬쳐랜드 로그인 페이지에 생긴 Captcha (Captcha.org에서 생성된 것으로 추정)을 해결하기 위해서 이 라이브러리는 [AntiCaptcha](https://anti-captcha.com/)에서 제공한 API를 사용합니다. 

1. 컬쳐랜드에서 사용하는 Captcha는 Image Captchas로 AntiCaptcha에서 1000개당 0.5$에 풀 수 있습니다. (최소 충전금액은 5달러). 해당 AntiCaptcha 웹사이트에 돈을 충전합니다.
2. https://anti-captcha.com/clients/settings/apisetup 여기 방문하면 API Key를 받을 수 있습니다. 이걸 어디에 잘 적어놔주세요.

### EN
### 1. PIP Installation
Install CulturelandPython by `pip install CulturelandPython`. This library has dependencies of following libraries:
- selenium
- webdriver-manager
- anticaptchaofficial
- PILLOW

These libraries get installed automatically.

### 2. Setting up Anti-Captcha.com
1. Cultureland uses Captchas from Captcha.org which is solvable by [AntiCaptcha](https://anti-captcha.com/). They offer 1000 Image Captchas in 0.5$. So add balance to Anti-Captcha.com.
2. After you are done with setting up API, visit https://anti-captcha.com/clients/settings/apisetup for API Key.  Do not lose it. This is important.

### Disclaimer - 알림
#### KR
- Anti-Captcha.com 사이트와 저와 관계는 아무것도 없습니다.
- 그냥 파이썬 라이브러리 제공을 해줘서 쓴겁니다.
- 이후 자체적으로 Captcha를 푸는 무료 API를 제공할 예정입니다. ([여기](https://github.com/gooday2die/Anti-Captcha-Sound) 참고)

#### EN
- Anti-Captcha.com has nothing to do with me. I do not have referal program going on. Just using it since they offer easy Python library
- Later on, there will be an free API that solves Captcha that will be made by me as well. Check this [repo](https://github.com/gooday2die/Anti-Captcha-Sound) as well.

## Usage - 사용법
### KR
이 파이썬 라이브러리는 크게 두개의 기능을 가지고 있습니다. 
- 로그인
- 문화상품권 충전

두개의 기능은 다음의 Python 표현을 사용하면 됩니다.

### 로그인 - 성공
```
from CulturelandPython import client
>>> c = client.CulturelandClient('gooday2die', 'PASSWORD', api_key="AntiCaptcha API 키")
>>> c
Cultureland Client Object, Logged in as gooday2die
```
`Culureland.client`를 사용하시면 컬쳐랜드에 로그인 되는 object를 생성할 수 있습니다. 단 이는 Anti Captcha 서버와 통신하고 Captcha를 해결하는데 시간이 조금 걸리기 때문에, `asyncio` 또는 `threading`을 사용해서 호출하는것을 추천합니다.
### 로그인 - 실패
```
>>> c = client.CulturelandClient("gooday2die", "WRONG_PASSWD")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/client.py", line 21, in __init__
    self.login()
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/client.py", line 38, in login
    login.login(self.web_driver, self.username, self.passwd)
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/login.py", line 23, in login
    raise LoginFailureException
CulturelandPython.login.LoginFailureException
```
옳지 않은 로그인을 할 시 `Exception` 으로 `CulturelandPython.login.LoginFailureException` 가 raise 됩니다.


### EN
This Python library has 2 main features. Logging in and redeeming giftcards. You can achieve that goal by using Python expressions below.

### Logging in - Success
```
from CulturelandPython import client
>>> c = client.CulturelandClient('gooday2die', 'PASSWORD', api_key="YOUR API KEY FROM ANTI CAPTCHA")
>>> c
Cultureland Client Object, Logged in as gooday2die
```
Using `CulturelandClient` class from `client` will generate an client object that is connected to the Cultureland System. If the login was successful, there will be **no return value**. If you are willing to use this class in a big project or fast runtime demanding project, I would suggest you using `asyncio` or `threading` when using this class.

### Logging in - Failure
```
>>> c = client.CulturelandClient("gooday2die", "WRONG_PASSWD")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/client.py", line 21, in __init__
    self.login()
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/client.py", line 38, in login
    login.login(self.web_driver, self.username, self.passwd)
  File "/home/gooday2die/.local/lib/python3.8/site-packages/CulturelandPython/login.py", line 23, in login
    raise LoginFailureException
CulturelandPython.login.LoginFailureException
```
When logging into the system with incorrect credentials, there will be `Exception` thrown as `CulturelandPython.login.LoginFailureException`.

###  Redeeming 
```
>>> c
Cultureland Client Object, Logged in as gooday2die
>>> c.redeem('4180-0252-0565-2549')
[True, 1000]
>>> c.redeem('4180-0252-0565-2549')
[False, '잔액이 0원인 상품권']
```
You can redeem by using `redeem` method of `CulturelandClient` object. The method returns `list` type object. 
- If the Redeeming process was successful, it returns [True, Amount Redeemed]
- If the Redeeming process was unsuccessful, it returns [False, Error Reason]

## Contacts & ETC
### KR
이 프로젝트에 좋은 아이디어가 있거나 추가하고 싶은 기능이 있다면 edina00@naver.com 으로 연락을 주세요. 또 이 프로젝트는 공식 프로젝트가 아니며 비공식 프로젝트이기 때문에 컬쳐랜드에서 프로그램을 내려달라고 로그인 하면 내릴 예정입니다. PR과 Issue는 환영입니다.

### EN
If you got questions on this project, or have a good idea to add into this project, let me know by POC edina00@naver.com. Also Since this project is NOT official project and it is kind of sketchy, this project might be removed from Github if Cultureland wants me to remove this project from Github. Any pull requests as well as issue reporting is welcomed. 
