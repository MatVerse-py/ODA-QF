const { expect } = require("chai");

describe("PoLE_M_Contract", function () {
  it("Deploys correctly", async function () {
    const Contract = await ethers.getContractFactory("PoLE_M_Contract");
    const contract = await Contract.deploy();
    await contract.waitForDeployment();
    expect(await contract.minted()).to.equal(false);
  });
});
