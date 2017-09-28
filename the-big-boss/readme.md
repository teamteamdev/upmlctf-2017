# The Big Boss

> Our secret dog agent told about there is Muhtar's portrait in each Dog Association Office.
> 
> We took its photo, but, as for me, there's nothing interesting for you.
> 
> Just look at this face and go to other tasks.
> 
> _Hint:_ flag consists of two parts. Each part needs separate analysis.
> 
> _Hint2:_ we found that file has three different parts.
>
> [Attachment](https://github.com/upmlctf/2017/blob/master/the-big-boss/portrait.jpg)

## Write-up

### EXIF-заголовки
Одна из частей таска — EXIF-заголовки. В одном из них есть кусок `_the_flag` — это вторая часть флага.
Заметим, что для его просмотра не нужен специальный софт, достаточно стандартных свойств картинки.

### ZIP-архив
Скачав оригинал с [Пикабу](http://pikabu.ru/story/lokalkhvost_3006923), можно было обнаружить несоответствие размеров.

При просмотре файла в любом hex-редакторе можно было увидеть заголовки ZIP-архива. Именно с ним была склеена картинка.
Однако, при открытии архива файл flag.txt оказывается зашифрован. За паролем не нужно далеко идти: между двумя файлами
был дан md5-хеш пароля. Любая база данных md5-хешей скажет, что пароль от архива — 2017.

Флаг: `uctf_work_for_the_flag`
