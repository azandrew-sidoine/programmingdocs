# Advance concepts

Recall:

`Wei` is the small unit of currency in the ETH network.

## Importing or Modularizing solidity source code

To include a solidity contract into solidity:

```sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./path/to/ContractFile.sol";

contract StorageFactory {

}
```

## Creating an instance of a contract

Because contract are class, we can create instance of contract using the `new` keyword. Creating an instance of a given contract return the hex address to where the contract is deployed to.

```sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./path/to/ContractFile.sol";

contract StorageFactory {
    ContractClass[] public contracts;

    function createContract() public {
        ContractClass contract = new ContractClass();
        contracts.push(contract);
    }

}
```

## Calling contract public method from another contract

In order to interact with a contract, we must have the address of the contract `hex value of the deployment` and the contract `ABI (Application Binary Interface)` callable members of the contract.

```sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./path/to/ContractFile.sol";

contract StorageFactory {
    ContractClass[] public contracts;

    function createContract() public {
        ContractClass contract = new ContractClass();
        contracts.push(contract);
    }

    function callStore(address index, uint256 _number) public {
        ContractClass c = ContractClass(address(contracts[index]));
        // This assume that the contract has retrieve method
        c.store(_number);
    }

}
```

**Note**

`address()` is a type casting function to convert a contract to it address representation.

## Inheritance

Solidity language support the OOP inheritance feature as well. To make a class a class inherite from a given class:

> contract <SUB_CLASS> is <BASE_CLASS> {} - `is` keyword is used to perform inheritance.

```sol
// ...
contract ContractClass is BaseContractClass {
    // Code defintion
}
```

## Payment

Functions can be declared payable. If a function is payable, they can be use to pay.

In every ethereum transactions, solidity save information about the source address and the amount of the transaction in an object called `msg` ; 

```yml
msg:
    - sender: Transaction source
    - value: Transaction currency value
    - data: Data send
    - gas: gas
```

## Block chain oracle

Because blockchain are isolated from external world we need a source of interaction on top of it. That's where the BlockChain Oracle comes in.

It's a device that interact with the off-chain world to provide external data or computation to smart contracts.

* Chaining (Decentralized Oracle Network)

Full replicas being run by independent and sybil resistant node operators, coming to consensus about a computation.

Chainlink focus on data validation and consensus about individual off-chain values to make them reliable enough to trigger contracts.

Node operators are security reviewed, can provide a provden performance history and high quality and highly sybil resitant.

[https://data.chain.link] provides a data feeds about currency from ethereum or blockchain oracles.

[https://docs.chain.link] provides documentation about working with external computation or chainlink providers.

**Note**

    Solidity codes are deployed on npm repository. To import from npm repository:

```sol
import "@scope/library/path/to/solidity/contract"

// Solidity code
```

## Interfaces

Solidity provides Interfaces for defining function and members that a contract might have.

Interface in solidity like in other programming language just has function declaration not the definition of the function.

Interfaces compile down to ABI, defining functions that can be called on a given contract.

```sol
// ...
interface SmartContractInterface {
    function(uint256 memory _number) public;

    function (string memory name) public views returns (string memory);
}
```

## Tuple

Solidity language support tuple data type as python programming language:

> (<DATA_TYPE> value1, <DATA_TYPE2> value2) = contract.callFunc()

```sol
contract Payment {

    function() public view returns(unint256) {
        (
            ,
            int256 price,
            ,
        ) = contract.getPrice()
    }
}
```

**Warning**

    When performing calculation, make sure to consider overflows to avoid loosing number part if number overflowed.

* Using keyword

Using keyword are directives in the form of `using A for B` for attaching library functions (from library A) to any type `B` in the context of a contract.

## Require statement

It's an alternative to `if` condition that fails or stop exection if condition is not met.

> require(<CONDITION_TO_EVALUATE>, <"Message">); 

## Sending Fund to Contract Address

> msg.sender - Refers to the address of the one who query for the message
> sender.transfer() - Message sender has a transfer() method to transfering amount to wallet
> address(contract).balance - Returns the current balance of the contract address

```sol

contract ContractClass {
    function withdraw() payable public {
        msg.sender.transfer(address(this).balance)
    }
}
```

## Who is the owner of the smart contract?

When a contract is deployed, it calls the contract constructor. To get the owner address we access the `msg.sender` property in the constructor call.

```sol

contract Payment {

    address public owner;

    // Constructor 
    constructor() {
        owner = msg.sender;
    }

    // Function to withdraw contract balance
    withdraw() payable public {
        // Here we make sure it's only the address of the owner which
        // can withdraw the balance of the contract
        require(msg.sender == owner, "Sorry you don't have the authorization required");
        msg.sender.transfer(address(this).balance);
    }
}
```

## Modifiers

They allows to modify the definition of a function in a declarative way. Modifier are like middlewares/decorators that run before or after a function block.

```sol

contract Payment {

    address public owner;

    // Constructor 
    constructor() {
        owner = msg.sender;
    }

    modifier isOwner() {
        // The modifier execute the require() statement first and the function
        // block later
        require(msg.sender == owner, "Sorry you don't have the authorization required");
        _; 
    }

    // Function to withdraw contract balance
    withdraw() payable public {
        // Here we make sure it's only the address of the owner which
        // can withdraw the balance of the contract
        require(msg.sender == owner, "Sorry you don't have the authorization required");
        msg.sender.transfer(address(this).balance);
    }

    // We apply the decorator or middleware to the function
    modifiedFunc() payable isOwner public {
        msg.sender.transfer(address(this).balance);
    }
}
```
