@echo off
net session >nul 2>&1
if not "%errorLevel%" == "0" (
  echo Oops: This tools must run with administrator permissions!
  echo it will popup the UAC dialog, please click [Yes] to continue.
  echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
  echo UAC.ShellExecute "%~s0", "%*", "", "runas", 1 >> "%temp%\getadmin.vbs"
  "%temp%\getadmin.vbs"
  exit /b 2
)
cd /d %~dp0
if "%PROCESSOR_ARCHITECTURE%"=="x86" (set ppath=%cd%\x86) else (set ppath=%cd%\x64)
echo 配置Python环境变量
set path=%ppath%\Python27;%ppath%\Python27\Scripts;%path%
copy %ppath%\dll\python27.dll %SystemRoot%\System32
cd %ppath%\whl
python -m pip install --no-index --find-links=%ppath%\whl  -r requirements.txt
copy %ppath%\Python27\Lib\site-packages\pywin32_system32 %SystemRoot%\System32 /y
cd /d %~dp0\U3DAutomatorClient
python script_handler.py
pause