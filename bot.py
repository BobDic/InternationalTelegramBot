import telebot
from telebot import *

ADMISSION_BAC = [
    'В 2021 году объявлен приём по следующим направлениям подготовки уровня бакалавриат и специалитет'
    'очной / заочной / очно-заочной формы обучения бюджетные и внебюджетные (платные) места:'
    '\n \nhttps://narfu.ru/entrant/bachelor/perechen-napravleniy/',  # 1
    'ДОПОЛНИТЬ!',  # 2
    'Обращаем Ваше внимание, что претендовать на бюджетные места имеют право иностранные граждане, подтвердившие свой'
    'статус соотечественника. \n\nКоличество бюджетных мест: https://narfu.ru/entrant/bachelor/kolichestvo-mest/',  # 3
    'Окончание приема документов: 10 июля 2021 г.Списки поступающих: 27 июля 2021 г. \nОкончание приема заявления о'
    'согласии на зачисление: 3 августа 2021 г.\n Зачисление: 5 августа 2021'
    'г.\n\nhttps://narfu.ru/entrant/bachelor/sroki-priema/',  # 4
    'Вступительные испытания для каждого направления подготовки размещены:'
    '\nhttps://narfu.ru/entrant/bachelor/vstupitelnye-ispytaniya/',  # 5
    'На этой странице вы можете узнать, какими были проходные баллы по общему конкурсу в 2013-2020 гг. Прочерк '
    'означает, что прием на данное направление подготовки в указанном году не осуществлялся. \n\nПроходной балл – это '
    'сумма баллов по трем вступительным испытаниям, с которой был зачислен абитуриент, на последнее бюджетное место в '
    'конкретном году. Значение проходного балла не является постоянным, оно меняется каждый год в зависимости от '
    'количества бюджетных мест и количества абитуриентов, а также качества их знаний. \nПричем, проходной балл может '
    'увеличиваться или уменьшаться. \n\nПроходной балл становится известен только после окончания зачисления '
    'абитуриентов '
    '(после издания приказов о зачислении). Таким образом проходные баллы в 2021 г. на все направления подготовки ('
    'специальности) будут известны только после зачисления! \n\nПроходные баллы прошлых лет: '
    'https://narfu.ru/entrant/bachelor/priyem-proshlykh/',  # 6
    'Зарегистрируйтесь в форме и наши сотрудники свяжутся с Вами:'
    '\nhttps://docs.google.com/forms/d/e/1FAIpQLSdVTlJP43BCJSe-xMOgNCvGsVgD5yOBnulwi-LzGJgGCKWWtQ/viewform'  # 7
]

ADMISSION_MAG = [
    'В 2021 году объявлен приём по следующим направлениям подготовки уровня магистратура очной / заочной / '
    'очно-заочной формы '
    'обучения бюджетные и внебюджетные (платные) места: \nhttps://narfu.ru/entrant/magistr/perechen-napravleniy/ ',
    'ДОПОЛНИТЬ!',
    'Обращаем Ваше внимание, что претендовать на бюджетные места имеют право иностранные граждане, подтвердившие свой '
    'статус соотечественника. \n\nhttps://narfu.ru/entrant/magistr/kolichestvo-mest/',
    'Окончание приема документов: 14 августа 2021 г. \nСписки поступающих: 21 августа 2021 г. \nОкончание приема '
    'заявления о согласии на зачисление: 25 августа 2021 г. \nЗачисление 26 августа 2021 г.',
    'Вступительные испытания для каждого направления подготовки размещены:   '
    '\nhttps://narfu.ru/entrant/magistr/vstupitelnye-ispytaniya/ ',
    'На этой странице вы можете узнать, какими были проходные баллы по общему конкурсу в 2013-2020 гг. Прочерк '
    'означает, что прием на данное направление подготовки в указанном году не осуществлялся. \n\nПроходной балл – это '
    'сумма баллов по трем вступительным испытаниям, с которой был зачислен абитуриент, на последнее бюджетное место в '
    'конкретном году. Значение проходного балла не является постоянным, оно меняется каждый год в зависимости от '
    'количества бюджетных мест и количества абитуриентов, а также качества их знаний. \nПричем, проходной балл может '
    'увеличиваться или уменьшаться. \n\nПроходной балл становится известен только после окончания зачисления '
    'абитуриентов '
    '(после издания приказов о зачислении). Таким образом проходные баллы в 2021 г. на все направления подготовки ('
    'специальности) будут известны только после зачисления! \n\nПроходные баллы прошлых лет: '
    'https://narfu.ru/entrant/magistr/priyem-proshlykh/',
    'Зарегистрируйтесь в форме и наши сотрудники свяжутся с Вами:'
    '\nhttps://docs.google.com/forms/d/e/1FAIpQLSdVTlJP43BCJSe-xMOgNCvGsVgD5yOBnulwi-LzGJgGCKWWtQ/viewform'
]

