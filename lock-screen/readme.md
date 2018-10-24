# Lock screen

> Take a look! We found an utilized *gavphone*! Nevertheless, we have a trouble. It is protected by four-digit code. We provide you secure remote connection to the phone. Just log into it.
>
> Connect to server: `nc ctf.upml.tech 1234`
>
> _Note:_ if you're using Windows, you can connect via Putty in Raw mode

## Write-up

Давайте хранить все корректные коды.

На каждом шаге будем запрашивать случайный корректный код и удалять все коды, не подходящие хотя бы под один запрос.

Жюри протестировало решение много раз, и, по статистике, оно удаляет не менее 2/3 доступных кодов на первых трех шагах (обычно даже более 80%). Это означает, что для 5 040 кодов в начале нам нужно всего 7-9 попыток (если мы очень неуспешны).

[Авторское решение](solution.py) за 1000 запусков ни разу не ошиблось и не превысило лимит на число попыток.

Вы получите флаг после 15 правильных кодов.

Флаг: `uctfimp0ssibletosolve`
