```
npm install -g ganache-cli

brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/GTxRV303eCPRDQ2Qi2Ru8AW1RANvctkb accounts=10 mnemonic=brownie port=8545



```

## Brownie CLI Commands

```
brownie console --network mainnet-fork
brownie test --network mainnet-fork
brownie compile
brownie accounts list
brownie accounts new freecodecamp-account
brownie accounts delete freecodecamp-account
brownie networks delete mainnet-fork
brownie run .\scripts\deploy_lottery.py

brownie test -k test_get_entrance_fee
brownie test -k test_get_entrance_fee --network rinkeby

brownie test -k test_can_pick_winner --network rinkeby -s
```

## Faucets

https://faucets.chain.link/kovan
https://faucets.chain.link/rinkeby

## Prettier Solidity

https://github.com/prettier-solidity/prettier-plugin-solidity#readme

### VSCode

VSCode is not familiar with the solidity language, so [`solidity`](https://marketplace.visualstudio.com/items?itemName=JuanBlanco.solidity) support needs to be installed.

```Bash
code --install-extension JuanBlanco.solidity
```

This extension provides basic integration with Prettier for most cases no further action is needed.

Make sure your editor has format on save set to true.
When you save VSCode will ask you what formatter would you like to use for the solidity language, you can choose `JuanBlanco.solidity`.

At this point VSCode's `settings.json` should have a configuration similar to this:

```JSON
{
  "editor.formatOnSave": true,
  "solidity.formatter": "prettier", // This is the default so it might be missing.
  "[solidity]": {
    "editor.defaultFormatter": "JuanBlanco.solidity"
  }
}
```

If you want more control over other details, you should proceed to install [`prettier-vscode`](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode).

```Bash
code --install-extension esbenp.prettier-vscode
```

To interact with 3rd party plugins, `prettier-vscode` will look in the project's npm modules, so you'll need to have `prettier` and `prettier-plugin-solidity` in your `package.json`

```
npm install --save-dev prettier prettier-plugin-solidity
```

This will allow you to specify the version of the plugin in case you want to use the latest version of the plugin or need to freeze the formatting since new versions of this plugin will implement tweaks on the possible formats.

You'll have to let VSCode what formatter you prefer.
This can be done by opening the command palette and executing:

```
>Preferences: Configure Language Specific Settings...

# Select Language
solidity
```

Now VSCode's `settings.json` should have this:

```JSON
{
  "editor.formatOnSave": true,
  "[solidity]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

Note: By design, Prettier prioritizes a local over a global configuration. If you have a `.prettierrc` file in your porject, your VSCode's default settings or rules in `settings.json` are ignored ([prettier/prettier-vscode#1079](https://github.com/prettier/prettier-vscode/issues/1079)).

## Edge cases

Prettier Solidity does its best to be pretty and consistent, but in some cases it falls back to doing things that are less than ideal.

### Modifiers in constructors

Modifiers with no arguments are formatted with their parentheses removed, except for constructors. The reason for this is that Prettier Solidity cannot always tell apart a modifier from a base constructor. So modifiers in constructors are not modified. For example, this:

```solidity
contract Foo is Bar {
  constructor() Bar() modifier1 modifier2() modifier3(42) {}

  function f() modifier1 modifier2 modifier3(42) {}
}

```

will be formatted as

```solidity
contract Foo is Bar {
  constructor() Bar() modifier1 modifier2() modifier3(42) {}

  function f() modifier1 modifier2 modifier3(42) {}
}

```

Notice that the unnecessary parentheses in `modifier2` were removed in the function but not in the constructor.
