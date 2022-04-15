// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage {

// SimpleStorage array (type) with visibility public and name simpleStorageArray
    SimpleStorage[] public simpleStorageArray;

    function createSimpleStorageContract() public {
        // create object of type SimpleStorage contract (from import) with name simpleStorage, this will be new SimpleStorage contract with no input
        SimpleStorage simpleStorage = new SimpleStorage();
        // adding simpleStorage variable to array
        simpleStorageArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        // Address from simpleStorageArray
        // ABI(Application Binary Interface) from import

        // SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        // simpleStorage.store(_simpleStorageNumber);
        // this line has an explicit cast to the address type and initializes a new SimpleStorage object from the address
        SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).store(_simpleStorageNumber);

        // this line simply gets the SimpleStorage object at the index _simpleStorageIndex in the array simpleStorageArray
        // simpleStorageArray[_simpleStorageIndex].store(_simpleStorageNumber);
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        // SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        // return simpleStorage.retrieve();
        // this line has an explicit cast to the address type and initializes a new SimpleStorage object from the address
        return SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).retrieve();

        // this line simply gets the SimpleStorage object at the index _simpleStorageIndex in the array simpleStorageArray
        // return simpleStorageArray[_simpleStorageIndex].retrieve(); 
    }
}