ADMISSION_ASP = [
    'Аспирантура является третьей ступенью высшего образования и предполагает подготовку научно-педагогических кадров '
    'высшей квалификации. \nПо окончании лицам, успешно прошедшим государственную итоговую аттестацию, '
    'выдается документ об образовании с присвоением квалификации «Исследователь. '
    'Преподаватель-исследователь».\n\nЛицам, '
    'окончившим аспирантуру и защитившим в установленном порядке диссертацию на соискание ученой степени кандидата '
    'наук, присваивается ученая степень кандидата наук по соответствующей специальности и выдается диплом кандидата '
    'наук.\n\n https://narfu.ru/entrant/aspirantura/priemKolMest/',
    'Окончание приема документов: 7 августа 2021 г. \nОкончание приема заявления о согласии на зачисление: 26 августа'
    '2021 г. \nЗачисление: 27 августа 2021 г. ',
    'Программы вступительных испытаний в аспирантуру по специальным дисциплинам (прием 2021 г.) \n\n'
    'https://narfu.ru/entrant/aspirantura/vstupitelnye-ispytaniya/',
    'Учет индивидуальных достижений осуществляется посредством начисления баллов в соответствии с «Перечнем '
    'показателей индивидуальных достижений поступающих». Указанные баллы начисляются поступающему, представившему '
    'документы, подтверждающие индивидуальные достижения, и включаются в сумму конкурсных баллов. \n\nПеречень '
    'показателей индивидуальных достижений поступающих на программы аспирантуры:\n '
    'https://narfu.ru/entrant/aspirantura/uchet_dostizheniy/ ',
    'На этой странице вы можете узнать, какими были проходные баллы по общему конкурсу в 2015-2020 гг. Прочерк '
    'означает, что прием на данное направление подготовки в указанном году не осуществлялся. \n\nПроходной балл — это '
    'балл абитуриента, зачисленного на последнее бюджетное место в конкретном году. \nЗначение проходного балла не '
    'является постоянным, оно меняется каждый год в зависимости от количества бюджетных мест и количества '
    'абитуриентов. Проходной балл может увеличиваться или уменьшаться. \nПроходной балл становится известен только '
    'после окончания зачисления абитуриентов (после издания приказов о зачислении). Таким образом проходные баллы в '
    '2021 г. на все направления подготовки (специальности) будут известны только после зачисления! '
    '\n\nhttps://narfu.ru/entrant/aspirantura/priyem-proshlykh/ '
]

