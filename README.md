# INT-18

В данном интенсиве решено несколько заданий.
Задание №1.\
a. Ссылку на коммит, исправляющий уязвимость\
b. Перечень значимых строк кода, относящихся к уязвимости\
c. Регулярное выражение, позволяющее максимально точно детектировать атаку на данную уязвимость в потоке трафика\
d(*). Перечень всех функций публичного API уязвимого приложения/компонента, из которых возможно достижение строк из п.b
1. CVE-2022-35919\
https://github.com/minio/minio/commit/bc72e4226e669d98c8e0f3eccc9297be9251c692 \
В указанной ссылке commit'a начиная с 294 строки и заканчивая 337 указаны изменяемые строки. Некоторые из них были удалены, другие изменены.
2. CVE-2019-9194\
https://github.com/Studio-42/elFinder/compare/6884c4f...0740028 & https://github.com/Studio-42/elFinder/commit/9b01848173fd678acc76e06a15103ddc71eefb35 \
В 1 -й ссылке указано, что добавлено обновление от CVE и перечислены изменения всех файлов.\
Во 2-й ссылке перечислены изменяемые строчки кода. 620(8-9), 643(3-4), 6439, 645(0-1).
3. CVE-2018-20434\
В данных ссылках предоставлен код эксплойта.\
https://packetstormsecurity.com/files/153448/LibreNMS-1.46-addhost-Remote-Code-Execution.html \
https://packetstormsecurity.com/files/153188/LibreNMS-addhost-Command-Injection.html \
Или же по следующей ссылке в примерах указано, из-за чего может появится данный эксплойт.\
https://cwe.mitre.org/data/definitions/78.html

c. Данное регулярное выражение способно обнаружить атаку в потоке трафика:\
CVE-\d{4}-\d{4,5}\
Год в виде 4-х цифр и номер уязвимости от 4 до 5 цифр.

Задание №2.\
Из-за некоторых проблем не смог реализовать атаку на поднятый сервер, загрузил ранее мной написанный файл с брутфорс атакой (broot.py), в которой нужно указать ссылку на сайт и при запуске нужно указать логин, далее количество потоков и будет произведён перебор паролей из словаря букв.\
Я понимаю, что это не подходит под задание, но суть почти одна и та же.

Задание №5.\
Функция метода решено и может вывести ответ 2-я разными способами, достаточно запустить файл main.py и следовать инструкциям.
