# CulturelandPython
- A Python library for unofficial Cultureland. This Python library can login, and redeem gift cards into your account. **Be advised, this project is UNOFFICIAL you are responsible for everything that might occur due to using this python library.**
- 컬쳐랜드 문화상품권 충전하는 파이썬 라이브러리입니다. 이 라이브러리는 로그인 및 문화상품권 충전을 할 수 있습니다. **이 프로젝트는 비공식이기에 이 파이썬 라이브러리를 사용하며 생기는 모든 문제는 본인에게 책임이 있습니다.**

## Installation
### 1. PIP Installation
Simply use `pip install CulturelandPython`.
### 2. Chromium Installation
This project automatically detects your chrome version and downloads webdriver using [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager). Special thanks to the original repository owner.

## Usage
This Python library has 2 main features. Logging in and redeeming giftcards. You can achieve that goal by using Python expressions below.

### Logging in - Success
```
from CulturelandPython import client
>>> c = client.CulturelandClient('gooday2die', 'PASSWORD')
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
If you got questions on this project, or have a good idea to add into this project, let me know by POC edina00@naver.com. Also Since this project is NOT official project and it is kind of sketchy, this project might be removed from Github if Cultureland wants me to remove this project from Github. Any pull requests as well as issue reporting is welcomed. 
