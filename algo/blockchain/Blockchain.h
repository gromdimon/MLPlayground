#pragma once
#include <vector>
#include <memory>
#include "Block.h"
#include "Transaction.h"
#include "Wallet.h"

/**
 * @brief Main blockchain class that manages blocks and transactions
 * 
 * Handles:
 * - Chain validation
 * - Block mining and addition
 * - Transaction verification and processing
 * - Chain integrity checks
 */
class Blockchain {
private:
    std::vector<Block> chain;              // The blockchain
    std::vector<Transaction> pendingTxs;   // Pending transactions
    int difficulty;                        // Mining difficulty
    double miningReward;                   // Reward for mining a block

    /**
     * @brief Gets the last block in the chain
     * @return Reference to the last block
     */
    const Block& getLastBlock() const;

public:
    /**
     * @brief Constructs a new Blockchain
     * @param difficulty Initial mining difficulty
     * @param miningReward Reward for mining a block
     */
    Blockchain(int difficulty = 4, double miningReward = 100.0);

    /**
     * @brief Adds a new transaction to pending transactions
     * @param transaction Transaction to add
     * @return true if transaction was added successfully
     */
    bool addTransaction(const Transaction& transaction);

    /**
     * @brief Mines pending transactions and adds new block to chain
     * @param minerAddress Address to receive mining reward
     */
    void minePendingTransactions(const std::string& minerAddress);

    /**
     * @brief Validates the entire blockchain
     * @return true if chain is valid
     */
    bool isChainValid() const;

    /**
     * @brief Gets balance for a wallet address
     * @param address Wallet address to check
     * @return Current balance
     */
    double getBalanceForAddress(const std::string& address) const;

    // Getters
    const std::vector<Block>& getChain() const { return chain; }
    const std::vector<Transaction>& getPendingTransactions() const { return pendingTxs; }
    int getDifficulty() const { return difficulty; }
    double getMiningReward() const { return miningReward; }
};
