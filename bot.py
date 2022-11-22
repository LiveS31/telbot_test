# code bot
from typing import Any
import telebot

fca = telebot.TeleBot('token')
codes = ''
errors = {'P0016': 'Синхронизация коленчатого вала/ распределительного вала. (Обнаружена погрешность позиционирования распределительного вала:нет совладения по фазе с коленчатым валом.)',
         'P01XX': 'Измерители топлива и воздуха',
         'P0100': 'Неисправность цепи датчика расхода воздуха',
         'P0101': 'Выход сигнала из допустимого диапазона',
         'P0102': 'Низкий уровень выходного сигнала',
         'P0103': 'Высокий уровень выходного сигнала',
         'P0105': 'Неисправность датчика давления воздуха',
         'P0106': 'Выход сигнала из допустимого диапазона',
         'P0107': 'Низкий уровень выходного сигнала',
         'P0108': 'Высокий уровень выходного сигнала',
         'P0110': 'Неисправность датчика температуры всасываемого воздуха',
         'P0111': 'Выход сигнала из допустимого диапазона',
         'P0112': 'Низкий уровень выходного сигнала',
         'P0113': 'Высокий уровень выходного сигнала',
         'P0115': 'Неисправность датчика температуры охлаждающей жидкости',
         'P0116': 'Выход сигнала из допустимого диапазона',
         'P0117': 'Низкий уровень выходного сигнала',
         'P0118': 'Высокий уровень выходного сигнала',
         'P0120': 'Неисправность датчика положения дроссельной заслонки',
         'P0121': 'Выход сигнала из допустимого диапазона',
         'P0122': 'Низкий уровень выходного сигнала',
         'P0123': 'Высокий уровень выходного сигнала',
         'P0125': 'Низкая температуры охлаждающей жид. для упр.по замкн.контуру',
         'P0130': 'Датчик О2 В1 S1 несправен(Банк1)',
         'P0131': 'Датчик О2 В1 S1 имеет низкий уровень сигнала',
         'P0132': 'Датчик О2 В1 S1 имеет высокий уровень сигнала',
         'P0133': 'Датчик О2 В1 S1 имеет медленный отклик на обогащение/обеднение',
         'P0134': 'Цепь датчика О2 В1 S1 пассивна',
         'P0135': 'Нагреватель датчика О2 В1 S1 несправен',
         'P0136': 'Датчик О2 В1 S2 несправен',
         'P0137': 'Датчик О2 В1 S2 имеет низкий уровень сигнала',
         'P0138': 'Датчик О2 В1 S2 имеет высокий уровень сигнала',
         'P0139': 'Датчик О2 В1 S2 имеет медленный отклик на обогащение/обеднение',
         'P0140': 'Цепь датчика О2 В1 S2 пассивна',
         'P0141': 'Нагреватель датчика О2 В1 S2 несправен',
         'P0142': 'Датчик О2 В1 S3 несправен',
         'P0143': 'Датчик О2 В1 S3 имеет низкий уровень сигнала',
         'P0144': 'Датчик О2 В1 S3 имеет высокий уровень сигнала',
         'P0145': 'Датчик О2 В1 S3 имеет медленный отклик на обогащение/обеднение',
         'P0146': 'Цепь датчика О2 В1 S3 пассивна',
         'P0147': 'Нагреватель датчика О2 В1 S3 несправен',
         'P0150': 'Датчик О2 В2 S1 несправен (Банк2)',
         'P0151': 'Датчик О2 В2 S1 имеет низкий уровень сигнала',
         'P0152': 'Датчик О2 В2 S1 имеет высокий уровень сигнала',
         'P0153': 'Датчик О2 В2 S1 имеет медленный отклик на обогащение/обеднение',
         'P0154': 'Цепь датчика О2 В2 S1 пассивна',
         'P0155': 'Нагреватель датчика О2 В2 S1 несправен',
         'P0156': 'Датчик О2 В2 S2 несправен',
         'P0157': 'Датчик О2 В2 S2 имеет низкий уровень сигнала',
         'P0158': 'Датчик О2 В2 S2 имеет высокий уровень сигнала',
         'P0159': 'Датчик О2 В2 S2 имеет медленный отклик на обогащение/обеднение',
         'P0160': 'Цепь датчика О2 В2 S2 пассивна',
         'P0161': 'Нагреватель датчика О2 В2 S2 несправен',
         'P0162': 'Датчик О2 В2 S3 несправен',
         'P0163': 'Датчик О2 В2 S3 имеет низкий уровень сигнала',
         'P0164': 'Датчик О2 В2 S3 имеет высокий уровень сигнала',
         'P0165': 'Датчик О2 В2 S3 имеет медленный отклик на обогащение/обеднение',
         'P0166': 'Цепь датчика О2 В2 S3 пассивна',
         'P0167': 'Нагреватель датчика О2 В2 S3 несправен',
         'P0170': 'Утечка топлива из топливной системы блока №1',
         'P0171': 'Блок цилиндров №1 беднит (возможно подсос воздуха)',
         'P0172': 'Блок цилиндров №1 богатит (возможно неполное закрытие форсунки)',
         'P0173': 'Утечка топлива из топливной системы блока №2',
         'P0174': 'Блок цилиндров №2 беднит (возможно подсос воздуха)',
         'P0175': 'Блок цилиндров №2 богатит (возможно неполное закрытие форсунки)',
         'P0176': 'Датчик выброса СНх неисправен',
         'P0177': 'Сигнал датчика выходит из допустимого диапазона',
         'P0178': 'Низкий уровень сигнала датчика СНх',
         'P0179': 'Высокий уровень сигнала датчика СНх',
         'P0180': 'Цепь датчика температуры топлива «А» неисправна',
         'P0181': 'Сигнал датчика «А» выходит из допустимого диапазона',
         'P0182': 'Низкий сигнал датчика температуры топлива «А»',
         'P0183': 'Высокий сигнал датчика температуры топлива «А»',
         'P0185': 'Цепь датчика температуры топлива «В» неисправна',
         'P0186': 'Сигнал датчика «В» выходит из допустимого диапазона',
         'P0187': 'Низкий сигнал датчика температуры топлива «В»',
         'P0188': 'Высокий сигнал датчика температуры топлива «В»',
         'P0190': 'Цепь датчика давления топлива в топливной рампе неисправна',
         'P0191': 'Сигнал датчика выходит из допустимого диапазона',
         'P0192': 'Низкий сигнал датчика давления топлива',
         'P0193': 'Высокий сигнал датчика давления топлива',
         'P0194': 'Сигнал датчика давления топлива перемежающийся',
         'P0195': 'Цепь датчика температуры масла в двигателе неисправна',
         'P0196': 'Сигнал датчика выходит из допустимого диапазона',
         'P0197': 'Низкий сигнал датчика температуры масла',
         'P0198': 'Высокий сигнал датчика температуры масла',
         'P0199': 'Сигнал датчика температуры масла перемежающийся',
         'P02XX': 'FUEL AND AIR METERING',
         'P0200': 'Цепь управления форсункой неисправна',
         'P0201': 'Цепь управления форсункой цилиндра №1 неисправна',
         'P0202': 'Цепь управления форсункой цилиндра №2 неисправна',
         'P0203': 'Цепь управления форсункой цилиндра №3 неисправна',
         'P0204': 'Цепь управления форсункой цилиндра №4 неисправна',
         'P0205': 'Цепь управления форсункой цилиндра №5 неисправна',
         'P0206': 'Цепь управления форсункой цилиндра №6 неисправна',
         'P0207': 'Цепь управления форсункой цилиндра №7 неисправна',
         'P0208': 'Цепь управления форсункой цилиндра №8 неисправна',
         'P0209': 'Цепь управления форсункой цилиндра №9 неисправна',
         'P0210': 'Цепь управления форсункой цилиндра №10 неисправна',
         'P0211': 'Цепь управления форсункой цилиндра №11 неисправна',
         'P0212': 'Цепь управления форсункой цилиндра №12 неисправна',
         'P0213': 'Цепь управления форсункой холодного старта №1 неисправна',
         'P0214': 'Цепь управления форсункой холодного старта №2 неисправна',
         'P0215': 'Соленоид выключения двигателя неисправен',
         'P0216': 'Цепь контроля времени впрыска неисправна',
         'P0217': 'Двигатель находится в перегретом состоянии',
         'P0218': 'Трансмиссия находится в перегретом состоянии',
         'P0219': 'Двигатель перекручен',
         'P0220': 'Неисправность датчика положения дроссельной заслонки «В»',
         'P0221': 'Выход сигнала из допустимого диапазона',
         'P0222': 'Низкий уровень выходного сигнала датчика «В»',
         'P0223': 'Высокий уровень выходного сигнала датчика «В»',
         'P0224': 'Сигнал датчика «В» перемежающийся',
         'P0225': 'Неисправность датчика положения дроссельной заслонки «С»',
         'P0226': 'Выход сигнала из допустимого диапазона',
         'P0227': 'Низкий уровень выходного сигнала датчика «С»',
         'P0228': 'Высокий уровень выходного сигнала датчика «С»',
         'P0229': 'Сигнал датчика «С» перемежающийся',
         'P0230': 'Первичная цепь бензонасоса (управление реле бензонас.) неисправна',
         'P0231': 'Вторичная цепь бензонасоса имеет постоянно низкий уровень',
         'P0232': 'Вторичная цепь бензонасоса имеет постоянно высокий уровень',
         'P0233': 'Вторичная цепь бензонасоса имеет перемежающийся уровень',
         'P0235': 'Цепь датчика давления турбо-наддува «А» неисправен',
         'P0236': 'Сигнал с датчика турбины «А» выходит из допустимого диапазона',
         'P0237': 'Сигнал с датчика турбины «А» имеет постоянно низкий уровень',
         'P0238': 'Сигнал с датчика турбины «А» имеет постоянно высокий уровень',
         'P0239': 'Цепь датчика давления турбо-наддува «Б» неисправен',
         'P0240': 'Сигнал с датчика турбины «Б» выходит из допустимого диапазона',
         'P0241': 'Сигнал с датчика турбины «Б» имеет постоянно низкий уровень',
         'P0242': 'Сигнал с датчика турбины «Б» имеет постоянно высокий уровень',
         'P0243': 'Соленоид затвора выхлопных газов турбины «А» неисправен',
         'P0244': 'Сигнал соленоида турбины «А» выходит из допустимого диапазона',
         'P0245': 'Соленоид выхлопных газов турбины «А» всегда закрыт',
         'P0246': 'Соленоид выхлопных газов турбины «А» всегда открыт',
         'P0247': 'Соленоид выхлопных газов турбины «В» неисправен',
         'P0248': 'Сигнал соленоида турбины «В» выходит из допустимого диапазона',
         'P0249': 'Соленоид выхлопных газов турбины «В» всегда закрыт',
         'P0250': 'Соленоид выхлопных газов турбины «В» всегда открыт',
         'P0251': 'Насос впрыска турбины «А» неисправен',
         'P0252': 'Сигнал насоса впрыска турбины «А» выходит из доп. диапазона',
         'P0253': 'Сигнал насоса впрыска турбины «А» имеет низкий уровень',
         'P0254': 'Сигнал насоса впрыска турбины «А» имеет высокий уровень',
         'P0255': 'Сигнал насоса впрыска турбины «А» перемежающийся',
         'P0256': 'Насос впрыска турбины «В» неисправен',
         'P0257': 'Сигнал насоса впрыска турбины «В» выходит из доп. диапазона',
         'P0258': 'Сигнал насоса впрыска турбины «В» имеет низкий уровень',
         'P0259': 'Сигнал насоса впрыска турбины «В» имеет высокий уровень',
         'P0260': 'Сигнал насоса впрыска турбины «В» перемежающийся',
         'P0261': 'Форсунка 1-ого цилиндра замкнута на землю',
         'P0262': 'Форсунка 1-ого цилиндра оборвана или замкнута на +12В',
         'P0263': 'Драйвер форсунки 1-ого цилиндра неисправен',
         'P0264': 'Форсунка 2-ого цилиндра замкнута на землю',
         'P0265': 'Форсунка 2-ого цилиндра оборвана или замкнута на +12В',
         'P0266': 'Драйвер форсунки 2-ого цилиндра неисправен',
         'P0267': 'Форсунка 3-го цилиндра замкнута на землю',
         'P0268': 'Форсунка 3-го цилиндра оборвана или замкнута на +12В',
         'P0269': 'Драйвер форсунки 3-го цилиндра неисправен',
         'P0270': 'Форсунка 4-ого цилиндра замкнута на землю',
         'P0271': 'Форсунка 4-ого цилиндра оборвана или замкнута на +12В',
         'P0272': 'Драйвер форсунки 4-ого цилиндра неисправен',
         'P0273': 'Форсунка 5-ого цилиндра замкнута на землю',
         'P0274': 'Форсунка 5-ого цилиндра оборвана или замкнута на +12В',
         'P0275': 'Драйвер форсунки 5-ого цилиндра неисправен',
         'P0276': 'Форсунка 6-ого цилиндра замкнута на землю',
         'P0277': 'Форсунка 6-ого цилиндра оборвана или замкнута на +12В',
         'P0278': 'Драйвер форсунки 6-ого цилиндра неисправен',
         'P0279': 'Форсунка 7-ого цилиндра замкнута на землю',
         'P0280': 'Форсунка 7-ого цилиндра оборвана или замкнута на +12В',
         'P0281': 'Драйвер форсунки 7-ого цилиндра неисправен',
         'P0282': 'Форсунка 8-ого цилиндра замкнута на землю',
         'P0283': 'Форсунка 8-ого цилиндра оборвана или замкнута на +12В',
         'P0284': 'Драйвер форсунки 8-ого цилиндра неисправен',
         'P0285': 'Форсунка 9-ого цилиндра замкнута на землю',
         'P0286': 'Форсунка 9-ого цилиндра оборвана или замкнута на +12В',
         'P0287': 'Драйвер форсунки 9-ого цилиндра неисправен',
         'P0288': 'Форсунка 10-ого цилиндра замкнута на землю',
         'P0289': 'Форсунка 10-ого цилиндра оборвана или замкнута на +12В',
         'P0290': 'Драйвер форсунки 10-ого цилиндра неисправен',
         'P0291': 'Форсунка 11-ого цилиндра замкнута на землю',
         'P0292': 'Форсунка 11-ого цилиндра оборвана или замкнута на +12В',
         'P0293': 'Драйвер форсунки 11-ого цилиндра неисправен',
         'P0294': 'Форсунка 12-ого цилиндра замкнута на землю',
         'P0295': 'Форсунка 12-ого цилиндра оборвана или замкнута на +12В',
         'P0296': 'Драйвер форсунки 12-ого цилиндра неисправен',
         'P03XX': 'Система зажигания и пропуски',
         'P0300': 'Обнаружены случайные/множественные пропуски зажигания',
         'P0301': 'Обнаружены пропуски зажигания в 1-ом цилиндре',
         'P0302': 'Обнаружены пропуски зажигания во 2-ом цилиндре',
         'P0303': 'Обнаружены пропуски зажигания в 3-ем цилиндре',
         'P0304': 'Обнаружены пропуски зажигания в 4-ом цилиндре',
         'P0305': 'Обнаружены пропуски зажигания в 5-ом цилиндре',
         'P0306': 'Обнаружены пропуски зажигания в 6-ом цилиндре',
         'P0307': 'Обнаружены пропуски зажигания в 7-ом цилиндре',
         'P0308': 'Обнаружены пропуски зажигания в 8-ом цилиндре',
         'P0309': 'Обнаружены пропуски зажигания в 9-ом цилиндре',
         'P0310': 'Обнаружены пропуски зажигания в 10-ом цилиндре',
         'P0311': 'Обнаружены пропуски зажигания в 11-ом цилиндре',
         'P0312': 'Обнаружены пропуски зажигания в 12-ом цилиндре',
         'P0320': 'Цепь распределителя зажигания неисправна',
         'P0321': 'Сигнал цепи распределителя зажигания выходит за доп. пределы',
         'P0322': 'Сигнал цепи распределителя зажигания отсутствует',
         'P0323': 'Сигнал цепи распределителя зажигания перемежающийся',
         'P0325': 'Цепь датчика детонации №1 неисправна',
         'P0326': 'Сигнал датчика детонации №1 выходит за допустимые пределы',
         'P0327': 'Сигнал датчика детонации №1 имеет низкий уровень',
         'P0328': 'Сигнал датчика детонации №1 имеет высокий уровень',
         'P0329': 'Сигнал датчика детонации №1 перемежающийся',
         'P0330': 'Цепь датчика детонации №2 неисправна',
         'P0331': 'Сигнал датчика детонации №2 выходит за допустимые пределы',
         'P0332': 'Сигнал датчика детонации №2 имеет низкий уровень',
         'P0333': 'Сигнал датчика детонации №2 имеет высокий уровень',
         'P0334': 'Сигнал датчика детонации №2 перемежающийся',
         'P0335': 'Датчик положения коленчатого вала «А» неисправен',
         'P0337': 'Сигнал датчика «А» имеет низкий уровень или замкнут на массу',
         'P0338': 'Сигнал датчика «А» имеет высокий уровень или замкнут на 12В',
         'P0339': 'Сигнал датчика «А» перемежающийся',
         'P0340': 'Датчик положения распределительного вала неисправен',
         'P0341': 'Сигнал датчика выходит за допустимые пределы',
         'P0342': 'Сигнал датчика имеет низкий уровень или замкнут на массу',
         'P0343': 'Сигнал датчика имеет высокий уровень',
         'P0344': 'Сигнал датчика перемежающийся',
         'P0350': 'Первичная/вторичная цепи катушки зажигания неисправны',
         'P0351': 'Первичная/вторичная цепи катушки зажигания «А» неисправны',
         'P0352': 'Первичная/вторичная цепи катушки зажигания «B» неисправны',
         'P0353': 'Первичная/вторичная цепи катушки зажигания «C» неисправны',
         'P0354': 'Первичная/вторичная цепи катушки зажигания «D» неисправны',
         'P0355': 'Первичная/вторичная цепи катушки зажигания «E» неисправны',
         'P0356': 'Первичная/вторичная цепи катушки зажигания «F» неисправны',
         'P0357': 'Первичная/вторичная цепи катушки зажигания «G» неисправны',
         'P0358': 'Первичная/вторичная цепи катушки зажигания «H» неисправны',
         'P0359': 'Первичная/вторичная цепи катушки зажигания «I» неисправны',
         'P0360': 'Первичная/вторичная цепи катушки зажигания «J» неисправны',
         'P0361': 'Первичная/вторичная цепи катушки зажигания «K» неисправны',
         'P0362': 'Первичная/вторичная цепи катушки зажигания «L» неисправны',
         'P0370': 'TIMING REF (HRS) A MALFUNCTION',
         'P0371': 'TIMING REF (HRS) A TOO MANY PULSES',
         'P0372': 'TIMING REF (HRS) A TOO MANY PULSES',
         'P0373': 'TIMING REF (HRS) A INTERMITTENT PULSES',
         'P0374': 'TIMING REF (HRS) A NO PULSES',
         'P0375': 'TIMING REF (HRS) B MALFUNCTION',
         'P0376': 'TIMING REF (HRS) B TOO MANY PULSES',
         'P0377': 'TIMING REF (HRS) B TOO MANY PULSES',
         'P0378': 'TIMING REF (HRS) B INTERMITTENT PULSES',
         'P0379': 'TIMING REF (HRS) B NO PULSES',
         'P0380': 'Свеча накаливания или цепь нагрева неисправны',
         'P0381': 'Свеча накаливания или индикатор нагрева неисправны',
         'P0385': 'Цепь датчика положения коленчатого вала «В» неисправны',
         'P0386': 'Сигнал датчика «В» выходит за допустимые пределы',
         'P0387': 'Цепь датчика оборвана или замкнута на массу',
         'P0388': 'Цепь датчика замкнута на один из силовых выводов',
         'P0389': 'Сигнал датчика «В» перемежающийся',
         'P04XX': 'AUXILIARY EMISSION CONTROLS',
         'P0400': 'Система рециркуляции отработанных газов неисправна',
         'P0401': 'Система рециркуляции отработанных газов неэффективна',
         'P0402': 'Система рециркуляции отработанных газов избыточна',
         'P0403': 'Цепь датчика рециркуляции отработанных газов неисправна',
         'P0404': 'Сигнал датчика выходит за допустимые пределы',
         'P0405': 'Сигнал датчика «А» имеет низкий уровень',
         'P0406': 'Сигнал датчика «А» имеет высокий уровень',
         'P0407': 'Сигнал датчика «В» имеет низкий уровень',
         'P0408': 'Сигнал датчика «В» имеет высокий уровень',
         'P0410': 'Система вторичной подачи (впрыска) воздуха неисправна',
         'P0411': 'Ошибочный поток проходит через систему вторичной подачи воздуха',
         'P0412': 'Клапан системы вторичной подачи воздуха «А» неисправен',
         'P0413': 'Клапан системы вторичной подачи воздуха «А» всегда открыт',
         'P0414': 'Клапан системы вторичной подачи воздуха «А» всегда закрыт',
         'P0415': 'Клапан системы вторичной подачи воздуха «В» неисправен',
         'P0416': 'Клапан системы вторичной подачи воздуха «В» всегда открыт',
         'P0417': 'Клапан системы вторичной подачи воздуха «В» всегда закрыт',
         'P0420': 'Эффективность системы катализаторов «В1» ниже порога',
         'P0421': 'Эффективность прогрева катализатора «В1» ниже порога',
         'P0422': 'Эффективность главного катализатора «В1» ниже порога',
         'P0423': 'Эффективность нагревателя катализатора «В1» ниже порога',
         'P0424': 'Температура нагревателя катализатора «В2» ниже порога',
         'P0430': 'Эффективность системы катализаторов «В2» ниже порога',
         'P0431': 'Эффективность прогрева катализатора «В2» ниже порога',
         'P0432': 'Эффективность главного катализатора «В2» ниже порога',
         'P0433': 'Эффективность нагревателя катализатора «В2» ниже порога',
         'P0434': 'Температура нагревателя катализатора «В2» ниже порога',
         'P0440': 'Контроль системы улавливания паров бензина неисправен',
         'P0441': 'Система улавливания паров бензина плохо продувается',
         'P0442': 'Обнаружена небольшая утечка в системе улавливания паров',
         'P0443': 'Управление клапаном продувки системы «EVAP» неисправен',
         'P0444': 'Клапан продувки системы «EVAP» всегда открыт',
         'P0445': 'Клапан продувки системы «EVAP» всегда закрыт',
         'P0446': 'Управление воздушным клапаном системы «EVAP» неисправно',
         'P0447': 'Воздушный клапан системы «EVAP» всегда открыт',
         'P0448': 'Воздушный клапан системы «EVAP» всегда закрыт',
         'P0450': 'Датчик давления паров бензина неисправен',
         'P0451': 'Сигнал датчика давления паров бензина выходит за доп. диапазон',
         'P0452': 'Сигнал датчика давления паров бензина имеет низкий уровень',
         'P0453': 'Сигнал датчика давления паров бензина имеет высокий уровень',
         'P0454': 'Сигнал датчика давления паров бензина перемежающийся',
         'P0455': 'Обнаружена грубая утечка в системе улавливания паров',
         'P0460': 'Цепь датчика уровня топлива неисправна',
         'P0461': 'Сигнал датчика уровня топлива выходит за допустимые пределы',
         'P0462': 'Сигнал датчика уровня топлива имеет низкий уровень',
         'P0463': 'Сигнал датчика уровня топлива имеет высокий уровень',
         'P0464': 'Сигнал датчика уровня топлива перемежающийся',
         'P0465': 'Цепь датчика потока воздуха продувки неисправен',
         'P0466': 'Сигнал датчика потока воздуха продувки выходит за доп. пределы',
         'P0467': 'Сигнал датчика потока воздуха продувки имеет низкий уровень',
         'P0468': 'Сигнал датчика потока воздуха продувки имеет высокий уровень',
         'P0469': 'Сигнал датчика потока воздуха продувки перемежающийся',
         'P0470': 'Датчик давления выхлопных газов неисправен',
         'P0471': 'Сигнал датчика давления выходит за доп. диапазон',
         'P0472': 'Сигнал датчика давления имеет низкий уровень',
         'P0473': 'Сигнал датчика давления имеет высокий уровень',
         'P0474': 'Сигнал датчика давления перемежающийся',
         'P0475': 'Клапан датчика давления выхлопных газов неисправен',
         'P0476': 'Сигнал клапана датчика давления выходит за доп. диапазон',
         'P0477': 'Сигнал клапана датчика давления имеет низкий уровень',
         'P0478': 'Сигнал клапана датчика давления имеет высокий уровень',
         'P0479': 'Сигнал клапана датчика давления перемежающийся',
         'P05XX': 'EHICLE SPEED, IDLE CONTROL AND AUXILIARY INPUTS',
         'P0500': 'Датчик скорости автомобиля неисправен',
         'P0501': 'Сигнал датчика скорости автомобиля выходит за доп. пределы',
         'P0502': 'Сигнал датчика скорости автомобиля имеет низкий уровень',
         'P0503': 'Сигнал датчика перемежающийся или имеет высокий уровень',
         'P0505': 'Система поддержания холостого хода неисправна',
         'P0506': 'Обороты двигателя под управлением системы слишком низкие',
         'P0507': 'Обороты двигателя под управлением системы слишком высокие',
         'P0510': 'Концевик индикации закрытого положения дросселя неисправен',
         'P0530': 'Датчик давления хладагента кондиционера неисправен',
         'P0531': 'Сигнал датчика давления хладагента выходит за доп. диапазон',
         'P0532': 'Сигнал датчика давления хладагента имеет низкий уровень',
         'P0533': 'Сигнал датчика давления хладагента имеет высокий уровень',
         'P0534': 'Большая потеря хладагента в кондиционере',
         'P0550': 'Датчик давления гидроусилителя руля неисправен',
         'P0551': 'Сигнал датчика давления выходит за допустимый диапазон',
         'P0552': 'Сигнал датчика давления имеет низкий уровень',
         'P0553': 'Сигнал датчика давления имеет высокий уровень',
         'P0554': 'Сигнал датчика давления перемежающийся',
         'P0560': 'Датчик бортового напряжения неисправен',
         'P0561': 'Бортовое напряжение нестабильно',
         'P0562': 'Бортовое напряжение имеет низкий уровень',
         'P0563': 'Бортовое напряжение имеет высокий уровень',
         'P0565': 'Цепь включения «круиз контроля» неисправна',
         'P0566': 'Цепь выключения «круиз контроля» неисправна',
         'P0567': 'Цепь продолжения работы «круиз контроля» неисправна',
         'P0568': 'Цепь продолжения работы «круиз контроля» неисправна',
         'P0569': 'Цепь поддержки «наката» «круиз контроля» неисправна',
         'P0570': 'Цепь поддержки «разгона» «круиз контроля» неисправна',
         'P0571': 'Переключатель включения тормозов «круиз контроля» неисправен',
         'P0572': 'Переключатель всегда замкнут',
         'P0573': 'Переключатель всегда разомкнут',
         'P06XX': 'COMPUTER AND AUXILIARY OUTPUTS',
         'P0600': 'Линия передачи последовательных данных неисправна',
         'P0601': 'Ошибка контрольной суммы внутренней памяти',
         'P0602': 'Программная ошибка контрольного модуля',
         'P0603': 'Ошибка репрограммируемой памяти',
         'P0604': 'Ошибка оперативного запоминающего устройства',
         'P0605': 'Ошибка постоянного запоминающего устройства',
         'P0606': 'Ошибка модуля управления энергосбережением',
         'P07XX': 'TRANSMISSION',
         'P0700': 'Система управления трансмиссией неисправна',
         'P0701': 'Система управления трансмиссией работает неверно',
         'P0702': 'TRANS CONTROL SYSTEM ELECTRICAL',
         'P0703': 'Переключатель карданный вал/тормоза неисправен',
         'P0704': 'Цепь датчика включения сцепления неисправен',
         'P0705': 'Датчик диапазона работы трансмиссии неисправен',
         'P0706': 'Сигнал датчика выходит за допустимые пределы',
         'P0707': 'Сигнал датчика имеет низкий уровень',
         'P0708': 'Сигнал датчика имеет высокий уровень',
         'P0709': 'Сигнал датчика перемежающийся',
         'P0710': 'Датчик температуры трансмиссионной жидкости неисправен',
         'P0711': 'Сигнал датчика выходит за допустимые пределы',
         'P0712': 'Сигнал датчика имеет низкий уровень',
         'P0713': 'Сигнал датчика имеет высокий уровень',
         'P0714': 'Сигнал датчика перемежающийся',
         'P0715': 'Датчик скорости турбины неисправен',
         'P0716': 'Сигнал датчика выходит за допустимые пределы',
         'P0717': 'Сигнал датчика отсутствует',
         'P0718': 'Сигнал датчика перемежающийся',
         'P0719': 'Переключатель карданный вал/тормоза замкнут на массу',
         'P0720': 'Цепь датчика «Внешней скорости» неисправна',
         'P0721': 'Сигнал датчика «Внешней скорости» выходит за доп. пределы',
         'P0722': 'Сигнал датчика «Внешней скорости» отсутствует',
         'P0723': 'Сигнал датчика «Внешней скорости» перемежающийся',
         'P0724': 'Переключатель карданный вал/тормоза замкнут на питание',
         'P0725': 'Цепь датчика скорости вращения двигателя неисправен',
         'P0726': 'Сигнал датчика выходит за допустимые пределы',
         'P0727': 'Сигнал датчика отсутствует',
         'P0728': 'Сигнал датчика перемежающийся',
         'P0730': 'Передаточное число трансмиссии неверно',
         'P0731': 'Передаточное число трансмиссии на 1 передаче неверно',
         'P0732': 'Передаточное число трансмиссии на 2 передаче неверно',
         'P0733': 'Передаточное число трансмиссии на 3 передаче неверно',
         'P0734': 'Передаточное число трансмиссии на 4 передаче неверно',
         'P0735': 'Передаточное число трансмиссии на 5 передаче неверно',
         'P0736': 'Передаточное число трансмиссии на передаче задн. хода неверно',
         'P0740': 'Цепь управления блокировкой дифференциала неисправна',
         'P0741': 'Дифференциал всегда выключен (разблокирован)',
         'P0742': 'Дифференциал всегда включен (заблокирован)',
         'P0743': 'TCC CIRCUIT ELECTRICAL',
         'P0744': 'Дифференциал состояние неустойчивое',
         'P0745': 'Управление сжимающим соленоидом неисправно',
         'P0746': 'Соленоид всегда в выключенном состоянии',
         'P0747': 'Соленоид всегда во включенном состоянии',
         'P0748': 'PRESSURE CONTROL SOLENOID ELECTRICAL',
         'P0749': 'Состояние соленоида неустойчиво',
         'P0750': 'Соленоид «А» включения передачи неисправен',
         'P0751': 'Соленоид «А» всегда в выключенном состоянии',
         'P0752': 'Соленоид «А» всегда во включенном состоянии',
         'P0753': 'SHIFT SOLENOID A ELECTRICAL',
         'P0754': 'Состояние соленоида «А» неустойчиво',
         'P0755': 'Соленоид «В» включения передачи неисправен',
         'P0756': 'Соленоид «В» всегда в выключенном состоянии',
         'P0757': 'Соленоид «В» всегда во включенном состоянии',
         'P0758': 'SHIFT SOLENOID B ELECTRICAL',
         'P0759': 'Состояние соленоида «В» неустойчиво',
         'P0760': 'Соленоид «С» включения передачи неисправен',
         'P0761': 'Соленоид «С» всегда в выключенном состоянии',
         'P0762': 'Соленоид «С» всегда во включенном состоянии',
         'P0763': 'SHIFT SOLENOID C ELECTRICAL',
         'P0764': 'Состояние соленоида «С» неустойчиво',
         'P0765': 'Соленоид «Д» включения передачи неисправен',
         'P0766': 'Соленоид «Д» всегда в выключенном состоянии',
         'P0767': 'Соленоид «Д» всегда во включенном состоянии',
         'P0768': 'SHIFT SOLENOID D ELECTRICAL',
         'P0769': 'Состояние соленоида «Д» неустойчиво',
         'P0770': 'P0771Соленоид «Е» включения передачи неисправен',
         'P0771': 'Соленоид «Е» всегда в выключенном состоянии',
         'P0772': 'Соленоид «Е» всегда во включенном состоянии',
         'P0773': 'SHIFT SOLENOID E ELECTRICAL',
         'P0774': 'Состояние соленоида «Е» неустойчиво',
         'P0780': 'Переключение передач не работает',
         'P0781': 'Электромагнитный клапан ускоряющей передачи неспособен провести переключение с 1-ей передачи на ускоряющую передачу 2',
         'P0782': 'Электромагнитный клапан ускоряющей передачи неспособен провести переключение с 2-ей передачи на ускоряющую передачу 3',
         'P0783': 'Электромагнитный клапан ускоряющей передачи неспособен провести переключение с 3-ей передачи на ускоряющую передачу 4',
         'P0784': 'Электромагнитный клапан ускоряющей передачи неспособен провести переключение с 4-ей передачи на ускоряющую передачу 5',
         'P0785': 'Соленоид управления синхронизатором неисправен',
         'P0786': 'SHIFT/TIMING SOL RANGE/PERFORMANCE',
         'P0787': 'Соленоид управления синхронизатором всегда выключен',
         'P0788': 'Соленоид управления синхронизатором всегда включен',
         'P0789': 'Соленоид управления синхронизатором неустойчив',
         'P0790': 'Цепь переключателя режима движения неисправна',
         'P0030': 'Проблемы в цепи реле нагревателя кислородного датчика 1/1',
         'P0036': 'Проблемы в цепи реле нагревателя кислородного датчика 1/2',
         'P0456': 'В системе улавливания паров топлива обнаружена небольшая утечка',
         'P0522': 'Сигнал датчика давления масла ниже нормы',
         'P0523': 'Сигнал датчика давления масла выше нормы',
         'P0645': 'Обрыв или короткое замыкание в цепи реле муфты компрессора кондиционера',
         'P0801': 'Обрыв или короткое замыкание в цепи электромагнитного клапана блокировки передачи заднего хода',
         'P1192': 'Низкое напряжение в цепи датчика температуры воздуха на впуске',
         'P1193': 'Высокое напряжение в цепи датчика температуры воздуха на впуске',
         'P1195': 'Медленный отклик кислородного датчика 1/1 при проверке нейтрализатора (был P 0133)',
         'P1196': 'Медленный отклик кислородного датчика 2/1 при проверке нейтрализатора (был P 0153)',
         'P1197': 'Медленный отклик кислородного датчика 1/2 при проверке нейтрализатора (был P 0139)',
         'P1198': 'Напряжение сигнала датчика температуры охлаждающей жидкости в радиаторе выше допустимого',
         'P1199': 'Напряжение сигнала датчика температуры охлаждающей жидкости в радиаторе ниже допустимого',
         'P1281': 'Температура двигателя ниже нормы при достаточно длинной поездке (термостат)',
         'P1282': 'Обрыв или короткое замыкание в цепи реле топливного насоса',
         'P1288': 'Обрыв или короткое замыкание в цепи электромагнитного клапана "короткого" впускного тракта',
         'P1289': 'Обрыв или короткое замыкание в цепи электромагнитного клапана впускного тракта с изменяемой геометрией',
         'P1290': 'Давление в системе сжатого природного газа выше нормы',
         'P1291': 'Включение подогрева впускного коллектора не приводит к заметному повышению температуры воздуха',
         'P1292': 'Сигнал датчика давления в системе сжатого природного газа выше нормы',
         'P1293': 'Сигнал датчика давления в системе сжатого природного газа ниже нормы',
         'P1294': 'Заданная частота вращения холостого хода не достигнута. Возможны либо утечки вакуума, либо неверная установка шагового электродвигателя регулятора холостого хода',
         'P1295': 'Нет подачи напряжения (5 В) на датчик положения дроссельной заслонки',
         'P1296': 'Нет подачи напряжения (5 В) на датчик абсолютного давления',
         'P1297': 'Нет изменения сигнала датчика абсолютного давления при запуске двигателя',
         'P1298': 'Длительное приготовление бедной смеси при полностью открытой дроссельной заслонке',
         'P1299': 'Сигнал датчика абсолютного давления не согласован с сигналом датчика положения дроссельной заслонки. Возможны утечки вакуума',
         'P1388': 'Обрыв или короткое замыкание в цепи реле отключения ASD',
         'P1389': 'Нет напряжений Z1 или Z2 при включении реле автоматического отключения ASD',
         'p1390': 'Нет синхронизации сигналов датчиков положения коленчатого и распределительного валов',
         'P1391': 'Потеря сигнала датчиков положения коленчатого и распределительного валов (2.0 L)',
         'P1398': 'Блок управления двигателем не может применить сигнал датчика положения коленчатого вала для диагностики пропусков воспламенения',
         'P1399': 'Обрыв или короткое замыкание в цепи индикатора "пауза перед запуском',
         'P1403': 'Нет питания (5 В) датчика положения клапана РОГ',
         'P1476': 'Недостаточный расход подачи воздуха на выпуск при проверке системы (был p 0411)',
         'P1477': 'Слишком большой расход подачи воздуха на выпуск при проверке системы (был P 0411)',
         'P1478': 'Напряжение сигнала температуры аккумуляторной батареи ниже нормы',
         'P1479': 'Обрыв или короткое замыкание в цепи реле вентилятора АКПП',
         'P1480': 'Обрыв или короткое замыкание в цепи электромагнитного клапана системы вентиляции картера',
         'P1481': 'Сигнал генератора импульсов EATX RPM для обнаружения пропусков воспламенения не соответствует ожидаемой величине',
         'P1482': 'Короткое замыкание в цепи датчика температуры каталитического нейтрализатора (низкая температура)',
         'P1483': 'Короткое замыкание в цепи датчика температуры каталитического нейтрализатора (высокая температура)',
         'P1484': 'Обнаружен перегрев каталитического нейтрализатора',
         'P1485': 'Обрыв или короткое замыкание в цепи электромагнитного клапана системы подачи воздуха на выпуск',
         'P1486': 'Насос определения утечек (LDP) в системе улавливания паров топлива определил пережатие шланга',
         'P1487': 'Обрыв или короткое замыкание в цепи реле №2 управления высокой скоростью вентилятора радиатора',
         'P1488': 'Вспомогательное питание датчика (5 В) ниже приемлемого предела',
         'P1489': 'Обрыв или короткое замыкание в цепи реле управления высокой скоростью вентилятора радиатора',
         'P1490': 'Обрыв или короткое замыкание в цепи реле управления низкой скоростью вентилятора радиатора',
         'P1491': 'Обрыв или короткое замыкание в цепи реле управления скоростью вентилятора радиатора (включая реле питания)',
         'P1492': 'Напряжение сигнала датчика температуры наружного воздуха выше нормы',
         'P1493': 'Напряжение сигнала датчика температуры наружного воздуха ниже нормы',
         'P1494': 'Некорректный статус выключателя насоса определения утечек (LDP) в системе улавливания паров топлива',
         'P1495': 'Обрыв или короткое замыкание в цепи электромагнитного клапана насоса определения утечек (LDP)',
         'P1496': 'Питание датчика (5 В) ниже приемлемого предела (меньше 4 В в течение 4 сек)',
         'P1498': 'Обрыв или короткое замыкание в цепи реле №3 управления высокой скоростью вентилятора радиатора',
         'P1595': 'Обрыв или короткое замыкание в цепи электромагнитных клапанов системы поддержания скорости',
         'P1596': 'На выключателе системы поддержания скорости напряжение выше допустимого',
         'P1597': 'На выключателе системы поддержания скорости напряжение ниже допустимого',
         'P1598': 'Напряжение датчика давления в системе кондиционирования слишком высокое',
         'P1599': 'Напряжение датчика давления в системе кондиционирования слишком низкое',
         'P1680': 'Обрыв или короткое замыкание в цепи муфты компрессора кондиционера',
         'P1681': 'Нет обмена между блоками CCD/J1850 управления приборами',
         'P1683': 'Обрыв или короткое замыкание в цепи управления системы поддержания скорости (внешнее реле SBECII)',
         'P1684': 'Аккумуляторная батарея была отсоединена в пределах последних 50 запусков',
         'P1685': 'Контроллер управления двигателем получил недействительный код SKIM',
         'P1686': 'Нет обмена между модулями CCD/J1850 при проверке кодов иммобилайзера',
         'P1687': 'Блоки CCD/J1850 не получили сообщения от блока приборов (MIC)',
         'P1693': 'Неисправность возникла в сопутствующем блоке управления двигателем',
         'P1694': 'Блоки CCD/J1850 не получили сообщения от блока управления силовым агрегатом (Aisin)',
         'P1695': 'Блоки CCD/J1850 не получили сообщения от блока управления электрооборудованием автомобиля',
         'P1696': 'Неудачная попытка записать в EEPROM место блока управления',
         'P1697': 'Неудачная попытка обновить показания индикатора обслуживания (SRI или EMR) в EEPROM',
         'P1698': 'Блоки CCD/J1850 не получили сообщения от блока управления АКПП',
         'P1719': 'Обрыв или короткое замыкание в цепи электромагнитного клапана переключения 2-3',
         'P1740': 'Неисправность в цепи электромагнитного клапана TCC или повышающей передачи',
         'P1756': 'Требуемое и фактическое давление в системе управления регулятором не в пределах допуска для управления 1-ой, 2-ой и 3-ей передачами (сбой среднего давления)',
         'P1757': 'Требуемое и фактическое давление в системе управления регулятором не в пределах допуска для управления 1-ой, 2-ой и 3-ей передачами (сбой нулевого давления)',
         'P1762': 'Сигнал датчика давления регулятора больше или меньше, чем предел калибровки (в трёх последовательных калибровках Парк/Нейтраль)',
         'P1763': 'Напряжение сигнала датчика давления регулятора выше приемлемого уровня',
         'P1764': 'Напряжение сигнала датчика давления регулятора ниже приемлемого уровня',
         'P1765': 'Обрыв или короткое замыкание в цепи реле питания управления АКПП (питание системы TCC)',
         'P1899': 'Неверный статус выключателя Парк/Нейтраль',
         'P0622': 'Обрыв или короткое замыкание в цепи обмотки возбуждения генератора',
         'P1594': 'Напряжение зарядки аккумуляторной батареи выше допустимого',
         'P1682': 'Напряжение зарядки аккумуляторной батареи ниже допустимого и нет заметного изменения напряжения при проверке выхода генератора'}


@fca.message_handler(commands=['start', 'help'])
def start(message):

    user = f'<b>{message.from_user.first_name}</b>'
    info = '! Вставляем ключ в замок зажигания и делаем три поворота ключа "туда- обрано" до положения включения приборной панели. На третий раз оставляем в положениие и переписываем ошибки '

    fca.send_message(message.chat.id, user + info, parse_mode='html')
    fca.send_message(message.chat.id, "вводить код: P0101")
    print("Пользователь:", message.from_user.first_name + ".")
    print("Сообщение пользователя:",message.text)


@fca.message_handler(content_types= ['text'])
def code(message):
    user_answer = 'НЕТ ТАКОЙ ОШИБКИ!!!'

    print("Пользователь:", message.from_user.first_name)
    print("Сообщение пользователя:", message.text)
    code = message.text.upper()
    if code in errors:
        fca.send_message(message.chat.id, errors[message.text.upper()])
    else:
        fca.send_message(message.chat.id, user_answer, parse_mode='html')

    fca.send_message(message.chat.id, 'введите ошибку:')



fca.polling(none_stop=True)
