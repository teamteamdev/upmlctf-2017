# One more letter

> Our agent has brought a new letter from dogs. And we can't read it again! Help us!
> 
> _Hint:_ this encryption method came from ancient times and it requires an one number key
>
> [Attachment](crypted.bin)

## Write-up

Это, конечно же, не `bin`-файл, а текст. Подсказка о древнем шифре и ключе в виде одного числа сильно скоращает спектр доступных шифров.

Методом перебора приходим к тому, что это [шифр Скитала](https://ru.wikipedia.org/wiki/Скитала) c ключом (количеством букв, которые помещаются по длине окружности), равным 7.

Отдельную сложность представляет выделение флага из расшифрованного текста: нужная часть выделялась из контеста так, чтобы после её удаления остался связный текст.

Флаг: `uctfbestcipher`
