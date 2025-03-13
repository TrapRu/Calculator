import requests

def get_moex_currency_rates():
    try:
        url = "https://iss.moex.com/iss/statistics/engines/futures/markets/indicativerates/securities.json"
        params = {
            'securities': 'USD/RUB',
            'iss.meta': 'off'
        }

        print('[Debug 1] Отправка запроса...')
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(f'[Debug 2] Статус ответа: {response.status_code}')

        data = response.json()
        print('[Debug 3] Получены сырые данные:', data)  # Для анализа структуры

        rates = {}
        
        # Проверяем существование ключей в ответе
        if 'securities' not in data or 'data' not in data['securities']:
            print('[Ошибка] Некорректная структура ответа API')
            return None

        print('[Debug 4] Обработка данных...')
        for item in data['securities']['data']:
            print('[Debug] Текущий элемент:', item)  # Показывает структуру элемента
            if item[2] == 'USD/RUB':
                rates['USD/RUB'] = item[3]
            elif item[2] == 'EUR/RUB':
                rates['EUR/RUB'] = item[3]
    
        print('[Debug 5] Результат:', rates)
        return rates

    except requests.exceptions.RequestException as e:
        print(f"[Ошибка] Проблема с запросом: {e}")
        return None
    except Exception as e:
        print(f"[Ошибка] Непредвиденная ошибка: {e}")
        return None
    
    

# Тестирование функции
"""  

if __name__ == "__main__":
    currency_rates = get_moex_currency_rates()
    
    if currency_rates:
        print("\nРезультат:")
        print(f"USD/RUB: {currency_rates.get('USD/RUB', 'Нет данных')}")
        print(f"EUR/RUB: {currency_rates.get('EUR/RUB', 'Нет данных')}")
    else:
        print("Не удалось получить данные")

"""