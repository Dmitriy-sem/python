from os import mkdir, chdir, getcwd


text = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./src/css/style.css">
    <title>Title</title>
</head>
<body>
    <script src="./src/js/main.js"></script>
</body>
</html>
"""
with open('index.html', 'w') as file:
    for i in text:
        file.write(i)


mkdir('src')
chdir('src')
mkdir('js')
mkdir('css')
mkdir('img')

chdir('js')
open('main.js', 'w').close()
chdir(getcwd()[:-3])
chdir('css')
open('style.css', 'w').close()


