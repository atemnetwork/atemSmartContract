const AtemPassport = artifacts.require("AtemRefund");

module.exports = function(deployer) {
  deployer.deploy(AtemPassport, baseURL);
};