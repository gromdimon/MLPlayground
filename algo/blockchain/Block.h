#pragma once
#include <string>
#include <vector>
#include <ctime>

/**
 * @brief Represents a block in the blockchain
 * 
 * Each block contains:
 * - Hash of previous block
 * - Timestamp
 * - Transaction data
 * - Nonce for mining
 * - Current block's hash
 */
class Block {
private:
    std::string prevHash;      // Previous block's hash
    std::string currentHash;   // Current block's hash
    std::string data;          // Transaction data
    std::time_t timestamp;     // Block creation time
    int nonce;                 // Mining nonce
    int difficulty;            // Mining difficulty (number of leading zeros required)

    /**
     * @brief Calculates hash of the block
     * @return SHA256 hash of block contents
     */
    std::string calculateHash() const;

public:
    /**
     * @brief Constructs a new Block
     * @param data Transaction data
     * @param prevHash Previous block's hash
     * @param difficulty Mining difficulty
     */
    Block(const std::string& data, const std::string& prevHash, int difficulty);

    /**
     * @brief Mines the block by finding a valid nonce
     */
    void mineBlock();

    // Getters
    std::string getPrevHash() const { return prevHash; }
    std::string getCurrentHash() const { return currentHash; }
    std::string getData() const { return data; }
    std::time_t getTimestamp() const { return timestamp; }
    int getNonce() const { return nonce; }

    // Validation
    bool isValid() const;
};
