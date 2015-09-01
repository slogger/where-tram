# Толстый клиент для [online.ettu.ru](http://online.ettu.ru)

## Что-нового

### Back-end
* Декомпозиция кода
* Подстроился под требования `select2`
* Добавил немного тестов
* Убрал шаблонизацию силами `tornado`
* Just startup for server

### Front-end
* Привет, БЭМ!, на самом деле нет
* Использование блока maps, написанного на БЭМ-хакатоне
* Карта центрируется на остановке
* Кэшированние на стороне клиента
* Сломал автокомплит поисковой формы и не смог подружить `i-bem` и `select2`,
  рабочий пример того как оно должно работать можно посмотреть [здесь](http://jsfiddle.net/slogger/g7rzhbx1/)

## В планах

### Back-end
* Больше тестов
* _Возможно_ прикрутить `ghost.py` (что то похожее на `phantom` из мира `node`),
  для тестирования фронтенда средствами пайтона
* _Возможно_ написать маленький браузер на `gtk` и `webkit-gtk`
* Вытаскивать больше данных с сервера ЕТТУ

### Front-end
* Починить автокомплит
* Тестирование
* Больше AJAX'a и работы без перезагрузки страницу
* _Возможно_ автообновление данных

## Порядок запуска
* Установить node зависимости `npm install`
* Установить bower зависимости `bower install`
* Собрать статические файлы, _#b\__  `enb make`
* Установить pip зависимости `pip install -f etransport/requirements.txt`
* Запустить сервер `python3 -m etransport`

## Порядок работы
Из-за сломаного автокомплита теперь приходится
вручную указывать айдишник интересующей нас
остановки, для этого нужно пройти по нехитрому алгоритму
```
    1) Зайти на сайт http://online.ettu.ru
    2) Выбрать нужную остановку
    3) Скопировать из адресной строки id-остновки
    4) Перейти по адресу <server addr>/?id=<id>
       например: http://localhost:5000/?id=3416
```