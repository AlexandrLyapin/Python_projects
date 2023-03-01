import telebot
import random

from telebot import types

bot = telebot.TeleBot('5968590184:AAG9AJe1vCXMwpVf3wmQskEv_VXfwWN2nHc')

with open("input.txt", "r") as file:
    s = file.read()
cat = s.split()

basket = []
basketdop = {1: 0, 2: 0, 3: 0, 4: 0}
sumall = 0
userdata = []
users = dict()
flags = dict()
yes = '✅'
no = '❌'
telegram = dict()
room = dict()
dormitory = dict()

@bot.message_handler(commands=['start'])
def start(message):
    users[message.chat.id] = basketdop.copy()
    telegram[message.chat.id] = '@' + str(message.from_user.username)
    room[message.chat.id] = None
    dormitory[message.chat.id] = None
    mess = f'Привет, <b>{message.from_user.first_name}</b>, пиши <b>"команды"</b> или <b>/help</b>, чтобы посмотреть мои команды😊'
    flags[message.chat.id] = 0
    bot.send_message(message.chat.id, mess, parse_mode='html')
@bot.message_handler(commands=['help'])
def help(message):
    mess = f'Список команд:\n\n1) <b>каталог</b> - посмотреть список товаров\n2) <b>корзина</b> - посмотреть корзину\n3) <b>заказать</b> - сделать заказ\n4) <b>добавить "код товара" "количество"</b> - добавить товары в корзину\n5) <b>личный кабинет</b> - посмотреть свои даннные\n6) <b>комната "номер комнаты"</b> - внести номер комнаты в личный кабинет (вводить без пробелов)\n7) <b>общежитие "номер общежития"</b> - внести номер общежития в личный кабинет\n8) <b>удалить "код товара" "количество"</b> - удалить товары из корзины\n9) <b>контакты</b> - связаться с администратором магазина\n\nПример добавления в корзину:\n<b>добавить 1 4</b>  -  добавлено 4 Бёрна\n<b>добавить 3 2</b>  -  добавлено 2 Монстра'
    flags[message.chat.id] = 0
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    global basket
    global sumall
    sumall = int(users[message.chat.id][1]) * 110 + int(users[message.chat.id][2]) * 110 + int(users[message.chat.id][3]) * 100 + int(users[message.chat.id][4]) * 100
    if message.text == "каталог" or message.text == "Каталог":
        catalog = "1) BURN Тёмная Энергия 0,449ml - 110 руб \nВ наличии - " + str(cat[0]) + " шт"
        if cat[0] == '0' or cat[0] == 0:
            catalog += no
        else:
            catalog += yes
        catalog += "\n\n2) BURN Яблоко-киви 0,449ml - 110 руб \nВ наличии - " + str(cat[1]) + " шт"
        if cat[1] == '0' or cat[1] == 0:
            catalog += no
        else:
            catalog += yes        
        catalog += "\n\n3) Monster Ultra Sunrise - 100 руб\nВ наличии - " + str(cat[2]) + " шт"
        if cat[2] == '0' or cat[2] == 0:
            catalog += no
        else:
            catalog += yes        
        catalog += "\n\n4) Adrenaline Rush classic 0,449ml - 100 руб \nВ наличии - " + str(cat[3]) + " шт"
        if cat[3] == '0' or cat[3] == 0:
            catalog += no
        else:
            catalog += yes     
        flags[message.chat.id] = 0
        bot.send_message(message.chat.id, catalog, parse_mode='html')
    elif message.text == "команды" or message.text == "Команды":
        commands = f'Список команд:\n\n1) <b>каталог</b> - посмотреть список товаров\n2) <b>корзина</b> - посмотреть корзину\n3) <b>заказать</b> - сделать заказ\n4) <b>добавить "код товара" "количество"</b> - добавить товары в корзину\n5) <b>личный кабинет</b> - посмотреть свои даннные\n6) <b>комната "номер комнаты"</b> - внести номер комнаты в личный кабинет (вводить без пробелов)\n7) <b>общежитие "номер общежития"</b> - внести номер общежития в личный кабинет\n8) <b>удалить "код товара" "количество"</b> - удалить товары из корзины\n9) <b>контакты</b> - связаться с администратором магазина\n\nПример добавления в корзину:\n<b>добавить 1 4</b>  -  добавлено 4 Бёрна\n<b>добавить 3 2</b>  -  добавлено 2 Монстра'
        flags[message.chat.id] = 0
        bot.send_message(message.chat.id, commands, parse_mode='html')
    elif message.text == "контакты" or message.text == "Контакты":
        contacts = f'<b>ВК:</b> https://vk.com/machine_21\n<b>Telegram:</b> @alexlyapin'
        flags[message.chat.id] = 0
        bot.send_message(message.chat.id, contacts, parse_mode='html')
    elif 'добавить' in message.text or 'Добавить' in message.text or 'Add' in message.text or 'add' in message.text:       
        flags[message.chat.id] = 0
        basket = message.text.split()
        if len(basket) != 3:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        elif basket[1].isdigit() == 0 or basket[2].isdigit() == 0:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        else:
            basket.pop(0)
            if int(basket[0]) < 1 or int(basket[0]) > 4 or int(basket[1]) < 1:
                if int(basket[0]) < 1 or int(basket[0]) > 4:
                    bot.send_message(message.chat.id, "Введён неверный код товара❌", parse_mode='html')
                else:
                    bot.send_message(message.chat.id, "Некорректное количество банок❌", parse_mode='html')
            else:
                users[message.chat.id][int(basket[0])] += int(basket[1])
                basket.pop(0)
                basket.pop(0)
                bot.send_message(message.chat.id, "Успешное добавление товара✅", parse_mode='html')
    elif 'удалить' in message.text or 'Удалить' in message.text or 'Delete' in message.text or 'delete' in message.text:
        flags[message.chat.id] = 0
        basket = message.text.split()
        if len(basket) != 3:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        elif basket[1].isdigit() == 0 or basket[2].isdigit() == 0:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        else:
            basket.pop(0)
            if int(basket[0]) < 1 or int(basket[0]) > 4 or int(basket[1]) < 1 or int(basket[1]) > users[message.chat.id][int(basket[0])]:
                if int(basket[0]) < 1 or int(basket[0]) > 4:
                    bot.send_message(message.chat.id, "Введён неверный код товара❌", parse_mode='html')
                else:
                    bot.send_message(message.chat.id, "Некорректное количество банок❌", parse_mode='html')
            else:
                users[message.chat.id][int(basket[0])] -= int(basket[1])
                basket.pop(0)
                basket.pop(0)
                bot.send_message(message.chat.id, "Успешное удаление товара✅", parse_mode='html')
    elif message.text == "корзина" or message.text == "Корзина":
        flags[message.chat.id] = 0
        names = []
        temp = 'Ваша корзина:\n\n'
        if users[message.chat.id][1] == users[message.chat.id][2] == users[message.chat.id][3] == users[message.chat.id][4] == 0:
            bot.send_message(message.chat.id, "Ваша корзина пуста ☹", parse_mode='html')
        else:
            for i in users[message.chat.id]:
                if users[message.chat.id][i] != 0:
                    if i == 1:
                        names.append('Burn Тёмная Энергия' + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 2:
                        names.append('Burn Яблоко-киви'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 3:
                        names.append('Monster Ultra Sunrise'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 4:
                        names.append('Adrenaline Rush classic'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
            for i in range(len(names)):
                temp += str(i + 1) + ') ' + str(names[i]) + '\n'
            temp += '\n' + 'Общая сумма: ' + str(sumall) + ' руб'
            bot.send_message(message.chat.id, temp, parse_mode='html')
    elif message.text == "заказать" or message.text == "Заказать":
        if room[message.chat.id] == None or dormitory[message.chat.id] == None:
            bot.send_message(message.chat.id, "Укажите все данные в личном кабинете!🙄", parse_mode='html')
        else:
            flags[message.chat.id] = 1
            names = []
            temp = 'Ваш заказ:\n\n'
            if users[message.chat.id][1] == users[message.chat.id][2] == users[message.chat.id][3] == users[message.chat.id][4] == 0:
                bot.send_message(message.chat.id, "Вы ничего не добавили в корзину ☹", parse_mode='html')
            else:
                for i in users[message.chat.id]:
                    if users[message.chat.id][i] != 0:
                        if i == 1:
                            names.append('Burn Тёмная Энергия' + ' - ' + str(users[message.chat.id][i]) + ' шт')
                        if i == 2:
                            names.append('Burn Яблоко-киви'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                        if i == 3:
                            names.append('Monster Ultra Sunrise'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                        if i == 4:
                            names.append('Adrenaline Rush classic'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                for i in range(len(names)):
                    temp += str(i + 1) + ') ' + str(names[i]) + '\n'
                temp += '\n' + 'Общая сумма: ' + str(sumall) + ' руб'
                bot.send_message(message.chat.id, temp, parse_mode='html')
                bot.send_message(message.chat.id, "Всё верно ?", parse_mode='html')
    elif 'комната' in message.text or 'Комната' in message.text or 'room' in message.text or 'Room' in message.text or 'рум' in message.text or 'Рум' in message.text:
        flags[message.chat.id] = 0
        basket = message.text.split()
        if len(basket) != 2:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        elif basket[1].isdigit() == 0:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        else:
            basket.pop(0)
            room[message.chat.id] = basket[0]
            basket.pop(0)
            bot.send_message(message.chat.id, "Номер комнаты успешно сохранён✅", parse_mode='html')
    elif 'общежитие' in message.text or 'Общежитие' in message.text or 'Общага' in message.text or 'общага' in message.text:
        flags[message.chat.id] = 0
        basket = message.text.split()
        if len(basket) != 2:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        elif basket[1].isdigit() == 0:
            bot.send_message(message.chat.id, "Неверный формат ввода❌", parse_mode='html')
        else:
            basket.pop(0)
            dormitory[message.chat.id] = basket[0]
            basket.pop(0)
            bot.send_message(message.chat.id, "Номер общежития успешно сохранён✅", parse_mode='html')
    elif message.text == "личный кабинет" or message.text == "Личный кабинет":
        prof = "<b>Ваши данные</b>\n\nTelegram: "
        prof += str(telegram[message.chat.id]) + '\nКомната: '
        prof += str(room[message.chat.id]) + '\nОбщежитие: '
        prof += str(dormitory[message.chat.id])
        flags[message.chat.id] = 0
        bot.send_message(message.chat.id, prof, parse_mode='html')  
    elif (message.text == "Да" or message.text == "да" or message.text == "yes" or message.text == "Yes") and flags[message.chat.id] == 1:
        flags[message.chat.id] = 0
        if (int(cat[0]) - int(users[message.chat.id][1]) < 0 or int(cat[1]) - int(users[message.chat.id][2]) < 0 or int(cat[2]) - int(users[message.chat.id][3]) < 0 or int(cat[3]) - int(users[message.chat.id][4]) < 0):
            bot.send_message(message.chat.id, "Какого-то из товаров нет в наличии ☹", parse_mode='html')
        else:
            mass = []
            for i in users[message.chat.id]:
                if users[message.chat.id][i] != 0:
                    if i == 1:
                        mass.append('Burn Тёмная Энергия' + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 2:
                        mass.append('Burn Яблоко-киви'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 3:
                        mass.append('Monster Ultra Sunrise'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
                    if i == 4:
                        mass.append('Adrenaline Rush classic'  + ' - ' + str(users[message.chat.id][i]) + ' шт')
            dop = '\n'
            for i in range(len(mass)):
                dop += str(mass[i]) + '\n'
            dop += '\n'
            cat[0] = int(cat[0]) - int(users[message.chat.id][1])
            cat[1] = int(cat[1]) - int(users[message.chat.id][2])
            cat[2] = int(cat[2]) - int(users[message.chat.id][3])
            cat[3] = int(cat[3]) - int(users[message.chat.id][4])
            chel = "Telegram: " + str(telegram[message.chat.id]) + ' Комната: '
            chel += str(room[message.chat.id]) + " Общежитие: "
            chel += str(dormitory[message.chat.id])
            chel += dop
            replacement = '' + str(cat[0]) + str(cat[1]) +  str(cat[2]) +  str(cat[3])
            st = s.replace("s", replacement)
            with open ('input.txt', 'w') as file:
                file.write(st)
            with open ('output.txt', 'a') as f:
                f.write(chel)
            bot.send_message(message.chat.id, "Ваш заказ принят, приходи ещё😉", parse_mode='html')
            users[message.chat.id][1] = 0
            users[message.chat.id][2] = 0
            users[message.chat.id][3] = 0
            users[message.chat.id][4] = 0
            sumall = 0
    elif (message.text == "Нет" or message.text == "нет" or message.text == "no" or message.text == "No") and flags[message.chat.id] == 1:
        flags[message.chat.id] = 0
        bot.send_message(message.chat.id, "Хорошо, повыбирай ещё)", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Не надо меня ломать 🗿", parse_mode='html')

bot.polling(none_stop=True)
