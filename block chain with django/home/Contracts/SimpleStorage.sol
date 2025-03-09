// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;  // Check this version

contract SimpleStorage {
    uint256 private storedData;

    function set(uint256 _data) public {
        storedData = _data;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
