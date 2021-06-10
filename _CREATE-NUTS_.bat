cls
call python scripts/generate-freight-graphics-ALL.py
call Combine-NML.py
cd scripts
call process_intro_dates.py
cd ..
call compile.bat
pause