# Project under development

> Dogs have hired people to develop «dogs communicating platform». Hmmm.. you are human too, you should know what tools they use. Maybe you can look for something useful?
>
> _Hint:_ the project is still in development, maybe there is somewhat that is bad for production?
> 
> _Hint2:_ we've found out that they're control versions of code

## Write-up
Ничего интересного на [главной странице](index.htm) нет, поэтому поищем что-нибудь ещё.

Информация о том, что проект ещё в разработке может говорить либо о дебаг-версии и лишних файлах, либо о системе контроля версий.

Подтверждается второй факт. Так, теперь нам нужно достать флаг без листинга директорий на сервере. Начнем исследовать git:

Шаг 0. Создадим у себя папку `.git`, в которую будем сохранять все найденные файлы. Положим туда все эти файлы: `HEAD`, `objects/info/packs`, `description`, `config`, `COMMIT_EDITMSG`, `index`, `packed-refs`, `refs/heads/master`, `refs/remotes/origin/HEAD`, `refs/stash`, `logs/HEAD`, `logs/refs/heads/master`, `logs/refs/remotes/origin/HEAD`, `info/refs`, `info/exclude`.

Шаг 1. [/.git/logs/refs/heads/master](git/logs/refs/heads/master)
Это — история коммитов в ветке `master`. Давайте посмотрим, что же изменялось в этих коммитах. Смысла в последнем нету, начнем со среднего.

Шаг 2. [/.git/objects/cc/a2f8091301c60f02e8adfc087b35b02a416769](git/objects/cc/a2f8091301c60f02e8adfc087b35b02a416769)
Это — файл второго коммита. Файлы в git хранятся так: директория — первые два символа хеш-суммы, файл — последние 38.
Чтобы посмотреть его, запустим такую команду в родительской директории для `.git`:

`$ git cat-file -p 6916ae52c0b20b04569c262275d27422fc4fcd34`
```
tree 43f38a5db238d136c5076d550b234caadacceb35
parent 25371f5431f7741b439cf404ccfca6c74913868c
author Ubuntu <ubuntu@nsychev.ru> 1488220103 +0500
committer Ubuntu <ubuntu@nsychev.ru> 1488220103 +0500

improvements
```

Шаг 3. [/.git/objects/43/f38a5db238d136c5076d550b234caadacceb35](git/objects/43/f38a5db238d136c5076d550b234caadacceb35)
Это — дерево, хранящее изменения, относящиеся к нашему коммиту

`$ git cat-file -p 43f38a5db238d136c5076d550b234caadacceb35`
```
100644 blob 6dae25ed1a68a1c097cd5aea62a369b166223769    index.htm
```

Шаг 4. [/.git/objects/6d/ae25ed1a68a1c097cd5aea62a369b166223769](git/objects/6d/ae25ed1a68a1c097cd5aea62a369b166223769)
Это — изменение файла index.htm, оно нам и нужно.

`$ git cat-file -p 6dae25ed1a68a1c097cd5aea62a369b166223769`
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Dog Communicating Platform</title>
    <link rel="stylesheet" href="https://ctf.upml.tech/ui/semantic.min.css" />
  </head>
  <body style="margin: 10px;">
    <h1 class="ui header">Dogs communicating platform</h1>
    <p>Secret code: <code>uctf_git_is_useful</code></p>
  </body>
</html>
```

Также существуют утилиты, позволяющие облегчить или автоматизировать процесс.

Флаг: `uctf_git_is_useful`

