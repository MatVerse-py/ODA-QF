const hre = require("hardhat");

async function main() {
  const Contract = await hre.ethers.getContractFactory("PoLE_M_Contract");
  const contract = await Contract.deploy();
  await contract.waitForDeployment();

  console.log("PoLE-M deployed at:", await contract.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
