открой проект в visual studio code (or webstorm) и убедись что у тебя установлен node.js. 

npm --version
node --version

Потом установи зависимости проекта (при выполнении команды убедись что терминал смотрит в папку frontend):
npm install vite@5 @vitejs/plugin-react@4 --save-dev



npm run dev - чтобы потестить локально на фронте
npm run build - скомпилить файлы в папке assets будет результат их надо положить в бэк, дима скажет куда
