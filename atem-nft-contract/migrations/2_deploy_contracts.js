const SnowGlobe = artifacts.require("SnowGlobe");
const baseURL = "https://gateway.pinata.cloud/ipfs/QmR8cPsZCxJxj9bVtPfdhWg6xpuaqpEHRXMi82y5uhjesx/"

module.exports = function(deployer) {
  deployer.deploy(SnowGlobe, baseURL);
};