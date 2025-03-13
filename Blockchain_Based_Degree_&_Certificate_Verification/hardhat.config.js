require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",  // Solidity version (make sure it's compatible with your contracts)
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545",
    },
  },
};
