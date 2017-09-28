# New organization

> They're growing!
> 
> Take a look: dogs have founded International Guide Dog Federation. They still try to proof that they love people. But only we know that it's false and our goal is to verify it.
> 
> One of our specialist brought lost flash drive to our office. It belongs to one of co-founders of this Federation. There is only a logotype on this drive. But do you see that it's strange?
> 
> Maybe that's not just a logotype...
> 
> _Hint:_ we remember that original file name started with brainco, but we missed the rest part.
> 
> [Attachment](https://github.com/upmlctf/2017/blob/master/new-organization/logo.png)

## Write-up
Можно найти оригинал картинки 200х200 (или сжать любой другой до такого размера). При сравнении картинок получается довольно странное изображение, в котором есть несколько особенностей:

* на второй картинке отличающийся от других пикселей монотонный фон по левому и правому краю в верхней половине
* некоторые "особые" пиксели также отличаются от других
* нижняя половина монотонна

Такая структура очень напоминает язык программирования Brainloller, и не зря.
Существует ещё одна известная модификация — язык [Braincopter](https://esolangs.org/wiki/Braincopter).
В нем команда вычисляется про формуле `(65536 * r + 256 * g + b) % 11`.
Запустим в любом интерпретаторе и получим флаг.

Флаг: `uctfexpertofbraincopter`