ADMISSION_COL = [
    'В 2021 году объявлен приём по следующим направлениям подготовки уровня СПО очной / заочной / очно-заочной формы '
    'обучения бюджетные и внебюджетные (платные) места. \n\nhttps://narfu.ru/entrant/spo/perechen/ ',
    'Прием граждан в университет для обучения по программам среднего профессионального образования (СПО) '
    'осуществляется по заявлениям лиц, имеющим основное общее образование или среднее общее образование. \n\nПрием на '
    'обучение по образовательным программам СПО осуществляется на основе результатов освоения поступающими '
    'образовательной программы основного общего или среднего общего образования, указанных в представленных '
    'поступающими документах об образовании. ',
    'https://narfu.ru/entrant/spo/kolichestvo-mest/',
    'Окончание приема документов: 25 августа 2021 г.\nОкончание приема заявления о согласии на зачисление: 27 августа'
    '2021 г.\nЗачисление: 28 августа 2021 г. '
]

ADMISSION_ESLE = [
    'Подготовительное отделение для иностранных граждан Высшей школы социально-гуманитарных наук и международной '
    'коммуникации обеспечивает подготовку иностранных граждан и лиц без гражданства к освоению профессиональных '
    'образовательных программ бакалавриата, специалитета, магистратуры, аспирантуры на русском языке. \n\nУчебный план '
    'подготовительного отделения для иностранных граждан (2020-2021 учебный год)\n'
    'https://narfu.ru/international/international_entrants/entrance/pre-training/napravleniya/ ',
    'Начало обучения: сентябрь 2020 г. (осенний семестр).\n Срок обучения: 10 месяцев. \nСтоимость обучения: 105 610 '
    'рублей / год (2020/2021 учебный год).\n Язык обучения: русский. ',
    'https://docs.google.com/forms/d/e/1FAIpQLSdVTlJP43BCJSe-xMOgNCvGsVgD5yOBnulwi-LzGJgGCKWWtQ/viewform',
    'Для поступления на подготовительное отделение, слушатель должен предоставить по адресу '
    'электронной почты - international@narfu.ru следующие документы: \n\n • Анкета-заявка \n• Копия паспорта * \n• Копия '
    'легализованного документа об образовании * \n• Медицинская справка * \n• 2 фотографии 3 см х 4 см \n\n* Документы '
    'должны быть переведены на русский язык и заверены у нотариуса. \n\nВнимание! По прибытии в Российскую Федерацию '
    'иностранный гражданин обязан оформить медицинскую страховку на срок не менее 10 месяцев. '
]

ARRIVAL_ARH = [
    'Добраться до Архангельска можно маршрутом через Москву или Санкт-Петербург самолетом или поездом. \nАвиасообщение:'
    'Время в пути составляет приблизительно 1,5 часа. Забронировать и выкупить билеты можно на сайте авиакомпании '
    'Nordavia или Аэрофлот. \nЖелезнодорожный транспорт: Время в пути составляет приблизительно 22 часа. Купить билеты '
    'можно на сайте РЖД или в железнодорожных кассах.\nСразу после покупки билетов, пожалуйста, сообщите точную дату и '
    'время Вашего приезда в Архангельск для организации Вашей встречи: \n\nпо электронной почте: international@narfu.ru'
    '\nпо телефонам: +7 (8182) 21-89-27, +7 (8182) 21-61-96.',
    'Если Вы предпочтете добраться до САФУ самостоятельно - используйте следующие ориентиры: \n\nАдрес главного корпуса'
    'университета: \nАрхангельск, набережная Северной Двины, 17, Управление международного сотрудничества, офис 1326а '
    '\n\nМаршрут: \n\n- такси (стоимость 300 рублей), автобус № 12 до остановки «Морской речной вокзал» (стоимость 28 '
    'рублей). \n- железнодорожного вокзала — такси (100-120 рублей), автобус № 1, 54, 76 до остановки «Морской речной '
    'вокзал» (стоимость 26 рублей). \n\nТелефоны такси: +7 (8182) 219-219, +7 (8182) 280-000 ',
    'Адреса общежитий и стоимость проживания: \nhttps://narfu.ru/life/campus/oplata-prozhivaniya-v-obshchezhitii/',
    'В случае, если у Вас нет справки о прохождении флюорографии, справки о чистых кожных покровах (на русском '
    'языке или с переводом), то пройти медицинский осмотр можно в Архангельской городской поликлинике № 2 по адресу: '
    'ул. Северодвинская, 16 (примерная стоимость осмотра составляет 700 рублей). \n\nДоговор на заселение в общежитии '
    'оформляется в Дирекции студенческого городка по адресу: ул. Красноармейская, 2. \n\nОплата проживания в общежитии '
    'производится в кассе по адресу: ул. Красноармейская, 2. \n\nВАЖНО! \n\nПосле заселения в общежитие документы на '
    'регистрацию иностранного гражданина (миграционная карта, 2 копии миграционной карты, 2 копии визы, '
    '2 копии паспорта) предоставляются по адресу: набережная Северной Двины, 17, Управление международного '
    'сотрудничества, Отдел визовой поддержки и регистрации, офис 1326а. \nЧерез 3-5 рабочих дней оформленные документы '
    'можно получить назад. ',
    'Вещи: \n\nОдежда: Советуем взять, в первую очередь, теплые вещи, поскольку в осенний период в Архангельске бывает '
    'холодно и дождливо. \n\nТехника: для Вашего удобства и в целях подготовки к учебным занятиям рекомендуем взять с '
    'собой ноутбук / планшет. Однако, если такой возможности нет, то в САФУ работает Научная библиотека, '
    'в которой предусмотрены компьютерные классы для самостоятельных занятий. \n\n!  Все необходимые магазины, аптеки, '
    'банки и т.д. находятся в шаговой доступности от общежитий. '
]

