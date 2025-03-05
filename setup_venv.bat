@echo off
set VENV_PATH=C:\Users\danie\OneDrive\Coding\Projects\Blog\venv
mkdir %VENV_PATH%
xcopy /E /I "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.752.0_x64__qbz5n2kfra8p0\Lib\venv\scripts\nt" "%VENV_PATH%\Scripts"
xcopy /E /I "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.752.0_x64__qbz5n2kfra8p0\Lib\venv\scripts\common" "%VENV_PATH%\Scripts"
copy "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.752.0_x64__qbz5n2kfra8p0\python.exe" "%VENV_PATH%\Scripts\python.exe"
echo Virtual environment setup completed.
REM Activate the virtual environment
call "%VENV_PATH%\Scripts\activate.bat"
