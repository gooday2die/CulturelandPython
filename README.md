# CulturelandPython
- A Python library for unofficial Cultureland. This Python library can login, and redeem gift cards into your account. **Be advised, this project is UNOFFICIAL you are responsible for everything that might occur due to using this python library.**
- 컬쳐랜드 문화상품권 충전하는 파이썬 라이브러리입니다. 이 라이브러리는 로그인 및 문화상품권 충전을 할 수 있습니다. **이 프로젝트는 비공식이기에 이 파이썬 라이브러리를 사용하며 생기는 모든 문제는 본인에게 책임이 있습니다.**

## Installation
### 1. PIP Installation
Simply use `pip install CulturelandPython`.
### 2. Chromium Installation
Since this project is using chromium and selenium for its webdrivers, you have to download each web drivers. 
- Check your Chrome version. If you do not have one, get one.
- Download Chromium driver from https://chromedriver.chromium.org/downloads
- **Download Chromium driver that matches your Chrome Version**
- **Any difference in between Chromium driver and Chrome version will result in unexpected exceptions and errors**
- Save `chromedriver` or `chromedriver.exe` into a directory you can remember.

## Usage
This Python library has 2 main features. Logging in and redeeming giftcards. You can achieve that goal by using Python expressions below.

```
from CulturelandPython import client
>>> c = client.CulturelandClient('gooday2die', 'PASSWORD', './chromedriver')
[SUCCESS] User gooday2die Logged in Successfully.
```
Import CulturelandPython library and also make an CulturelandClient object. This process might take some time to generate an object. While the object is being generated, the object automatically logs into Cultureland website. When you get the message `[SUCCESS] User gooday2die Logged in Successfully.` It means that the object has been successfully generated. If you are willing to use this class in a big project or fast runtime demanding project, I would suggest you using `asyncio` when using this class.

```
>>> c
Cultureland Client Object, Logged in as gooday2die
>>> c.redeem('4180-0252-0565-2549')
[SUCCESS] User gooday2die successfully redeemed code: 4180-0252-0565-2549
[True, '1000원']
>>> c.redeem('4180-0252-0565-2549')
[ERROR] User gooday2die failed to redeem code 4180-0252-0565-2549 : 잔액이 0원인 상품권
[False, '잔액이 0원인 상품권']
```
You can redeem by using `redeem` method of `CulturelandClient` object. The method returns `list` type object. 
- If the Redeeming process was successful, it returns [True, Amount Redeemed]
- If the Redeeming process was unsuccessful, it returns [False, Error Reason]

## Contacts & ETC
If you got questions on this project, or have a good idea to add into this project, let me know by POC edina00@naver.com. Also Since this project is NOT official project and it is kind of sketchy, this project might be removed from Github if Cultureland wants me to remove this project from Github. Any pull requests as well as issue reporting is welcomed. 
