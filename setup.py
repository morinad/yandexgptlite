from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yandexgptlite',
    version='0.1.7',
    packages=find_packages(),
    description='Получение ответов от YandexGPT Lite',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Александр Морин',
    author_email='y.director@yandex.ru',
    url='https://github.com/morinad/yandexgptlite',
    install_requires=[
        'requests'
    ],
)