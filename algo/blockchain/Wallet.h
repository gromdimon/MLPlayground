#pragma once
#include <string>
#include <vector>
#include <memory>
#include <openssl/rsa.h>
#include <openssl/pem.h>

/**
 * @brief Represents a wallet in the blockchain system
 * 
 * Handles:
 * - Key pair generation and management
 * - Transaction signing
 * - Balance tracking
 * - Fund transfers
 */
class Wallet {
private:
    std::string id;                    // Wallet identifier
    double balance;                    // Current balance
    std::unique_ptr<RSA, void(*)(RSA*)> privateKey;  // Private key for signing
    std::unique_ptr<RSA, void(*)(RSA*)> publicKey;   // Public key for verification

    /**
     * @brief Generates RSA key pair for the wallet
     * @throws std::runtime_error if key generation fails
     */
    void generateKeyPair();

    /**
     * @brief Signs data using the private key
     * @param data Data to sign
     * @return Signature as string
     */
    std::string sign(const std::string& data) const;

public:
    /**
     * @brief Constructs a new Wallet
     * @param id Wallet identifier
     * @throws std::runtime_error if initialization fails
     */
    explicit Wallet(const std::string& id);

    /**
     * @brief Creates a new transaction to transfer funds
     * @param recipient Recipient's wallet address
     * @param amount Amount to transfer
     * @return Created and signed transaction
     * @throws std::runtime_error if insufficient funds or signing fails
     */
    Transaction createTransaction(const std::string& recipient, double amount);

    /**
     * @brief Updates wallet balance based on blockchain transactions
     * @param transactions Vector of transactions to process
     */
    void updateBalance(const std::vector<Transaction>& transactions);

    /**
     * @brief Verifies a transaction signature
     * @param transaction Transaction to verify
     * @return true if signature is valid
     */
    bool verifyTransaction(const Transaction& transaction) const;

    // Getters
    std::string getId() const { return id; }
    double getBalance() const { return balance; }
    std::string getPublicKey() const;  // Returns public key in PEM format

    // Prevent copying of wallets
    Wallet(const Wallet&) = delete;
    Wallet& operator=(const Wallet&) = delete;
};
