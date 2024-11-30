# PythonDayTimeProject
An executable batch file python program which shows the day and time of the searched place.

The repository has two files:
1. "DayTime.bat" is the main executable batch file, which will run the "DayTimePython.pyw" python code file.
2. "DayTimePython.pyw" is the file, which contains the python code of the program.

1. "DayTime.bat" breakdown:
-pythonw: A Windows-specific interpreter that runs Python scripts without opening a console window.
Can be used with both .py and .pyw files to suppress the console.
-pyw: A file extension designed for Python scripts intended to run without a console window on Windows.
When double-clicked, .pyw files are automatically executed using pythonw.exe.

The batch file ensures that the script runs in a no-console mode and if you’re working in an environment where .pyw is not correctly associated with pythonw.exe (e.g., a misconfigured system), using pythonw ensures the no-console behavior.
