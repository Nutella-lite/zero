import telebot
import requests

# Инициализация бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот погоды. Напиши мне название города, и я покажу тебе погоду в нем.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text
    weather_data = get_weather(city)
    if weather_data:
        response = f"Погода в городе {city.title()}: {weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}"
    else:
        response = f"Извините, не удалось получить данные о погоде для города {city.title()}"
    bot.reply_to(message, response)

# Получение данных о погоде от OpenWeatherMap
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_OPENWEATHERMAP_API_KEY&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Запуск бота
bot.polling()