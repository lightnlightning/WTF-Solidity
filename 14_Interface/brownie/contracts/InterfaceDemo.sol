// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;
interface Base1 {
    function getFirstName() external pure returns(string memory);
    function getLastName() external pure returns(string memory);
}
contract BaseImpl1 is Base1{
    uint public a = 13;
    function getFirstName() external pure override returns(string memory){
        return "Amazing";
    }
    function getLastName() external pure override returns(string memory){
        return  "Ang";
    }
}
