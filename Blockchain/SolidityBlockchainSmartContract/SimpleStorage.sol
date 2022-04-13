// SPDX-License-Identifier: MIT
pragma solidity >0.6.0 <0.9.0;

// something like class in Python
contract SimpleStorage {

    // defining variable
    // uint256 favouriteNumber = 5;
    // bool favouriteBool = true;
    // string favouriteString = 'String';
    // // unlike uint this one can be negative or positive
    // int256 favouriteInt = -5;
    // address favouriteAddress = 0xf36e894fC749b7A9193b44E26B70b9D6C85BBBDb;
    // // bytes2, bytes3 and so on till bytes 32
    // bytes32 favourtieBytes = 'cat';

    // it will get initialized to null value i.e. =0
    // public - visibility keyword, default - internal
    // uint256 public favouriteNumber;
    uint256 favouriteNumber;
    bool favouriteBool;

    // creates newb object
    struct People {
        uint256 favouriteNumber;
        string name;
    }

    // array
    People[] public people;
    
    // mapping
    mapping(string => uint256) public nameToFavouriteNumber;

    // People public person = People({favouriteNumber: 2, name: 'Patric'});

    function store(uint256 _favouriteNumber) public {
        favouriteNumber = _favouriteNumber;
        // uint256 test = 4;
    }

    // // store2 does not know about uint256 test
    // function store2() public {

    // }
    // view - reading of the blockchain, we do not make tx, public is technically view func
    // pure - does some type of math, also do not change state of blockchain, do not make tx
    function retrieve() public view returns(uint256) {
        return favouriteNumber;
    }

    // types of storage, memory - during executuion of func or cotrnacrt, storage longer
    function addPerson(string memory _name, uint256 _favouriteNumber) public {
        // people.push(People(_favouriteNumber, _name));
        people.push(People({favouriteNumber: _favouriteNumber, name: _name}));
        nameToFavouriteNumber[_name] = _favouriteNumber;
    }

}