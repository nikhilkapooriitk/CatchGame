set hour=360000
set /a counter=0

:loop
start "" "python" "main.py"
start /wait "" "python" "main.py"
set /a counter=%counter% + 1
if %counter% LSS %hour% goto loop
