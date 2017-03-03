# Accounts

> Each member of new organization gets personal cabinet in Dogs Systems. There are a lots of messages between dogs. They are very useful proofs against dogs.
> 
> We think that they don't mind about securely storing passwords. Find some message for us.
>
> _Hint:_ what users have you met earlier? Can you find their data

## Write-up
Вы часто встречались с Мухтаром и Петром. Давайте их и проверим.

На главной странице система выдает ошибки "Invalid username" или "Invalid password".
Подбором узнаем, что подходящие имена для пользователей — `muhtar` и `petro`.

Пароль узнать уже труднее. Но в HTML-коде главной страницы есть комментарий, указывающий на наличие страницы восстановления пароля.

Переходим по `/restore/` и видим три вопроса:

1. Логин — узнаем, что Мухтар запретил восстановление пароля, а Петро не делал этого.
2. E-mail — его можно узнать из таска Private data. Если вы уже решили этот таск, то найти данные можно двумя способами:
* из истории браузера, в котором решался данный таск
* из JSON-данных о тасках, которые запрашивает браузер каждые 5 секунд
3. Секретный вопрос — из того же таска понимаем, что ответ — Russia

Получаем пароль и вводим его на главной странице, забираем флаг из сообщения от Мухтара.
