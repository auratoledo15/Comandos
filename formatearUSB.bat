@echo off

set /P letra=letra_unidad
set /P formato=formato_unidad
set /P label=nombre_del_dispositivo
format %letra% /FS:%formato% /v:%label% /q
pause