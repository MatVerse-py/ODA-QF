install:
	python -m pip install --no-cache-dir -r requirements.txt || (echo "⚠️ pip install falhou; veja README.md em 'Instalação em ambientes restritos' para alternativas." && exit 1)
	cd contracts && npm install

test:
	pytest -q
	cd contracts && npx hardhat test

run:
	python server.py

monitor:
	cd monitoring && docker-compose up -d