VISA_ACC = [
    'Для постановки иностранных граждан на миграционный учет по месту пребывания университету по закону отводится 7 '
    'дней.\n\nОбязательно сохраняйте билеты до Архангельска!\n\nПо приезду в Архангельск следует в ближайший рабочий '
    'день обратиться в отдел по работе с иностранными партнерами (далее-ОРИП УМС) (Главный корпус САФУ, Набережная '
    'Северной Двины, д. 17, 3 этаж, каб.1-326а)',
    '— Национальный паспорт, по которому въезжали в РФ — в подлиннике и ксерокопии всех страниц паспорта.\n\n— Оригинал'
    'и копия миграционной карты (документ, который выдается при пересечении границы Российской Федерации). \n\n— '
    'Прибывшие в САФУ в первый раз — делают дополнительно копии: страницы паспорта с фото, действующей визы и '
    'миграционной карты в 2-х экз. ; один экземпляр заверяют в ОРиП УМС и оставляют себе, другой предоставляют в ОРиП '
    'УМС для оформления личного дела. \n\nПосле постановки на миграционный учет иностранный гражданин получает на руки '
    'отрывную часть уведомления о постановке на миграционный учет. ',
    'При любом выезде из г. Архангельска (на каникулы, на практику или по другой причине в течение учебного года) '
    'студенты должны обязательно проинформировать сотрудников отдела по работе с иностранными партнерами. При выписке '
    'из лечебного учреждения также необходимо поставить в известность сотрудников указанного отдела для оформления '
    'необходимых документов в ближайший рабочий день с предоставлением отрывной части уведомления о прибытии '
    'иностранного гражданина к месту временного пребывания по юридическому адресу лечебного учреждения и её копии. ',
    'За несоблюдение требований миграционного законодательства предусмотрена административная ответственность в '
    'отношении иностранного гражданина, должностных лиц, юридического лица (см. статьи 18.8-18.10 Кодекса Российской '
    'Федерации об административных правонарушениях).\n\n В настоящее время штраф за несоблюдение норм миграционного '
    'законодательства составляет от 2000 до 5000 рублей на физическое лицо, от 40000 до 50000 рублей на должностное '
    'лицо, от 400000 до 500000 рублей на юридическое лицо. \n\nПри наличии двух и более зарегистрированных '
    'административных правонарушений возможно ограничение въезда (запрет на въезд) в Российскую Федерацию на срок от '
    'трёх до пяти лет. ',
    'Просим вас своевременно сообщать в отдел по работе с иностранными партнёрами о любых изменениях в вашей '
    'контактной информации.\n\nЕсли Вы госпитализированы в больницу, обязательно сообщите об этом по телефону: '
    '21-89-27, либо 21-89-68.После выписки явка в каб. 1326-а в ближайший рабочий день обязательна. \n\nВ случае '
    'намечающегося отъезда из Архангельска, в том числе в пределах Российской Федерации, после бронирования билетов '
    'сообщите о дате выезда по телефону 21-89-27 либо по эл. почте n.juzhanina@narfu.ru; v.kareljskaya@narfu.ru\n\n '
    'По приезде в Архангельск в ближайший рабочий день необходимо обязательно подойти в каб. 1326-а для повторной '
    'постановки на миграционный учёт либо проверки необходимости повторной постановки на миграционный учёт. '
    'Постановка на миграционный учёт обязательна каждый раз после пересечения границы российской федерации, '
    'после получения новой миграционной карты, после пребывания в гостиницах, хостелах, базах отдыха, санаториях и '
    'больницах. '
]

