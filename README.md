# Коннектор к YandexGPT Lite на Python

### Как использовать коннектор:

1) Активируем платёжный аккаунт Yandex.Cloud: https://console.cloud.yandex.ru/billing?section=accounts. Можно активировать пробный период на 60 дней.
Вам потребуется ID папки Yandex.Cloud, эти папки находятся тут: https://console.cloud.yandex.ru/folders/. Folder ID можно взять из URL или из интерфейса.


2) Получаем токен вашего аккаунта на Яндексе для подключения к YandexGPT:
https://oauth.yandex.ru/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb

3) Устанавливаем пакет pip:
pip install yandexgptlite

4) Импортируем класс из пакета:
from yandexgptlite import YandexGPTLite 

5) Подключаемся к Yandex GPT, создавая экземпляр класса (требуется указать папку Yandex Cloud и токен):
account = YandexGPTLite('b1g2k730lqhu8pc02a', 'y0_AgAAAAMf8GzATuwQAAAD15w-py1O8Ucn-RN6bl9W8hwdkX7vuE' )

6) Вызываем функцию обращения к GPT для нашего аккаунта (температура от 0 до 1, где единица - максимум творчества):
text = account.create_completion('Привет! Как твои дела?', '0.6')
print(text) #Привет! У меня всё хорошо, как дела у вас?

