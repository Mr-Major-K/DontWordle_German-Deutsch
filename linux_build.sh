pyinstaller --hidden-import Flask --add-data "./words.txt:." --add-data "./static/js/*:static/js" --add-data "./static/css/*:static/css" --add-data "./static/*:static" --add-data "./templates/*:templates" --icon=DontWordle_German-Deutsch/static/favicon.ico --paths ../venv/lib/python3.10/site-packages/ --onefile --console ./app.py

cd ./dist/

cp ../words.txt .

cd ..

touch "IN DEM DIST ORDNER IST DIE AUSFÜHRBARE DATEI".txt