# What do they mean?

> Hm... One more «only-for-dogs»-labeled site...
> 
> Why are they so selfish? They can't make one website for all, can they? It's just not tolerantly towards to cats.
> 
> They spread between dogs information about a method how to log into this site. Can you guess this method?
> 
> _Hint:_ we use HTTP protocol to view the pages. What methods does it have?

# Write-up

Слово method достаточно часто употребляется в [HTTP](https://en.wikipedia.org/wiki/HTTP) — протоколе, по которому передаются веб-страницы.
Клиент выбирает HTTP-метод в зависимости от действия, которое он хочет сделать. Из основных есть `GET`, `POST`, `PUT`, `HEAD`, `OPTIONS`, `DELETE`.

Флаг выдавался сервером при запросе по методу `PUT`. Произвольные запросы из браузера можно отправлять, например, [так](https://www.hurl.it/)

Флаг: `uctf_use_put_instead_of_get`
