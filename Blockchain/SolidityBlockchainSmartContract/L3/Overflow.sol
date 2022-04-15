// SPDX-License-Identifier: MIT

// for lower than 0.8
pragma solidity ^0.6.0;

contract Overflow {

    function overflow() public view returns(uint256){
        uint8 big = 255 + uint8(100);
        return big;
    }
}