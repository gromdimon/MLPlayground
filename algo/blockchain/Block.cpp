/*
 * This is the implementation of the Block class for the blockchain.
 * 
 * Compilation:
 * g++ -o blockchain Block.cpp -lssl -lcrypto
 */

#include "Block.h"
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

Block::Block(const std::string& data, const std::string& prevHash, int difficulty) {
    this->data = data;
    this->prevHash = prevHash;
    this->timestamp = std::time(nullptr);
    this->difficulty = difficulty;
    this->nonce = 0;
    mineBlock();
}

void Block::mineBlock() {
    std::string target(difficulty, '0');  // Create target string with leading zeros
    
    do {
        nonce++;
        currentHash = calculateHash();
    } while (currentHash.substr(0, difficulty) != target);
}

std::string Block::calculateHash() const {
    std::stringstream ss;
    ss << prevHash 
       << std::put_time(std::gmtime(&timestamp), "%Y-%m-%dT%H:%M:%S")
       << data 
       << nonce;
    
    return sha256(ss.str());
}

std::string Block::sha256(const std::string str) const {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.size());
    SHA256_Final(hash, &sha256);

    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

bool Block::isValid() const {
    // Verify the current hash matches a recalculated hash
    return currentHash == calculateHash() && 
           currentHash.substr(0, difficulty) == std::string(difficulty, '0');
}
