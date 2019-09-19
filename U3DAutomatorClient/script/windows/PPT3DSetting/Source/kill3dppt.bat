@echo off

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if '%errorlevel%' NEQ '0' (

goto UACPrompt

) else ( goto gotAdmin )

:UACPrompt

echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"

echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"

exit /B

:gotAdmin

if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
taskkill /F /IM 3DPPT.exe /T
taskkill /F /IM 3DCefClients.exe /T
taskkill /F /IM Losdkserver.exe /T
taskkill /F /IM soffice.bin /T
taskkill /F /IM soffice.exe /T
taskkill /F /IM lo.exe /T