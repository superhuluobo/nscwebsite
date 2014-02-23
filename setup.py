import os
from setuptools import setup,find_packages

PROJECT_ROOT=os.path.dirname(os.path.abspath(__file__))

setup(name='nscwebsite',
      version='1.0',
      description='django framwork website',
      author='DrWrong',
      author_email='yuhangchaney@gmail.com',
      url='https://github.com/superhuluobo/nscwebsite',
      packages=find_packages(),
	  install_requires=['Django==1.6.2','django-mysql-pymysql']
     )
