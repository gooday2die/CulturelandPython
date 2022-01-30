from selenium.webdriver.common.by import By


class LoginFailureException(Exception):
    pass


def login(web_driver, username, password):
    """
    A function that logs into the Cultureland Website like magic!
    :param web_driver: The web driver this session is using
    :param username: The username to use
    :param password: The password to use
    :return:
    """

    web_driver.execute_script("$(\"#txtUserId\")[0].value = \"" + username + "\";")  # Input user name into system
    web_driver.find_element(By.XPATH, "//*[@id=\"passwd\"]").click()  # prompt virtual keyboard

    keyboard_dict = generate_keyboard(web_driver)
    enter_password(password, keyboard_dict, web_driver)  # Enter password
    if web_driver.current_url == "https://m.cultureland.co.kr/mmb/loginMain.do":
        raise LoginFailureException


def generate_keyboard(web_driver):
    """
    Generates the Virtual keyboard mapping into JS command

    The Virtual keyboard works stupid.
    Each key has a values by DIV but they have img tag that shows the alt values.

    The generated dictionary works like this '1': ['mtk.cap(event, this);'
    It literally matches the key with the JS command that would be used.

    :param web_driver: The web driver that the current session is using
    :return: returns the keyboard mapping dictionary
    """
    keyboard_dict = dict()

    for i in range(3):  # from 1st row to 3rd row
        for j in range(1, 12, 1):
            js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]").get_attribute("onmousedown")
            alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]/div/img").get_attribute("alt")
            keyboard_dict[alt_value] = [js_script]

    for i in range(2, 10, 1):  # 4th row only
        js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]").get_attribute("onmousedown")
        alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]/div/img").get_attribute("alt")
        keyboard_dict[alt_value] = [js_script]

    # all lower case keys registered till here

    web_driver.execute_script("mtk.sp(event, this);")  # Change into special letters

    for i in range(3):  # from 1st row to 3rd row special character
        for j in range(1, 12, 1):
            js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]").get_attribute("onmousedown")
            alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]/div/img").get_attribute("alt")
            alt_value = translate_letter(alt_value)
            keyboard_dict[alt_value] = ["mtk.sp(event, this);", js_script, "mtk.sp(event, this);"]

    for i in range(2, 10, 1):  # 4th row only special character
        js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]").get_attribute("onmousedown")
        alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]/div/img").get_attribute("alt")
        alt_value = translate_letter(alt_value)
        keyboard_dict[alt_value] = ["mtk.sp(event, this);", js_script, "mtk.sp(event, this);"]

    web_driver.execute_script("mtk.sp(event, this);")  # Change into special letters

    # all special character keys are registered till here

    web_driver.execute_script("mtk.cap(event, this);")  # Change into capital letters

    for i in range(1, 3):  # from 1st row to 3rd row
        for j in range(1, 12, 1):
            js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]").get_attribute("onmousedown")
            alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]/div/img").get_attribute("alt").upper().replace("대문자", "")
            keyboard_dict[alt_value] = ["mtk.cap(event, this);", js_script, "mtk.cap(event, this);"]

    for i in range(2, 10, 1):  # 4th row only
        js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]").get_attribute("onmousedown")
        alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_passwd_Row3\"]/div[" +
                                            str(i) + "]/div/img").get_attribute("alt").upper().replace("대문자", "")
        keyboard_dict[alt_value] = ["mtk.cap(event, this);", js_script, "mtk.cap(event, this);"]

    web_driver.execute_script("mtk.cap(event, this);")  # Change into lower letters

    return keyboard_dict


def translate_letter(word):
    """
    This dumbass people Translated special letters into Korean letters.
    So This function translates the special letters into normal characters.
    :param word: The word to translate into normal character
    :return: The translated word
    """

    try:
        word.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:  # The shitshow begins here :b
        if word == "어금기호":
            word = '`'
        elif word == "물결표시":
            word = '~'
        elif word == "느낌표":
            word = '!'
        elif word == "골뱅이":
            word = '@'
        elif word == "샾":
            word = '#'
        elif word == "달러기호":
            word = '$'
        elif word == "퍼센트":
            word = '%'
        elif word == "꺽쇠":
            word = '^'
        elif word == "엠퍼샌드":
            word = '&'
        elif word == "별표":
            word = '*'
        elif word == "왼쪽괄호":
            word = '('
        elif word == "오른쪽괄호":
            word = ')'
        elif word == "빼기":
            word = '-'
        elif word == "밑줄":
            word = '_'
        elif word == "등호":
            word = '='
        elif word == "더하기":
            word = '+'
        elif word == "왼쪽대괄호":
            word = '['
        elif word == "왼쪽중괄호":
            word = '{'
        elif word == "오른쪽대괄호":
            word = ']'
        elif word == "오른쪽중괄호":
            word = '}'
        elif word == "역슬래시":
            word = '\\'
        elif word == "수직막대":
            word = '|'
        elif word == "세미콜론":
            word = ';'
        elif word == "콜론":
            word = ':'
        elif word == "슬래시":
            word = '/'
        elif word == "물음표":
            word = '?'
        elif word == "쉼표":
            word = ','
        elif word == "왼쪽꺽쇠괄호":
            word = '<'
        elif word == "마침표":
            word = '.'
        elif word == "오른쪽꺽쇠괄호":
            word = '>'
        elif word == "작은따옴표":
            word = '\''
        elif word == "따옴표":
            word = '\"'
        elif word == "더하기":
            word = '+'
        elif word == "빼기":
            word = '-'
        elif word == "별표":
            word = '{'
        elif word == "슬래시":
            word = '/'
        else:
            word = 'None'
    else:
        pass

    return word


def enter_password(password_string, keyboard_dict, web_driver):
    """
    Enters password using the keyboard dictionary and each corresponding commands.
    :param password_string: The password that the user is using
    :param keyboard_dict: The keyboard_dict that is generated by generate_keyboard function
    :param web_driver: The web driver object that the current session is using
    :return:
    """
    for i in password_string:
        js_command = keyboard_dict[i]

        for j in js_command:
            web_driver.execute_script(j)

    web_driver.execute_script("mtk.done(event, this);")  # done typing password
    web_driver.find_element(By.XPATH, "//*[@id=\"btnLogin\"]").click()
