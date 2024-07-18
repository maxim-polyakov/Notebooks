{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "93759e3d-9f43-49b1-98bf-209469186107",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Сейчас в городе Нижний Новгород 31 °C\n",
      "Ощущается как 30 °C\n"
     ]
    }
   ],
   "source": [
    "# подключаем библиотеку для работы с запросами\n",
    "import requests\n",
    "# указываем город\n",
    "city = 'Нижний Новгород'\n",
    "# формируем запрос\n",
    "url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'\n",
    "# отправляем запрос на сервер и сразу получаем результат\n",
    "weather_data = requests.get(url).json()\n",
    "# получаем данные о температуре и о том, как она ощущается\n",
    "temperature = round(weather_data['main']['temp'])\n",
    "temperature_feels = round(weather_data['main']['feels_like'])\n",
    "# выводим значения на экран\n",
    "print('Сейчас в городе', city, str(temperature), '°C')\n",
    "print('Ощущается как', str(temperature_feels), '°C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "339332b4-aca5-4cf6-b44c-dc2ce37e381a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
