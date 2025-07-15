@echo off
for %%f in (data\*) do if not "%%~nxf"==".gitignore" del /Q "%%f"
rmdir /S /Q dist
pyinstaller --onefile --name "GoExport Outro Maker" --icon ./assets/icon.ico ^
 --add-data "data;data" --add-data "dependencies;dependencies" ^
 --hidden-import=modules.logger --hidden-import=modules.processor ^
 .\main.py
copy readme.md dist\
copy LICENSE dist\
xcopy assets dist\assets /E /I /Q /Y