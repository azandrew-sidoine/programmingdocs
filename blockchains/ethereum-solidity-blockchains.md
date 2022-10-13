# Ethereum - Solidity - Blockchains

## Requirement

To create a dAPP (decentralized application) we need to create a Wallet. An Easy way to create a wallet is by using MetaMask browser plugin.

- EtherScan

It's a Block explorer that allow ethereum users to view transactions that happens in the blockchain.

EtherScan is a web tool for reading transaction and other information about a given address.

- Accounts

With the dAPP created, developpers can add multiple account attached to it.
Each account has a private key that we revealed to the outside world, other user can perform transactions on the account.

**Warning** - Security concerns
    Mnemonic - Access all accounts - Should be protected
    Private Key - Access to 1 account - Should be protected
    Public Key  - Access Nothing - No need to protected it

- Rinkeby Test Network

Testing Ethereum network for testing ethereum application. To fund your testing wallet, we must follow some tweet instruction.

**Note**
    Funding wallet on a testing network does not affect the wallet on the Main Ethereum Network.

- Gas

Gas is a unit of computational measure. The more computation a transaction uses the more `gas` you must pay. For every transaction that happends on-chain a `gas-fee` is paid to node operators.

Note: Transaction processing at Node level is prioritize based on the gaz measurement. If the `Transaction fee` is high, it's likely to be processed faster.
The more people wat to make transactions, the higher the gas price, and therefore the higher transaction fee.

A gas is factor of computation resources.

- Gas Price

How much it costs per unit of gas

- Gas Limit

Max amount of gas in a transaction

- Transaction fee

`Tr_Fee = Gas * Gas_Price`

## Basics

- Mining

It's the process of finding the solution to the blockchain problem.
Node gets paid for mining or computation operations they perform.

- Nonce

`Number used once` to find a `solution` to the blockchain problem. It's also used to determine the transction number for an Address/Account.

- Block

Miners runs computational intensive operations to hash a block, by determining a `nonce` value for the block hash to starts with `0000`

```yml
Block:
    - id: string # Block number
    - Nonce: int # Compute by Mining algorithm to make sure the generated hash starts with 0000
    - Data: string # Data to be encoded
```

- Block Chain

A block chain is a linked list with the current block points to the hash value of the previous block. The root of the list is called `Genesis Block`.

Note: The genesis block previous hash value equals `000000000000...`;

```yml
BlockStruct:
    - id: string # Block number
    - Nonce: int # Compute by Mining algorithm to make sure the generated hash starts with 0000
    - Data: string # Data to be encoded
    - previous: string
```

BLockChain = BlockStruct -> BlockStruct -> BlockStruct -> BlockStruct ...

The chain is what makes the transaction secure... When a bloc changes in the bloc chain, the chain is no more valid.

- Distributed

Each node(a.k.a) has the same copy of the chain in the ethereum network.

Nodes in the cluster will use RAFT Consensus (The more having same chain data) will win over other chain if their data is tampered.

Note:
    `Data` is database of transansaction that are processed, have been processed in the network. That's why the data must be immutable.

- Private key - Public key algorightm

BlockChain use the asymmetric ECDSA(Elliptic Curve Digital Signature Algorithm) algorithm.
The asymmetric keys are used to sign transactions to make sure they are not tampered at a given point in time.

Transaction_Bloc: FixedLength<string> = Has_Func(Bloc);
ETH_Addr = Hash_Func(ETH_Public_Key)
ETH_Public_Key = ECDSA_Encrypt_Func(ETH_Private_Key)

- Consensus

It's the mechanism used to agree on the state of a blockchain.

1) Chain selection
Process to determine which block chain is the real block chain. BLock chain implementations uses the Nakmoto consensus to determine proof of work and Proof of state.

The larger the blockchain, the more likely it's to be accepted as blockchain.

2) Sybil Resistance
It's the mechanism make by the blockchain nodes to identify malicious treat trying to gain disproportion advantage influence in the system.

- Proof of Work
The process of mining to find the nonce value for the current block chain.

Note: The first Node to be able to compute the solution to the problem and find find the transaction and process it.

- Sybil attack
A user creates a large number of anonymous account to try to influence the network.

- 51% Attack
Because the blockchain elected by the network as valid blockchain is the chain with largest transaction, if a malicious user manage to gain at least 51% of the vote it can be able to make the network thing it is the main blockchain.

- PoS (Proof of Stake) (ETH 2.0)

Put up collateral as sybil resistance mechanism. It use less computation resources than Proof of Work.

1) Validators
Node are randomly choosen to propose solution to the block chain problem.

- Scalability

ETH 2.0 implements sharding the in the ethereum network. ETH 2.0 becomes a block chain of block chains. This greatly increase the transaction processing time.

-- Layered architecture

Layer 1 - Layer 1 blockchain are the base implementation of the Blockchain standard (ETH, Bitcoin, etc...)

Layer 2 - Layer 2 blockchain are application built on to of layer 1 block chains.

Rollups - Derive their security feature from Layer 1 blockchain an still send transations to be process into Layer 1 chains.

## Solidity Programming Language

