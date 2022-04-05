// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AtemRefund is Ownable {
    using SafeMath for uint256;

    uint256 private refundAmountPerUser = 3 * 10**17;
    address externalNFTContractAddress = 0x01BE23585060835E02B77ef475b0Cc51aA1e0709;

    IERC721 atemNFTV1 = IERC721(externalNFTContractAddress);
    address burnwallet = address(0);

    mapping(address => bool) public whitelist;
    mapping(uint256 => bool) public burnedList;

    bool private _pause;
    bool private _init_whitelist;
    uint256 private _whitelist_count = 0;
    uint256 private _burned_count = 0;
    
    constructor() {
        pause(false);
        _init_whitelist = false;
        _initwhitelist();
    }

    function burnAndRefund(uint256 tokenId) public payable {
        require(atemNFTV1.balanceOf(msg.sender) > 0, "no V1 NFT");
        require(!burnedList[tokenId], "already burned for this token id");
        require(whitelist[msg.sender], "not whitelist user");
        require(!_pause, "paused by owner");
        
        // burn a NFT first
        atemNFTV1.safeTransferFrom(msg.sender, burnwallet, tokenId);

        _widthdraw(msg.sender, refundAmountPerUser);
        burnedList[tokenId] = true;
        _burned_count = _burned_count + 1;
    }
    function _initwhitelist() private {
        require(!_init_whitelist, "Whitelist already initialized!");

        addwhitelist(0x71E084AB76a113727cdB1d10B0e9B1041a51eD07);
    
        _init_whitelist = true;
    }
    function getBurnedCount() public view returns (uint256) {
        return _burned_count;
    }
    function getWhitelistCount() public view returns (uint256) {
        return _whitelist_count;
    }
    function isPaused() public view returns (bool) {
        return _pause;
    }
    function getRefundAmountPerUser() public view returns (uint256) {
        return refundAmountPerUser;
    }
    function totalRefundAmount() public view returns (uint256) {
        return address(this).balance;
    }
    function pause(bool val) public onlyOwner {
        _pause = val;
    }
    function addwhitelist(address _addr) public onlyOwner {
        whitelist[_addr] = true;
        _whitelist_count = _whitelist_count + 1;

    }
    function setNFTContractAddress(address _nftContractAddress) public onlyOwner {
        atemNFTV1 = IERC721(_nftContractAddress);
    }
    function setRefundAmountPerUser(uint256 amount) public onlyOwner {
        refundAmountPerUser = amount;
    }
    function deposit() public payable onlyOwner {
        require(msg.value > 0);
    }
    function withdrawAll() public payable onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0);
        _widthdraw(msg.sender, address(this).balance);
    }
    function withdraw() public payable onlyOwner {
        uint256 balance = address(this).balance;
        require(balance >= msg.value);
        _widthdraw(msg.sender, msg.value);
    }
    function _widthdraw(address _address, uint256 _amount) private {
        (bool success, ) = _address.call{value: _amount}("");
        require(success, "Transfer failed.");
    }
}