VISA_CARD = [
    'Миграционная карта является важнейшим документом для иностранного гражданина. Ни в коем случае не приобретайте '
    'ее с рук сомнительных лиц, она выдается бесплатно при пересечении границы Российской Федерации. \nПокупка '
    'миграционной карты с рук у сомнительных лиц (на вокзалах или через объявления) является серьезным '
    'правонарушением, влекущим за собой ответственность вплоть до уголовной. \nОбращаем ваше внимание на то, '
    'что подлинность миграционной карты выявляется при занесении данных в электронную базу УФМС (по серии и номеру '
    'миграционной карты), и при проверке на специальном оборудовании, так что незаконно полученная миграционная карта '
    'будет выявлена. \nЗаполните  согласно инструкции. Не забудьте подчеркнуть цель въезда: для студентов — учеба, '
    'для преподавателей и партнеров — служебная, при наличии рабочей визы — рабочая. Обязательно напишите, '
    'что приглашающая сторона — САФУ (для заполняющих на английском языке- NArFU). \nВыданную Вам при пересечении '
    'границы миграционную карту вложите в паспорт, ни в коем случае не потеряйте и не выбрасывайте ее! Штамп на '
    'обратной стороне миграционной карты является свидетельством легальности Вашего пребывания в РФ. Если так '
    'случилось, что Вы потеряли миграционную карту, Вам придется вместе с сотрудником отдела визовой поддержки и '
    'регистрации Управления международного сотрудничества (кабинет 1326-а Главного корпуса САФУ) проехать в УФМС '
    'России по Архангельской области и написать заявление о выдаче дубликата, возможно, придется уплатить штраф. '
    '\nСсылка на инструкцию:\n https://narfu.ru/upload/medialibrary/8a5/20110712_165337.pdf '
]

CONTACTS = [
    'intenational@narfu.ru\n +7 8182 216 196 \nВК САФУ/NArFU International: \nhttps://vk.com/narfuinternational \n'
    'Whatsapp | Viber | Telegram: \n+7 952 250 3827 \nInstagram: narfu_international '
]

TOKEN = '1460604666:AAE0oASwac6RJzbReQ69iqd-UAP7LcRnczg'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Поступление", callback_data="admission")
    btn2 = types.InlineKeyboardButton(text="Приезд", callback_data="arrival")
    btn3 = types.InlineKeyboardButton(text="Визовая поддержка", callback_data="visa")
    btn4 = types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Здравствуй, это начальное окно бота, выбери, что тебе интересно",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
# Обработка невалидного текстового сообщения пользователя и перенаправление на /start
def message_from_user(message):
    bot.send_message(message.chat.id,
                     "Команда не поддерживается.\nДля начала работы введите '/start'.")


