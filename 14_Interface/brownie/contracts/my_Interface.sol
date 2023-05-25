// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;
interface Base1 {
    function getFirstName() external pure returns(string memory);
    function getLastName() external pure returns(string memory);
}
contract my_interface {
    Base1 my_inter; 
    
    constructor(address _add){
        my_inter = Base1(_add);
    }
    
    function getFN() external view returns(string memory){
        return my_inter.getFirstName();
    }

    function getLN() external view returns(string memory){
        return  my_inter.getLastName();
    }

}
