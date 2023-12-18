from setuptools import setup, find_packages

setup(
    name='yandexgptlite',
    version='0.1',
    packages=find_packages(),
    description='Получение ответов от YandexGPT Lite',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Александр Морин',
    author_email='y.director@yandex.ru',
    url='https://github.com/morinad/yandexgptlite',
    install_requires=[
        'json',
        'requests'
    ],
)