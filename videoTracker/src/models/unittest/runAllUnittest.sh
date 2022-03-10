@echo off
goto :runUnittests


:runUnittests
echo ***********runing unittiest: test_Liste.py***********************
python -m unittest -v test_Liste.py
echo ***********runing unittiest: test_FileRepo.py********************
python -m unittest -v test_FileRepo.py
echo ***********runing unittiest: test_Point.py***********************
python -m unittest -v test_Point.py
pause
goto runCoverage

:runCoverage
WHERE coverage
IF %ERRORLEVEL% NEQ 0 goto INSTALLCOVERAGE
echo ***********runing coverage: test_FileRepo.py test_Liste.py test_Point.py****************
coverage run -m unittest test_FileRepo.py test_Liste.py test_Point.py
coverage html --precision=2
coverage report --precision=2  --show-missing
coverage report --precision=2  --show-missing >coverageReport.txt
pause
goto END

:INSTALLCOVERAGE
echo "!!!!coverage is not installed -> installing coverage!!!!!"
pip install coverage
echo !!!!coverage is now installed!!!!!
goto runCoverage

:END