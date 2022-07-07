from PIL import Image
import os
from anticaptchaofficial.imagecaptcha import *


class AntiCaptchaFailedException(Exception):
    pass


class AntiCaptchaAPIKeyFailedException(Exception):
    pass


class AntiCaptchaNoBalanceException(Exception):
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
    solver = imagecaptcha()
    solver.set_verbose(0)
    solver.set_key(key)
    balance = solver.get_balance()
    if balance == -1:
        raise AntiCaptchaAPIKeyFailedException()
    if balance == 0:
        raise AntiCaptchaNoBalanceException()

    solver.set_soft_id(0)

    captcha_text = solver.solve_and_return_solution("./captcha.png")
    if captcha_text != 0:
        return captcha_text
    else:
        raise AntiCaptchaFailedException()


def report_incorrect_captcha(key):
    solver = imagecaptcha()
    solver.set_verbose(0)
    solver.set_key(key)
    solver.report_incorrect_recaptcha()


def report_correct_captcha(key):
    solver = imagecaptcha()
    solver.set_verbose(0)
    solver.set_key(key)
    solver.report_correct_recaptcha()


def clean_up():
    #os.remove("./captcha.png")
    os.remove("./screenshot.png")