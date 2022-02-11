require('dotenv').config();
const HDWalletProvider = require("@truffle/hdwallet-provider");
const { API_URL, API_URL_Test, MNEMONIC } = process.env;

module.exports = {
  networks: {
    development: {
      host: "localhost",
      port: 8545,
      network_id: "*"
    },
    rinkeby: {
      provider: function() {
        return new HDWalletProvider(MNEMONIC, API_URL_Test)
      },
      network_id: 4,
//      gas: 1000000 //4M is the max
    },
    mainnet: {
      provider: function() {
        return new HDWalletProvider(MNEMONIC, API_URL)
      },
      network_id: 1,
//      gas: 1000000 //4M is the max
    }
  },
  compilers: {
    solc: {
      version: "^0.8.0",
      settings: {
        optimizer: {
          enabled: true, // Default: false
          runs: 200      // Default: 200
        },
      }
    }
  },
  plugins: ['truffle-plugin-verify'], //PLUGIN ADDED HERE
  api_keys: {
    etherscan: process.env.ETHERSCAN_API_KEY
  }
};