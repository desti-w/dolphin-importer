# dolphin-importer
![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?style=flat-square)
![Supports](https://img.shields.io/badge/Python-Windows%20%7C%20MacOS-brightgreen?style=flat-square)
![Metamask](https://img.shields.io/badge/Metamask-10.25.0%20--%2010.29.0-orange?style=flat-square)
___

#### Описание режимов работы:
1. Скрипт импортирует созданные метамаски в готовые профили в Adspower.
После импорта он добавляет сети Optimism, BSC, Polygon и Arbitrum, zkSync Era, Arbitrum Nova, Avalanche, Gnosis Chain, Fantom, Aurora в кошелек.  
Заменяет уже добавленые метамаски на новые. Добавленые сети сохраняются.
2. Режим подготовки профилей к работе. Открывает профили и разблокирует метамаски.

___
#### Для установки необходимых библиотек пропиши в терминал:
```
pip install -r requirements.txt
```
___
### LavaMoat Fixed :white_check_mark:

Этот фикс отключает LavaMoat путем изменения переменной **scuttleGlobalThis** в файле run-time.js


В фиксе присутствуют 1 файл:
* LavaMoatExtFix.py




**LavaMoatExtFix.py** - предназначен для изменения файла run-time.js в условном "корневом" каталоге расширения Metamask, скаченным Adspower. Позваляет создавать профили с **отключенным** LavaMoat.

**Запуск LavaMoatExtFix.py**
1. Запустите скрипт.
* При успешном применении вы увидите:

```
Фикс применен/fix applied.
```
___



### Исктрукция для скрипта импорта :man_technologist: :rocket:
1. Измени переменную "metamask_id" в разделе настроек. <br> </br>
   ```metamask_id = 'YOUR_METAMASK_ID'``` <br> </br>
   Для получения metamask_id запустите профиль dolphin с установленным Metamask. Скопируйте:<br></br> ![mm_id](./images/mm.png)
<br></br>

2. Экспортируй ids из adspower со своих профилей
3. Добавь эти ids в файл id_users.txt (каждый с новой строки)
4. Добавь сид-фразы от заранее созданных кошельков в файл seeds.txt (каждый с новой строки)
5. По желанию в файле main.py измени переменную password (по умолчанию=password123)
6. Запусти Adspower
7. Запусти файл main.py



**Возможные режимы работы:**

|  Переменная   |  Значение  | Режим работы                                                                                                                                                                              |        
|:-------------:|:----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  unlock_mode  |     0      | Импортирует сид-фразы в созданные профиля, если в профиле уже имеется авторизованный метамаск, он будет заменен на новый через fargot password.                                           |
|  unlock_mode  |     1      | Режим предназначен для подготовки профилей к работе.   <br>Запускает профиль и входит в метамаск, при этом окно профиля закрываться не будет.   <br>Не требует заполнения файла seeds.txt |        

### FAQ
1. Если у вас не прогружается Metamask, попробуйте отключить/изменить прокси.
2. Если у вас не прогружаются сети, попробуйте изменить rpc проблемной сети или отключить/изменить прокси.

Если у вас что-то не получается или возникают ошибки, обратитесь к разработчику. Буду рад помочь :alien:	

### Поддержка :heart:
Btc   : bc1qwjv6rlkwhj3ft0ejzq8ntdcw455gfmzupstgte <br> 
Eth   : 0xbF7534d0e8A048a6b621c7DA1db65b4b866718E4 <br>
Arb   : 0xbF7534d0e8A048a6b621c7DA1db65b4b866718E4 <br>
USDT &nbsp;trc20&nbsp;&nbsp; : &nbsp; TFyu4aPm8jHU68pZwJjSwN4r72X8hEvnV3 <br>
BUSD &nbsp;bep20 : &nbsp; 0xbF7534d0e8A048a6b621c7DA1db65b4b866718E4 <br>

### Rework by *[Desti](https://t.me/ddest1)*

#### При поддержке канала *[hodlmod.eth](https://t.me/hodlmodeth)*