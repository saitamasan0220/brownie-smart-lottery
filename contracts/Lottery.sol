// SPDX-License-Identifier: MIT
pragma solidity ^0.6.6;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract Lottery {

 address payable[] public players;
 uint256 public usdEntryFee;
 AggregatorV3Interface internal ethUsdPriceFeed;

 constructor(address _priceFeedAddress) public {
  usdEntryFee = 50;
  ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
 }
 function enter() public payable {
  // $50 minimum
  players.push(msg.sender);

 }

 function getEthPriceInDollars() public view returns (uint256){
  (,int price,,,) = ethUsdPriceFeed.latestRoundData();

  uint256 adjustedPrice = uint256(price) / ( 10 ** 8 ); // 18 decimals, conver to wei

  return adjustedPrice;
 }

 function getEntranceFee() public view returns (uint256){ // in wei
  // (,int price,,,) = ethUsdPriceFeed.latestRoundData();

  // uint256 adjustedPrice = uint256(price) * 10 ** 10; // 18 decimals, conver to wei

  // $50, $2000 / ETH
  // uint256 costToEnter = (usdEntryFee * 10 ** 18) / adjustedPrice;

  // ======================================================
  // uint256 ethPriceInDollars = getEthPriceInDollars();
  // uint256 costToEnter = (usdEntryFee / ethPriceInDollars) * 10**18;
  // return costToEnter;

  uint costToEnter = getWeiPriceFromDollar(usdEntryFee);
  return costToEnter;
 }

 function getWeiPriceFromDollar(uint256 dollarAmount) public view returns (uint256){
  uint256 ethPriceInDollars = getEthPriceInDollars();

  uint256 dollarAmountInWei = ((dollarAmount * 10**18) / ethPriceInDollars) ; // 
  return dollarAmountInWei;
 }

 function startLottery() public{}
 function endLottery() public {}
}
