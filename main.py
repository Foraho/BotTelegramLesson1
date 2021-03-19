import telebot

bot = telebot.TeleBot('1772195736:AAHfP2tPN2GMJ7FF1WlUkEYZlfS0poMZg8s') #Создаём переменную где будет хранится токен бота

keyboard1 = telebot.types.ReplyKeyboardMarkup(True) #Первая true означает что кнопки стаунт меньшего размера, вторая true означает что после выбора кнопку исчезнут
keyboard1.row('Я люблю пить чай', 'Я люблю пить кофе', 'Нет, я банан') #

@bot.message_handler(commands=['start'])
def abc(message):
	bot.send_message(message.chat.id, 'Приветсвую вас сударь, вот список всех моих команд: привет, пока, хакер, кнопки') #Создаём комманду /start на которую нам бот будет отвечать сообщением

@bot.message_handler(content_types=['text']) #Передаём на проверку сообщения, в данном случаем текст
def lalala(message):
  if message.text.lower() == 'привет':
    bot.send_message(message.chat.id, 'Здраствуйте') #Если мы напишем привет то бот выведет здраствуйте
  elif message.text.lower() == 'кнопки':
    bot.send_message(message.chat.id, 'Вот ваши кнопки', reply_markup=keyboard1) #Если мы напишем кнопки то бот выведет кнопки
  elif message.text.lower() == 'пока':
    bot.send_message(message.chat.id, 'Досвидания') #Инчае если вы введёте пока то бот выведет досвидания
  elif message.text.lower() == 'хакер':
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEBAb1gVNtzrDrxJp7YhCJzLD9wyj7C7wACUAEAAqghIQaxvfG1zemEoh4E') #Отправка стикера
  else:
	  bot.send_message(message.chat.id, message.text) #Если ни то ни другое не выполнится то бот просто выведет введённое вами сообщение

bot.polling(none_stop=True) #Эта строка нужна для того чтобы бот ждал новых сообщений от сервера
