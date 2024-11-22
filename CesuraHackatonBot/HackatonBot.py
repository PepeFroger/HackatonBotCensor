import telebot

bot = telebot.TeleBot('7042968739:AAFFRRl4jnFdZ3QLR1kOeyIEKZwRje0xV-I')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

# Список нецензурных слов (можно расширять по необходимости)
bad_words = [
    "архипиздрит", "басран", "бздение", "бздеть", "бздех", "бзднуть", "бздун", "бздунья", "бздюха", "бикса",
    "блежник", "блудилище", "бляд", "блябу", "блябуду", "блядун", "блядунья", "блядь", "блядюга", "взьебка",
    "волосянка", "взьебывать", "вз'ебывать", "выблядок", "выблядыш", "выебать", "выеть", "выпердеть", "высраться",
    "выссаться", "говенка", "говенный", "говешка", "говназия", "говнецо", "говно", "говноед", "говночист",
    "говнюк", "говнюха", "говнядина", "говняк", "говняный", "говнять", "гондон", "дермо", "долбоеб", "дрисня",
    "дрист", "дристать", "дристануть", "дристун", "дристуха", "дрочена", "дрочила", "дрочилка", "дрочить",
    "дрочка", "ебало", "ебальник", "ебануть", "ебаный", "ебарь", "ебатория", "ебать", "ебаться", "ебец",
    "ебливый", "ебля", "ебнуть", "ебнуться", "ебня", "ебун", "елда", "елдак", "елдачить", "заговнять",
    "задристать", "задрока", "заеба", "заебанец", "заебать", "заебаться", "заебываться", "заеть", "залупа",
    "залупаться", "залупить", "залупиться", "замудохаться", "засерун", "засеря", "засерать", "засирать",
    "засранец", "засрун", "захуячить", "злоебучий", "изговнять", "изговняться", "кляпыжиться", "курва",
    "курвенок", "курвин", "курвяжник", "курвяжница", "курвяжный", "манда", "мандавошка", "мандей", "мандеть",
    "мандища", "мандюк", "минет", "минетчик", "минетчица", "мокрохвостка", "мокрощелка", "мудак", "муде",
    "мудеть", "мудила", "мудистый", "мудня", "мудоеб", "мудозвон", "муйня", "набздеть", "наговнять", "надристать",
    "надрочить", "наебать", "наебнуться", "наебывать", "нассать", "нахезать", "нахуйник", "насцать", "обдристаться",
    "обдристаться", "обосранец", "обосрать", "обосцать", "обосцаться", "обсирать", "опизде", "отпиздячить",
    "отпороть", "отъеть", "охуевательский", "охуевать", "охуевающий", "охуеть", "охуительный", "охуячивать",
    "охуячить", "педрик", "пердеж", "пердение", "пердеть", "пердильник", "перднуть", "пердун", "пердунец",
    "пердунина", "пердунья", "пердуха", "пердь", "передок", "пернуть", "пидор", "пизда", "пиздануть", "пизденка",
    "пиздеть", "пиздить", "пиздища", "пиздобратия","профиль", "профель", "приватка", "приват", "пиздоватый", "пиздорванец", "пиздорванка", "пиздострадатель",
    "пиздун", "пиздюга", "пиздюк", "пиздячить", "писять", "питишка", "плеха", "подговнять", "подъебнуться",
    "поебать", "поеть", "попысать", "посрать", "поставить", "поцоватый", "презерватив", "проблядь", "проебать",
    "промандеть", "промудеть", "пропиздеть", "пропиздячить", "пысать", "разъеба", "разъебай", "распиздай",
    "распиздеться", "распиздяй", "распроеть", "растыка", "сговнять", "секель", "серун", "серька", "сика",
    "сикать", "сикель", "сирать", "сирывать", "скурвиться", "скуреха", "скурея", "скуряга", "скуряжничать",
    "спиздить", "срака", "сраный", "сранье", "срать", "срун", "ссака", "ссаки", "ссать", "старпер", "струк",
    "суходрочка", "сцавинье", "сцака", "сцаки", "сцание", "сцать", "сциха", "сцуль", "сцыха", "сыкун",
    "титечка", "титечный", "титка", "титочка", "титька", "трипер", "триппер", "уеть", "усраться", "усцаться",
    "фик", "фуй", "хезать", "хер", "херня", "херовина", "херовый", "хитрожопый", "хлюха", "хуевина", "хуевый",
    "хуек", "хуепромышленник", "хуерик", "хуесос", "хуище", "хуй", "хуйня", "хуйрик", "хуякать", "хуякнуть",
    "целка", "шлюха"
]
def check_message(message):
    for word in bad_words:
        if word in message.text.lower():
            return True
    return False


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if check_message(message):
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"Сообщение от пользователя {message.from_user.username} было удалено из чата за использование запрещенных слов")
    else:
        print(message.text)

bot.infinity_polling(none_stop=True)

