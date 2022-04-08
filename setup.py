from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:  # Read README.md file for long_description
    long_description = fh.read()

setup(
    name='CulturelandPython',
    version='0.1.2',
    description='An Unofficial Python Library for Cultureland',
    url='https://github.com/gooday2die/CulturelandPython',
    author='Gooday2die',
    author_email='edina00@naver.com',
    license='GPL',
    packages=['CulturelandPython'],
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=['selenium', 'webdriver-manager'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)
