Инструкция по запуску:
1) Если ваш путь до папки project(папки внутри Backend_project) не C:\Games\Backend_project\project\, то вам нужно:
  а)Открыть docker-compose.yml(изпапки deploy) через блокнот
  б)В строке build: C:\Games\Backend_project\project\ поменять путь на ваш путь до папки project(папки внутри Backend_project)
  в)В строке volumes: C:\Games\Backend_project\project\:/usr/src/project/ поменять путь на ваш путь до папки project(папки внутри Backend_project)
2) Собрать проект в docker с помощью команды docker-compose build
3) Запустить проект с помощью команды docker-compose up -d
