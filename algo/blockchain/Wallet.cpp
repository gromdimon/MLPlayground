/*
 * This is the implementation of the Wallet class for the blockchain.
 * 
 * Compilation:
 * g++ -o wallet Wallet.cpp -lssl -lcrypto -std=c++17
 */

#include "Wallet.h"
#include <iostream>
#include <stdexcept>
#include <sstream>
#include <openssl/pem.h>
#include <openssl/err.h>

// Custom deleter for RSA pointers
static void RSA_deleter(RSA* rsa) {
    if (rsa) RSA_free(rsa);
}

Wallet::Wallet(const std::string& id)
    : id(id),
      balance(0.0),
      privateKey(nullptr, RSA_deleter),
      publicKey(nullptr, RSA_deleter) 
{
    generateKeyPair();
}

void Wallet::generateKeyPair() {
    // Initialize OpenSSL's random number generator
    if (RAND_load_file("/dev/urandom", 32) != 32) {
        throw std::runtime_error("Failed to initialize random number generator");
    }

    // Create key generation context
    BIGNUM* bne = BN_new();
    if (!BN_set_word(bne, RSA_F4)) {
        BN_free(bne);
        throw std::runtime_error("Failed to set public exponent");
    }

    // Generate RSA key pair
    RSA* rsa = RSA_new();
    if (!RSA_generate_key_ex(rsa, 2048, bne, nullptr)) {
        BN_free(bne);
        RSA_free(rsa);
        throw std::runtime_error("Failed to generate RSA key pair");
    }
    BN_free(bne);

    // Store private key
    privateKey.reset(rsa);

    // Extract public key
    RSA* pub_key = RSAPublicKey_dup(rsa);
    if (!pub_key) {
        throw std::runtime_error("Failed to extract public key");
    }
    publicKey.reset(pub_key);
}

std::string Wallet::sign(const std::string& data) const {
    if (!privateKey) {
        throw std::runtime_error("Private key not initialized");
    }

    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, data.c_str(), data.length());
    SHA256_Final(hash, &sha256);

    std::vector<unsigned char> signature(RSA_size(privateKey.get()));
    unsigned int sig_len;

    if (!RSA_sign(NID_sha256, hash, SHA256_DIGEST_LENGTH,
                  signature.data(), &sig_len, privateKey.get())) {
        throw std::runtime_error("Failed to sign data");
    }

    return std::string(signature.begin(), signature.begin() + sig_len);
}

Transaction Wallet::createTransaction(const std::string& recipient, double amount) {
    if (amount > balance) {
        throw std::runtime_error("Insufficient funds");
    }

    Transaction tx{id, recipient, amount, std::time(nullptr)};
    
    // Create transaction data string
    std::stringstream ss;
    ss << tx.sender << tx.recipient << tx.amount << tx.timestamp;
    
    // Sign transaction
    tx.signature = sign(ss.str());
    
    return tx;
}

void Wallet::updateBalance(const std::vector<Transaction>& transactions) {
    for (const auto& tx : transactions) {
        if (tx.sender == id) {
            balance -= tx.amount;
        }
        if (tx.recipient == id) {
            balance += tx.amount;
        }
    }
}

bool Wallet::verifyTransaction(const Transaction& tx) const {
    if (!publicKey) {
        throw std::runtime_error("Public key not initialized");
    }

    // Recreate transaction data
    std::stringstream ss;
    ss << tx.sender << tx.recipient << tx.amount << tx.timestamp;
    std::string data = ss.str();

    // Calculate hash
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, data.c_str(), data.length());
    SHA256_Final(hash, &sha256);

    // Verify signature
    return RSA_verify(NID_sha256, hash, SHA256_DIGEST_LENGTH,
                     reinterpret_cast<const unsigned char*>(tx.signature.c_str()),
                     tx.signature.length(), publicKey.get()) == 1;
}

std::string Wallet::getPublicKey() const {
    BIO* bio = BIO_new(BIO_s_mem());
    PEM_write_bio_RSAPublicKey(bio, publicKey.get());
    
    char* pem_key = nullptr;
    long key_size = BIO_get_mem_data(bio, &pem_key);
    std::string result(pem_key, key_size);
    
    BIO_free(bio);
    return result;
}