Solidity is a compiled OOP language. Every solidity source code must start with the language version definitions. The syntax follows semantic versionification.

```sol
pragma solidity ^0.60;
```

- Constract

Contrat is the high level user defined type definition. It's like class in other programming languages

```sol
pragma solidity ^0.6.6;

contract SimpleStorage {
    // Contract definitions
}
```

- Solidity type system & Variable definitions

> uint<SIZE> - Whole number of the given size
> bool - For Thruthy values
> string - Text strings
> int<SIZE> -  Signed Whole number
> address - Hexadecimal ETH addreses
> bytes<SIZE> - bytes of characters . Note: 1>=SIZE<=32.

Note: Solidity variables are initialized by default to the type default values.

Syntax:

> <TYPE_DEF> [<VISIBILITY_>] <VARIABLE_NAME> [= <VALUE_>]

```sol
pragma solidity ^0.6.6;

contract SimpleStorage {
    uint64 amount; // Creates an unsigned 64bits integer
    string name; // Creates an empty string
    address source = 0x983402795292;
}
```

- Solidity user defined types

Solidity makes use of `struct` to define composite type juste like in c programming language

```sol
contract SimpleStorage {

    // ...
    struct People {
        string name;
        string lastname;
    }

    // Creating instance of people
    People public person = People({name: "", lastname: ""});
}
```

Note:
By default every member of a solidity contract is private.

- Solity lists [`Arrays`]

For working with list in solidity we can create arrays.

> <DATA_TYPE>[size] <TYPE_MODIFIER> variableName; // `size` can be omitted to create a dynamic size array

```sol
contract SimpleStorage {

    // ...
    struct People {
        string name;
        string lastname;
    }

    // Creating instance of people
    People[] public people; // Initialize the array to empty
    People[2] public people2; // Fixed size array
}
```

-- Array methods

> <LIST_VARIABLE>.push(<VALUE_>); // Push an item to the list
> <LIST_VARIABLE>.lenght - Returns the length of the array

- Conditionals

In Solidity we can performs condition checking using `if...else` statements.

```sol
contract ContractClass {

    function doSomething(unint256 memory value) public {
        if (value <= 10) {
            // Do something
        } else {
            // Else block
        }
    }
}
```

- Looping

Solidity support C style loops and smart for loops.

```sol
contract ContractClass {
    address[] funders;

    function doSomething(unint256 memory value) public {
        for(uint256 index=0; index<funders.length; index++) {
            // Do something
        }
    }
}
```

- Method / functions

Syntax:

function func_name([...PARAMETERS]) [<VISIBILITY_>] {
    // Function definitions
}

```sol
contract SimpleStorage {
    unint256 number;

    function store(unint256 _number) public {
        number = _number;
    }
}
```

- Dictionnary

Hash map is defines using `mapping` keyword

> mapping(TKey => TValue) <TYPE_MODIFIER> variableName;

```sol
contract SimpleStorage {
    unint256 number;

    // Creates a map of string -> uint256 for storing key value paired data
    mapping(string => uint256) public dictionary;

    function store(string memory name , unint256 _number) public {
        dictionary[name] = _number;
    }
}
```

- Solidity storage type

There are two storage type used by solidity VM.

> memory - Data will be store during the execution of a given function or contract calls
> storage - Like static variable persists data after function call

- View functions

function func_name([...PARAMETERS]) [<VISIBILITY_>] view returns(<RETURN_TYPE>) {
    // Function definitions
    return <STATE_VALUE>
}

Function parameter syntax is as follow:

> <DATA_TYPE> [<MEMORY_TYPE>] <VARIABLE_NAME>

```sol
contract SimpleStorage {

    struct People {
        string name;
        string lastname;
    }

    // Creating instance of people
    People[] public people; // Initialize the array to empty

    function addPerson(string memory name, string memory lastname) {
        people.push(People({name: name, lastname: lastname}));
    }
}
```

Views are non-state changing function. They act like state getter function to contract's properties. They do not causes transaction call.

**Note**
    When a variable is declared public, solidity compile internally create a view function internaly for reading the contract state.

- Pure function

Pure function are used to do computational tasks and returns or not a value.

function func_name([...PARAMETERS]) [<VISIBILITY_>] pure {
    // Function definitions
    // Performs mathematic compiutation
}

- Visibility

-- External - external members are part of the contract interface, meaning they can be called by other contract or via trasactions. They cannot be called internally like by the same contract.

-- Public - Part of the contract interface and are internally called or via messages

-- internal - Only accessed internally by contract defining them of derived contracts

-- Private - Visible inside the contract only

Note: Whenever we call a function or change state of a contract we are making a transaction.

**Note**
    Variable defines inside function are always internal the declaring function

## Solidity Licence declaration

Solidity encourage to add/use a machine readable SPDX Licence identifier on top of solidity source files:

```sol
// SPDX-Licence-Identifier: MIT
```

The compiler will include the supplied string the the source-code file to add legal copyrights information to source code.

## Smart contract deployment

Use the directive on [https://docs.chain.link/docs/link-token-contracts] to deploy a new created contract.