def send_admission(message):
    # Создание и отправка клавиатуры с возможностью выбора места поступления
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Бакалавриат/Специалитет", callback_data="adm_1")
    btn2 = types.InlineKeyboardButton(text="Магистратура", callback_data="adm_2")
    btn3 = types.InlineKeyboardButton(text="Аспирантура", callback_data="adm_3")
    btn4 = types.InlineKeyboardButton(text="Колледж", callback_data="adm_4")
    btn5 = types.InlineKeyboardButton(text="Подготовительное отделение", callback_data="adm_5")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='start')
    markup.add(btn1, btn2, btn3, btn4, btn5, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении",
                     reply_markup=markup)


def send_arrival(message):
    # Создание и отправка клавиатуры с возможностью выбора информации о приезде
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Как добраться до Архангельска?", callback_data="arv_1")
    btn2 = types.InlineKeyboardButton(text="Как добраться до САФУ?", callback_data="arv_2")
    btn3 = types.InlineKeyboardButton(text="Общежития", callback_data="arv_3")
    btn4 = types.InlineKeyboardButton(text="Как происходит заселение в общежитие?", callback_data="arv_4")
    btn5 = types.InlineKeyboardButton(text="Необходимые вещи", callback_data="arv_5")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='start')
    markup.add(btn1, btn2, btn3, btn4, btn5, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о приезде",
                     reply_markup=markup)


def send_visa(message):
    # Создание и отправка клавиатуры с возможностью информации о миграции
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Миграционный учет", callback_data="visa_1")
    btn2 = types.InlineKeyboardButton(text="Миграционная карта", callback_data="visa_2")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='start')
    markup.add(btn1, btn2, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о визе",
                     reply_markup=markup)


def send_admission_bacalavr(message):
    # Создание и отправка клавиатуры с возможностью подменю для бакалавриата
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Направления подготовки", callback_data="adm_bac_1")
    btn2 = types.InlineKeyboardButton(text="Пакет документов", callback_data="adm_bac_2")
    btn3 = types.InlineKeyboardButton(text="Количество бюджетных мест", callback_data="adm_bac_3")
    btn4 = types.InlineKeyboardButton(text="Сроки приемной кампании САФУ", callback_data="adm_bac_4")
    btn5 = types.InlineKeyboardButton(text="Вступительные испытания", callback_data="adm_bac_5")
    btn6 = types.InlineKeyboardButton(text="Проходные баллы прошлых лет", callback_data="adm_bac_6")
    btn7 = types.InlineKeyboardButton(text="Подать заявку на консультацию ", callback_data="adm_bac_7")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='admission')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении в бакалавриат",
                     reply_markup=markup)


def send_admission_magistr(message):
    # Создание и отправка клавиатуры с возможностью подменю для магистратуры
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Направления подготовки", callback_data="adm_mag_1")
    btn2 = types.InlineKeyboardButton(text="Пакет документов", callback_data="adm_mag_2")
    btn3 = types.InlineKeyboardButton(text="Количество бюджетных мест", callback_data="adm_mag_3")
    btn4 = types.InlineKeyboardButton(text="Сроки приемной кампании САФУ", callback_data="adm_mag_4")
    btn5 = types.InlineKeyboardButton(text="Вступительные испытания", callback_data="adm_mag_5")
    btn6 = types.InlineKeyboardButton(text="Проходные баллы прошлых лет", callback_data="adm_mag_6")
    btn7 = types.InlineKeyboardButton(text="Подать заявку на консультацию ", callback_data="adm_mag_7")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='admission')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении в магистратуру",
                     reply_markup=markup)


