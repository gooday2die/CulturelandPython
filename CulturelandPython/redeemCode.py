import selenium.common.exceptions
from selenium.webdriver.common.by import By


class CodeInvalidError:
    pass


def redeem_code(code, web_driver):
    """
    A function that redeems the gift code to the server
    :param code: The code to verify and redeem
    :param web_driver: The web driver of the current session
    :return: True if success, False if Failure
    """

    code_1 = code[:4]  # First 4
    code_2 = code[5:9]  # Second 4
    code_3 = code[10:14]  # Third 4
    code_4 = code[15:]  # Last 4 or 6 Digits

    web_driver.get("https://m.cultureland.co.kr/csh/cshGiftCard.do")  # Opens the giftcard redeem page
    web_driver.execute_script("$(\"#txtScr11\")[0].value = \"" + code_1 + "\";")  # Enter First 4
    web_driver.execute_script("$(\"#txtScr12\")[0].value = \"" + code_2 + "\";")  # Enter Second 4
    web_driver.execute_script("$(\"#txtScr13\")[0].value = \"" + code_3 + "\";")  # Enter Third 4

    key_dict = generate_key_dict(web_driver)  # get the key dict
    enter_last_key(code_4, web_driver, key_dict)  # enter last 4
    web_driver.find_element(By.XPATH, "//*[@id=\"btnCshFrom\"]").click()  # Submit

    amount_redeemed = ""
    for i in range(10):
        try:
            amount_redeemed = web_driver.find_element(By.XPATH, "//*[@id=\"wrap\"]/div[" + str(i) + "]/section/dl/dd").text
            if len(amount_redeemed) != 0:
                break
        except selenium.common.exceptions.NoSuchElementException:
            pass

    if amount_redeemed == "0원":  # If the code was invalid
        error_reason = ""
        for i in range(10):
            try:
                error_reason = web_driver.find_element(By.XPATH, "//*[@id=\"wrap\"]/div[" + str(i) + "]/section/div/table/tbody/tr/td[3]/b").text
                if len(error_reason) != 0:
                    break
            except selenium.common.exceptions.NoSuchElementException:
                pass
        return [False, error_reason]
    else:
        amount_redeemed = amount_redeemed.replace("," , "")
        amount_redeemed = amount_redeemed.replace("원", "")
        amount_redeemed = int(amount_redeemed)
        return [True, amount_redeemed]


def generate_key_dict(web_driver):
    """
    As we did the same thing earlier before when logging in, we also need the key dict here
    This generates and returns the key dictionary and JS commands
    :param web_driver: The web driver to use in this session
    :return: The key dictionary
    """
    web_driver.find_element(By.XPATH, "// *[ @ id = \"txtScr14\"]").click()
    web_driver.find_element(By.XPATH, "//*[@id=\"txtScr14\"]").click()
    keyboard_dict = dict()

    for i in range(2):  # from 1st row to 2nd row
        for j in range(1, 7, 1):
            js_script = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_txtScr14_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]").get_attribute("onmousedown")
            alt_value = web_driver.find_element(By.XPATH, "//*[@id=\"mtk_txtScr14_Row" + str(i) + "\"]/div[" +
                                                str(j) + "]/div/img").get_attribute("alt")
            keyboard_dict[alt_value] = js_script

    return keyboard_dict


def enter_last_key(last_digit, web_driver, key_dict):
    """
    A function that enters last 4 or 6 digits of Giftcard
    :param last_digit: The last digit to enter
    :param web_driver: The web driver to use in this session
    :param key_dict: The key dictionary to use
    :return:
    """
    for i in last_digit:
        js_command = key_dict[i]
        web_driver.execute_script(js_command)
    try:  # If the gift code is 4 digits, we need done button
        web_driver.execute_script("mtk.done(event, this);")
    except selenium.common.exceptions.JavascriptException:  # if the gift card is 6 digits it will raise exception
        pass
