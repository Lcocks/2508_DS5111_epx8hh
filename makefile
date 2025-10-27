default:
	@cat makefile
  
env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt
	bash -c "source env/bin/activate && pip install -r requirements.txt"

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"; cd bin && python3 my_normalizer.py

.PHONY: ygainers_tstamp
ygainers_tstamp: ygainers.csv
	cd bin && mv normalized_ygainers.csv ../ygainers_`date +"%Y%m%d_%H%M%S"`.csv

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"; cd bin && python3 my_normalizer.py

.PHONY: wsjgainers_tstamp
wsjgainers_tstamp: wsjgainers.csv
	cd bin && mv normalized_wsjgainers.csv ../wsjgainers_`date +"%Y%m%d_%H%M%S"`.csv

.PHONY: clean
clean:
	rm wsjgainers.html wsjgainers.csv ygainers.html ygainers.csv | true # using a | true here because incase the wsjgainers* files are not present it will still succeed in running (won't fail out).

lint:
	. env/bin/activate; pylint bin/my_normalizer.py

test: lint
	. env/bin/activate; pytest -vv tests/

linttest: lint test