def send_admission_aspirant(message):
    # Создание и отправка клавиатуры с возможностью подменю для магистратуры
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Направления подготовки и количество бюджетных мест",
                                      callback_data="adm_asp_1")
    btn2 = types.InlineKeyboardButton(text="Сроки приемной кампании САФУ", callback_data="adm_asp_2")
    btn3 = types.InlineKeyboardButton(text="Программы вступительных испытаний", callback_data="adm_asp_3")
    btn4 = types.InlineKeyboardButton(text="Индивидуальные достижения", callback_data="adm_asp_4")
    btn5 = types.InlineKeyboardButton(text="Проходные баллы прошлых лет", callback_data="adm_asp_5")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='admission')
    markup.add(btn1, btn2, btn3, btn4, btn5, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении в аспирантуру",
                     reply_markup=markup)


def send_admission_college(message):
    # Создание и отправка клавиатуры с возможностью подменю для магистратуры
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Направления подготовки", callback_data="adm_col_1")
    btn2 = types.InlineKeyboardButton(text="Перечень документов", callback_data="adm_col_2")
    btn3 = types.InlineKeyboardButton(text="Количество бюджетных мест", callback_data="adm_col_3")
    btn4 = types.InlineKeyboardButton(text="Сроки приемной кампании", callback_data="adm_col_4")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='admission')
    markup.add(btn1, btn2, btn3, btn4, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении в колледж",
                     reply_markup=markup)


def send_admission_else(message):
    # Создание и отправка клавиатуры с возможностью подменю для подготовительного отделения
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Направления подготовки", callback_data="adm_else_1")
    btn2 = types.InlineKeyboardButton(text="Сроки обучения и стоимость", callback_data="adm_else_2")
    btn3 = types.InlineKeyboardButton(text="Анкета-заявка", callback_data="adm_else_3")
    btn4 = types.InlineKeyboardButton(text="Пакет документов", callback_data="adm_else_4")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='admission')
    markup.add(btn1, btn2, btn3, btn4, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о поступлении в подготовительное отделение",
                     reply_markup=markup)


