from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    data_str = '01/11/1996'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)


if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()