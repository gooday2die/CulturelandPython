from PIL import Image
import os
from anticaptchaofficial.imagecaptcha import *


class AntiCaptchaFailedException(Exception):
    """
    A class that is for anti-captcha fails to solve captchas
    """
    pass


class AntiCaptchaAPIKeyFailedException(Exception):
    """
    A class that is for anti-captcha API key was invalid.
    """
    pass


class AntiCaptchaNoBalanceException(Exception):
    """
    A class that is for anti-captcha API's balance is 0. (or none)
    """
    pass


def crop_captcha_image():
    """
    A function that crops captcha image from the original screenshot that we took.
    :return: returns image object that includes the captcha image.
    """
    image = Image.open("screenshot.png")
    area = (35, 379, 246, 441)  # in screen resolution 1000,1000 the captcha area is this position.
    crop_image = image.crop(area)
    image_dir = os.path.join(os.getcwd(), "./captcha.png")  # save screenshot in /tmp/captcha.png
    try:
        crop_image.save(image_dir)
    except FileNotFoundError:
        os.mkdir(image_dir)
        crop_image.save(image_dir)
    return crop_image


def capture_captcha_image(web_driver):
    """
    A function that captures captcha image multiple times so that we can make a prediction model.
    :param web_driver: the web_driver object that this session is using
    :return: None
    """
    web_driver.save_screenshot("screenshot.png")  # save screenshot
    crop_captcha_image()  # crop image and save it


def get_captcha_solved(key):
    """
    A function that solves captcha image using AntiCaptcha API.
    This will solve by using imagecaptcha from AntiCaptcha.
    :param key: a string that represents Anti captcha API key
    :return: returns string object when it is properly solved.
    """
    solver = imagecaptcha()
    solver.set_verbose(0)  # set verbose 0 since we do not want verbose.
    solver.set_key(key)
    balance = solver.get_balance()
    if balance == -1:  # Means API Key was invalid
        raise AntiCaptchaAPIKeyFailedException()
    if balance == 0:  # Means balance is 0. or less lol
        raise AntiCaptchaNoBalanceException()

    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("./captcha.png")
    if captcha_text != 0:
        return captcha_text
    else:  # value that is 0 means that it failed
        raise AntiCaptchaFailedException()


def report_incorrect_captcha(key):
    """
    A function that is for reporting to AntiCaptcha API that the captcha result was not correct.
    :param key: a string that represents Anti captcha API key
    :return: None
    """
    solver = imagecaptcha()
    solver.set_verbose(0)
    solver.set_key(key)
    solver.report_incorrect_recaptcha()


def report_correct_captcha(key):
    """
    A function that is for reporting to AntiCaptcha API that the captcha result was not correct.
    :param key: a string that represents Anti captcha API key
    :return: None
    """
    solver = imagecaptcha()
    solver.set_verbose(0)
    solver.set_key(key)
    solver.report_correct_recaptcha()


def clean_up():
    """
    A function that removes captcha.png and screenshot.png.
    This function is for cleaning up the space.
    """
    os.remove("./captcha.png")
    os.remove("./screenshot.png")