def send_visa_accounting(message):
    # Создание и отправка клавиатуры с возможностью подменю для миграционного учета
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Постановка на миграционный учет", callback_data="visa_acc_1")
    btn2 = types.InlineKeyboardButton(text="Пакет документов", callback_data="visa_acc_2")
    btn3 = types.InlineKeyboardButton(text="Снятие с учета", callback_data="visa_acc_3")
    btn4 = types.InlineKeyboardButton(text="Административная ответственность", callback_data="visa_acc_4")
    btn5 = types.InlineKeyboardButton(text="Контакты", callback_data="visa_acc_5")
    backBtn = types.InlineKeyboardButton(text='Назад', callback_data='visa')
    markup.add(btn1, btn2, btn3, btn4, btn5, backBtn)
    bot.send_message(message.chat.id, "Окно с информацией о миграционном учете",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == 'start':
        send_welcome(call.message)

    # Обработка нажатия кнопки из основного (приветственного) окна
    elif call.data == 'admission':
        send_admission(call.message)
    elif call.data == 'arrival':
        send_arrival(call.message)
    elif call.data == 'visa':
        send_visa(call.message)
    elif call.data == 'contacts':
        bot.send_message(call.message.chat.id, CONTACTS[0])

    # Обработка нажатия кнопки из поступления
    elif call.data == 'adm_1':
        send_admission_bacalavr(call.message)
    elif call.data == 'adm_2':
        send_admission_magistr(call.message)
    elif call.data == 'adm_3':
        send_admission_aspirant(call.message)
    elif call.data == 'adm_4':
        send_admission_college(call.message)
    elif call.data == 'adm_5':
        send_admission_else(call.message)

    # Обработка нажатия кнопки из визовой поддержки
    elif call.data == 'visa_1':
        send_visa_accounting(call.message)
    elif call.data == 'visa_2':
        bot.send_message(call.message.chat.id, VISA_CARD[0])

    # Обработка нажатия кнопки из подменю бакалавриата
    elif call.data == 'adm_bac_1':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[0])
    elif call.data == 'adm_bac_2':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[1])
    elif call.data == 'adm_bac_3':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[2])
    elif call.data == 'adm_bac_4':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[3])
    elif call.data == 'adm_bac_5':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[4])
    elif call.data == 'adm_bac_6':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[5])
    elif call.data == 'adm_bac_7':
        bot.send_message(call.message.chat.id, ADMISSION_BAC[6])

    # Обработка нажатия кнопки из подменю магистратуры
    elif call.data == 'adm_mag_1':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[0])
    elif call.data == 'adm_mag_2':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[1])
    elif call.data == 'adm_mag_3':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[2])
    elif call.data == 'adm_mag_4':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[3])
    elif call.data == 'adm_mag_5':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[4])
    elif call.data == 'adm_mag_6':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[5])
    elif call.data == 'adm_mag_7':
        bot.send_message(call.message.chat.id, ADMISSION_MAG[6])

    # Обработка нажатия кнопки из подменю аспирантуры
    elif call.data == 'adm_asp_1':
        bot.send_message(call.message.chat.id, ADMISSION_ASP[0])
    elif call.data == 'adm_asp_2':
        bot.send_message(call.message.chat.id, ADMISSION_ASP[1])
    elif call.data == 'adm_asp_3':
        bot.send_message(call.message.chat.id, ADMISSION_ASP[2])
    elif call.data == 'adm_asp_4':
        bot.send_message(call.message.chat.id, ADMISSION_ASP[3])
    elif call.data == 'adm_asp_5':
        bot.send_message(call.message.chat.id, ADMISSION_ASP[4])

    # Обработка нажатия кнопки из подменю колледжа
    elif call.data == 'adm_col_1':
        bot.send_message(call.message.chat.id, ADMISSION_COL[0])
    elif call.data == 'adm_col_2':
        bot.send_message(call.message.chat.id, ADMISSION_COL[1])
    elif call.data == 'adm_col_3':
        bot.send_message(call.message.chat.id, ADMISSION_COL[2])
    elif call.data == 'adm_col_4':
        bot.send_message(call.message.chat.id, ADMISSION_COL[3])

    # Обработка нажатия кнопки из подменю колледжа
    elif call.data == 'adm_else_1':
        bot.send_message(call.message.chat.id, ADMISSION_ESLE[0])
    elif call.data == 'adm_else_2':
        bot.send_message(call.message.chat.id, ADMISSION_ESLE[1])
    elif call.data == 'adm_else_3':
        bot.send_message(call.message.chat.id, ADMISSION_ESLE[2])
    elif call.data == 'adm_else_4':
        bot.send_message(call.message.chat.id, ADMISSION_ESLE[3])

    # Обработка нажатия кнопки из подменю приезд
    elif call.data == 'arv_1':
        bot.send_message(call.message.chat.id, ARRIVAL_ARH[0])
    elif call.data == 'arv_2':
        bot.send_message(call.message.chat.id, ARRIVAL_ARH[1])
    elif call.data == 'arv_3':
        bot.send_message(call.message.chat.id, ARRIVAL_ARH[2])
    elif call.data == 'arv_4':
        bot.send_message(call.message.chat.id, ARRIVAL_ARH[3])

    # Обработка нажатия кнопки из подменю миграционный учет
    elif call.data == 'visa_acc_1':
        bot.send_message(call.message.chat.id, VISA_ACC[0])
    elif call.data == 'visa_acc_2':
        bot.send_message(call.message.chat.id, VISA_ACC[1])
    elif call.data == 'visa_acc_3':
        bot.send_message(call.message.chat.id, VISA_ACC[2])
    elif call.data == 'visa_acc_4':
        bot.send_message(call.message.chat.id, VISA_ACC[3])
    elif call.data == 'visa_acc_5':
        bot.send_message(call.message.chat.id, VISA_ACC[4])


if __name__ == '__main__':
    bot.polling()
