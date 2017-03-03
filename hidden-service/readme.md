# Hidden service

> When you're passing our missions to save the world, they're inventing new methods to hide from us.
> 
> We were informed that Dog Association sends every dog in the world link to one site. But it seems down, because every page says that it's not found.
> 
> Is it fatal bug or great feature?
> 
> _Hint:_ how can server distinguish whether you use HTTP or HTTPS? Or maybe FTP?

## Write-up
На самом деле, несуществование сайта ещё ни о чем не говорит. Например, на этой машине сервер может быть запущен на другом порту (о чем и намекает подсказка).

Для перебора открытых портов идеально подходит программа [NMap](https://nmap.org/).

Она говорит об открытых портах 22, 80, 443, 1234, 6443 и 8082. Порт 22 занят для SSH, он не подходит. Порт 1234 уже знаком вам из другого таска.
Порты 80, 443 и 6443 не подходят, в чем мжоно убедиться перебором портов. Подходит лишь 8082 — на нем и находится флаг.

Флаг: `uctf_icaninscan`
