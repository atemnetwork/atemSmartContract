const AtemPassport = artifacts.require("AtemPassport");
const baseURL = "https://gateway.pinata.cloud/ipfs/QmTuycV3jsLQ6Ep1Nk5JjboEeVTHYqkfZoV8ZYNxTtHGCt/"

module.exports = function(deployer) {
  deployer.deploy(AtemPassport, baseURL);
};