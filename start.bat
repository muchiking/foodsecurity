@echo on
REM Start PowerShell and execute the following commands
powershell -NoExit -Command "& {
    $env:VIRTUAL_ENV = '.\wenv';
    . .\wenv\Scripts\Activate.ps1;
    python .\my_tennis_club\manage.py runserver;
}"
