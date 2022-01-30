from CulturelandPython import webDriverManager
import os


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # need to specify the Dir of DB file
    chrome_driver_path_linux = os.path.join(BASE_DIR, "chromedriver")
    c = webDriverManager.CulturelandClient('username', 'password', chrome_driver_path_linux)
    c.redeem('4180-0115-2657-8251')
    c.disconnect()
