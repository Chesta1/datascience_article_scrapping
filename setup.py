from setup import setup,find_packages

setup(
    name ='python_package',
    version = 0.1,
    packages = find_packages()
    install=[pandas,
             selenium,
             datetime],
    author="Chesta Dhingra",
    author_email = "chestadhingra25@gmail.com",
    license='MIT',
    description = "A python package for webscraping the latest articles on popular Data science blogs",
    long_description=open('README.md').read()
    url = ""

)