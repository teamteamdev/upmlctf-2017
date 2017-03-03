# Weird program

> Recently Dog Association had posted some «security program patch» to their products. But we analyzed it and found that there's no interesting things in it.
> 
> What is happening there? Please help us with this program
> 
> _Hint:_ Hmmm, many empty lines at the end.. Anyway, nothing interesting
> 
> _Hint2:_ Wow! They're not empty! There is spaces and tabs in this string!
>
> [Attachment](https://github.com/upmlctf/2017-quals/blob/master/weird-program/program.c)

## Write-up

В программе на C 19 строк и абсолютно ничего интересного. Даже неопытному человеку очевидно, что эта программа вряд ли выдаст флаг.

Однако, стоит отметить, что на самом деле в файле 60 строк. Большая часть строк заполнена табами и пробелами. Да и в самой программе есть весьма странные отступы.

Всё это намекает на то, что использовался эзотерический [язык Whitespace](https://ru.wikipedia.org/wiki/Whitespace). Запустив программу в любом интерпретаторе ([пример](https://ideone.com/), получаем флаг.

### Альтернативное решение

Код программы на Whitespace обладал очень странной особенностью — если перевести все пробелы в нули, а табы — в единицы, получится также правильный ответ.

Флаг: `uctf_whitespace_is_best_lang`
