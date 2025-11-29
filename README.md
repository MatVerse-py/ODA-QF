# 🧬 ODA-QF — Organismo Digital Autônomo Antifrágil Quântico-Fractal

Repositório oficial do primeiro organismo digital verificável governado por:
- Antifragilidade (Ω)
- Coerência semântica (Ψ)
- Risco de cauda mínimo (CVaR)
- Auditoria integral (Cassandra Ledger)
- Prova de existência on-chain (PoLE-M → τΩ)

## 🚀 Execução rápida

```
make install
make test
make run
make monitor
```

## 🛠️ Instalação em ambientes restritos

- Ambiente offline ou com proxy bloqueando o PyPI?
  1) Verifique se o proxy corporativo libera `https://pypi.org/simple` e exporte as variáveis `HTTPS_PROXY`/`https_proxy`.
  2) Se ainda falhar, faça o download manual dos wheels (fastapi, uvicorn, numpy, pytest, requests) em uma máquina com acesso e instale apontando para a pasta local:
     ```
     python -m pip install --no-index --find-links /caminho/para/wheels -r requirements.txt
     ```
  3) O alvo `make install` aborta com uma mensagem amigável se o pip não conseguir baixar os pacotes; consulte esta seção para as alternativas.

Métricas:
```
curl localhost:8000/metrics
```

Deploy contrato:
```
cd contracts
npx hardhat run deploy_pole_m.js --network polygonAmoy
```

## 📊 Telemetria
Prometheus + Grafana
Dashboard em: monitoring/grafana-dashboard.json

## 🔗 PoLE-M
Contrato real, compilável e implantável em testnet.
Mint gera: OrganismMinted(Ω, Ψ, CVaR, MerkleRoot)
