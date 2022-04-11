```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/GTxRV303eCPRDQ2Qi2Ru8AW1RANvctkb accounts=10 mnemonic=brownie port=8545

brownie test --network mainnet-fork
```
