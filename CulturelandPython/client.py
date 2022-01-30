from selenium import webdriver
from CulturelandPython import redeemCode, login


class CulturelandClient:
    """
    A class that is a single session and a single client for logging in
    """
    def __init__(self, username, passwd, chromedriver_dir):
        """
        A init method for class CulturelandClient
        :param username: The username
        :param passwd: The password
        """
        self.username, self.passwd = username, passwd
        self.web_driver = None
        self.chromedriver_dir = chromedriver_dir

        self.login()

    def login(self):
        """
        A method that logs into the system
        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        # Have fake client info so that this is not considered headless
        options.add_argument("headless")  # Open with headless

        self.web_driver = webdriver.Chrome(executable_path=self.chromedriver_dir, chrome_options=options)
        self.web_driver.get("https://m.cultureland.co.kr/mmb/loginMain.do")  # open login page
        try:
            login.login(self.web_driver, self.username, self.passwd)
            print("[SUCCESS] User " + self.username + " Logged in Successfully.")
        except login.LoginFailureException:
            print("[ERROR] User " + self.username + " Failed to login.")

    def redeem(self, code):
        """
        A method that redeems code
        :param ip: the ip address that the API was called
        :param code: The code to redeem
        :return:
        """
        result = redeemCode.redeem_code(code, self.web_driver)
        if result[0]:
            print("[SUCCESS] User " + self.username + " successfully redeemed code: " + code)
        else:
            print("[ERROR] User " + self.username + " failed to redeem code " + code + " : " + result[1])
        #self.disconnect()
        return result

    def disconnect(self):
        """
        A method that disconnects the session
        :return:
        """
        self.web_driver.quit()

    def __repr__(self):
        """
        A method that returns the object string
        :return: the string for __repr__
        """
        return "Cultureland Client Object, Logged in as " + self.username
