import requests
import time
print('''█████████████████████████
█───█─███─█────███──█───█
█─███──█──█─██─████─██─██
█───█─█─█─█─██─████─██─██
█─███─███─█─██─█─██─██─██
█───█─███─█────█────█───█
█████████████████████████
██████████████████████████████████
█───█───█────█───█─█─█───█───█───█
█─████─██─██─██─██─█─█─███─███─███
█───██─██────██─██─█─█───█───█───█
███─██─██─██─██─██─█─███─█─█████─█
█───██─██─██─██─██───█───█───█───█
██████████████████████████████████''')

print('''Привет
Это скрипт, который будет автоматически сменять эмоджи статусы
Сначала тебе нужно получить три токена.
Токены действуют 24 часа, так что потом придется получать новый

1)Скопируй ссылку и вставь в браузере. Нажми разрешить. Теперь тут в введи свой токен от access_token= до &expires_in. Это токен от приложения, вашему аккаунту ничего не угрожает
https://oauth.vk.com/authorize?client_id=7622189&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1''')
tok_druzba=input('Введите первый токен: ')
print('''Теперь те же действия, но для другого приложения
https://oauth.vk.com/authorize?client_id=7641157&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1''')
tok_adrik=input('Введите второй токен: ')
print('''И еще один токен
https://oauth.vk.com/authorize?client_id=7362610&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1''')
tok_covid=input('Третий токен: ')
print('Все токены получены')
vrem=float(input('Введите время между сменами эмоджи статусов в секундах (не менее 0.1 и не болеее 14 400): '))

print('''Как вы хотите ограничить длительность действия скрипта:
1) По количеству смен эмоджи статуса (не более''',int((86400/vrem)))
print('''2) Не ограничивать (максимальное время действия скрипта - 24 часа''')
vib=input('Введите 1 или 2: ')
if vib==1:
    pov=int(input("Введите количество смен: "))
z=0
while True:
    for id in range(1,130):
        if id <15:
            l = requests.get('https://api.vk.com/method/status.setImage?access_token='+tok_covid+'&v=5.123&status_id='+str(id))
            time.sleep(vrem)
            print(l.text)
            z+=1
        elif id>105 and id<110:
            l = requests.get('https://api.vk.com/method/status.setImage?access_token='+tok_adrik+'&v=5.123&status_id='+str(id))
            time.sleep(vrem)
            print(l.text)
            z += 1
        elif id>113 and id<122:
            l = requests.get('https://api.vk.com/method/status.setImage?access_token='+tok_druzba+'&v=5.123&status_id='+str(id))
            time.sleep(vrem)
            print(l.text)
            z += 1
        else:
            d=0
        if vib==1 and z>pov:
            break
