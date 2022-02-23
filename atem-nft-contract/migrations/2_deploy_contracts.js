const AtemPassport = artifacts.require("AtemPassport");
const baseURL = "https://gateway.pinata.cloud/ipfs/QmR8cPsZCxJxj9bVtPfdhWg6xpuaqpEHRXMi82y5uhjesx/"

module.exports = function(deployer) {
  deployer.deploy(AtemPassport, baseURL);
};