// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Payment {

    // Hash map of addresses that send eth|wei|gwei to the smart contract
    mapping(address => uint256) public addresses;

    function receive() public payable {
        addresses[msg.sender] += msg.value;
    }
}
