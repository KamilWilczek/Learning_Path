// SPDX-License-Identifier: MIT

// Smart contract that lets anyone deposit ETH into the contract
// Only the owner of the contract can withdraw the ETH

pragma solidity >=0.6.6 <0.9.0;

// Interfaces compile down to an ABI
// ABI tells solidity what func can be called on antoher contracts

// Get the latest ETH/USD price from chainlink price feed
// import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
interface AggregatorV3Interface {
  function decimals() external view returns (uint8);
  function description() external view returns (string memory);
  function version() external view returns (uint256);

  // getRoundData and latestRoundData should both raise "No data present"
  // if they do not have data to report, instead of returning unset values
  // which could be misinterpreted as actual reported values.
  function getRoundData(uint80 _roundId)
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );

  function latestRoundData()
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );
}

// for less than pragma solidity 0.8
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    // safe math library check uint256 for integer overflows
    using SafeMathChainlink for uint256;

    // mapping to store which address depositeded how much ETH
    mapping(address => uint256) public addressToAmountFunded;
    // array of addresses who deposited
    address[] public funders;
    // address of the owner (who deployed the contract)
    address public owner;

    // constructor initializes automatically just after initialization of contract
    // the first person to deploy the contract is the owner
    constructor() public {
        owner = msg.sender;
    }

    // keyword payable 
    function fund() public payable {
        
        // $50
        // we use everything in gwei hence value*10**18
        // 18 digit number to be compared with donated amount 
        uint256 minimumUSD = 50 * 10 ** 18;

        // is the donated amount less than 50USD?
        // 1gwei < $50
        // if(msg.value < minimumUSD){
        //     revert?
        // } 
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");
        
        // msg.sender, msg.value are keyword that are always in every contract call in every transaction
        // masg.sender - sender of the function call
        // msg.value - how much they send
        // if not, add to mapping and funders array
        addressToAmountFunded[msg.sender] += msg.value;
        
        // what the ETh -> USD conversion rate
        funders.push(msg.sender);
    }

    // function to get the version of the chainlink pricefeed
    function getVersion() public view returns (uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331);
        (,int256 answer,,,) = priceFeed.latestRoundData();

        // ETH/USD rate in 18 digit 
        return uint256(answer * 10000000000);
    }

    // 1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;

        // the actual ETH/USD conversation rate, after adjusting the extra 0s.
        return ethAmountInUsd;
    }

    // modifier: https://medium.com/coinmonks/solidity-tutorial-all-about-modifiers-a86cf81c14cb
    modifier onlyOwner {

        // is the message sender owner of the contract?
        require(msg.sender == owner);
        // when underscore _ happens code of the function
        _;
    }

    // onlyOwner modifer will first check the condition inside it 
    // and 
    // if true, withdraw function will be executed 
    function withdraw() payable onlyOwner public {

        // whoever calls this function transfer them all money
        // only want the contract admin/owner
        // require msg.sender = owner
        // require(msg.sender == owner);
        msg.sender.transfer(address(this).balance);

        // iterate through all the mappings and make them 0
        // since all the deposited amount has been withdrawn
        for (uint256 funderIndex=0; funderIndex<funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        // funders array will be initialized to 0
        funders = new address[](0);
    }
}