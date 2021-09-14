@echo on
dir /b *.ass > ass.txt

:set
setlocal EnableDelayedExpansion
set "CurrCD=%~dp0"
set "strOld=.ass"
set "strNew="
set x264=C:\Program Files (x86)\AviSynth+\plugins\x264_32_tMod-8bit-420.exe

:replace
::输出不带后缀的txt
for /f %%i in ('dir /b ass.txt') do ( powershell -Command "(gc %%i) -replace '%strOld%', '%strNew%' | Out-File %%i" )
pause