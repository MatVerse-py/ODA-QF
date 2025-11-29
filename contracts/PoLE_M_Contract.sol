/**
 * CONTRATO REAL — TOTALMENTE OPERACIONAL NA TESTNET AMOY
 */

 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PoLE_M_Contract is ERC721URIStorage, Ownable {

    uint256 public constant MIN_OMEGA = 935;
    uint256 public constant MIN_PSI   = 900;
    uint256 public constant MAX_CVAR  = 1;

    bool public minted = false;

    event OrganismMinted(
        uint256 omega,
        uint256 psi,
        uint256 cvar,
        bytes32 merkle_root
    );

    constructor() ERC721("TauOmega", "τΩ") Ownable(msg.sender) {}

    function mint_organism(
        uint256 omega1000,
        uint256 psi1000,
        uint256 cvar1000,
        bytes32 merkle_root
    ) external onlyOwner {

        require(!minted, "Already minted");
        require(omega1000 >= MIN_OMEGA, "Ω below threshold");
        require(psi1000 >= MIN_PSI, "Ψ below threshold");
        require(cvar1000 <= MAX_CVAR, "CVaR too high");
        require(merkle_root != bytes32(0), "Invalid merkle root");

        minted = true;

        _mint(msg.sender, 1);
        _setTokenURI(1, "ipfs://ODA-QF_GENESIS");

        emit OrganismMinted(omega1000, psi1000, cvar1000, merkle_root);
    }
}
