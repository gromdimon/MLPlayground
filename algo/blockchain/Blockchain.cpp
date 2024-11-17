#include "Blockchain.h"
#include <stdexcept>

Blockchain::Blockchain(int difficulty, double miningReward)
    : difficulty(difficulty), 
      miningReward(miningReward) 
{
    // Create genesis block
    chain.emplace_back(Block("Genesis Block", "", difficulty));
}

const Block& Blockchain::getLastBlock() const {
    if (chain.empty()) {
        throw std::runtime_error("Blockchain is empty");
    }
    return chain.back();
}

bool Blockchain::addTransaction(const Transaction& transaction) {
    // Verify transaction signature
    Wallet senderWallet(transaction.getSender());
    if (!senderWallet.verifyTransaction(transaction)) {
        return false;
    }

    // Check if sender has sufficient funds
    if (getBalanceForAddress(transaction.getSender()) < transaction.getAmount()) {
        return false;
    }

    pendingTxs.push_back(transaction);
    return true;
}

void Blockchain::minePendingTransactions(const std::string& minerAddress) {
    // Create mining reward transaction
    Transaction rewardTx("System", minerAddress, miningReward);
    pendingTxs.push_back(rewardTx);

    // Create new block with pending transactions
    std::string transactions_str;
    for (const auto& tx : pendingTxs) {
        transactions_str += tx.toString();
    }

    Block newBlock(transactions_str, getLastBlock().getCurrentHash(), difficulty);
    chain.push_back(newBlock);

    // Clear pending transactions
    pendingTxs.clear();
}

bool Blockchain::isChainValid() const {
    for (size_t i = 1; i < chain.size(); i++) {
        const Block& currentBlock = chain[i];
        const Block& previousBlock = chain[i - 1];

        // Verify block hash
        if (!currentBlock.isValid()) {
            return false;
        }

        // Verify chain linkage
        if (currentBlock.getPrevHash() != previousBlock.getCurrentHash()) {
            return false;
        }
    }
    return true;
}

double Blockchain::getBalanceForAddress(const std::string& address) const {
    double balance = 0;

    // Check all blocks for transactions involving this address
    for (const auto& block : chain) {
        std::string blockData = block.getData();
        // Note: In a real implementation, you would parse the transaction data
        // and update the balance accordingly
        // This is a simplified version
    }

    return balance;
}
