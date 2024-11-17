#pragma once
#include <string>
#include <ctime>

/**
 * @brief Represents a transaction in the blockchain
 * 
 * Contains:
 * - Sender's wallet ID
 * - Recipient's wallet ID
 * - Amount transferred
 * - Timestamp
 * - Digital signature
 */
class Transaction {
private:
    std::string sender;       // Sender's wallet ID
    std::string recipient;    // Recipient's wallet ID
    double amount;           // Amount to transfer
    std::time_t timestamp;   // Transaction timestamp
    std::string signature;   // Digital signature of the transaction

public:
    /**
     * @brief Constructs a new Transaction
     * @param sender Sender's wallet ID
     * @param recipient Recipient's wallet ID
     * @param amount Amount to transfer
     */
    Transaction(const std::string& sender, 
               const std::string& recipient, 
               double amount);

    /**
     * @brief Signs the transaction with given signature
     * @param sig Digital signature to set
     */
    void setSignature(const std::string& sig);

    // Getters
    std::string getSender() const { return sender; }
    std::string getRecipient() const { return recipient; }
    double getAmount() const { return amount; }
    std::time_t getTimestamp() const { return timestamp; }
    std::string getSignature() const { return signature; }

    /**
     * @brief Creates string representation of transaction data
     * @return String containing transaction details
     */
    std::string toString() const;

    // Friend class declarations
    friend class Wallet;
    friend class Block;
    friend class Blockchain;
};
