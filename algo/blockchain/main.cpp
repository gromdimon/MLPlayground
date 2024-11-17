/*
 * Blockchain Demo Application
 * 
 * This program demonstrates the functionality of a simple blockchain implementation
 * including wallet creation, transactions, mining, and chain validation.
 * 
 * Compilation:
 * g++ -o blockchain *.cpp -lssl -lcrypto -std=c++17
 */

#include <iostream>
#include <iomanip>
#include <thread>
#include <chrono>
#include "Blockchain.h"
#include "Wallet.h"

// Utility function to print blockchain information
void printChainInfo(const Blockchain& chain) {
    std::cout << "\n=== Blockchain Status ===" << std::endl;
    std::cout << "Number of blocks: " << chain.getChain().size() << std::endl;
    std::cout << "Is chain valid: " << (chain.isChainValid() ? "Yes" : "No") << std::endl;
    std::cout << "Mining difficulty: " << chain.getDifficulty() << std::endl;
    std::cout << "Mining reward: " << chain.getMiningReward() << " coins" << std::endl;
    std::cout << "Pending transactions: " << chain.getPendingTransactions().size() << std::endl;
    std::cout << "=====================\n" << std::endl;
}

// Utility function to print wallet information
void printWalletInfo(const std::string& name, const Wallet& wallet, const Blockchain& chain) {
    std::cout << "=== " << name << "'s Wallet ===" << std::endl;
    std::cout << "Address: " << wallet.getId() << std::endl;
    std::cout << "Balance: " << chain.getBalanceForAddress(wallet.getId()) << " coins" << std::endl;
    std::cout << "=====================\n" << std::endl;
}

int main() {
    try {
        std::cout << "Initializing blockchain...\n" << std::endl;
        
        // Create blockchain with difficulty 4 and mining reward 100
        Blockchain chain(4, 100.0);
        printChainInfo(chain);

        // Create wallets for different users
        std::cout << "Creating wallets..." << std::endl;
        Wallet miner("miner");
        Wallet alice("alice");
        Wallet bob("bob");
        Wallet charlie("charlie");

        // Display initial wallet balances
        std::cout << "\nInitial wallet states:" << std::endl;
        printWalletInfo("Miner", miner, chain);
        printWalletInfo("Alice", alice, chain);
        printWalletInfo("Bob", bob, chain);
        
        // Mine first block to get some coins
        std::cout << "Mining first block..." << std::endl;
        chain.minePendingTransactions(miner.getId());
        std::cout << "Block mined!" << std::endl;
        
        // Show miner's reward
        printWalletInfo("Miner", miner, chain);

        // Create some transactions
        std::cout << "Creating transactions..." << std::endl;
        
        // Miner sends coins to Alice and Bob
        try {
            auto tx1 = miner.createTransaction(alice.getId(), 30.0);
            auto tx2 = miner.createTransaction(bob.getId(), 50.0);
            
            chain.addTransaction(tx1);
            chain.addTransaction(tx2);
            std::cout << "Transactions created successfully!" << std::endl;
        } catch (const std::exception& e) {
            std::cout << "Transaction error: " << e.what() << std::endl;
        }

        // Mine block with these transactions
        std::cout << "\nMining block with transactions..." << std::endl;
        chain.minePendingTransactions(miner.getId());
        
        // Show updated balances
        std::cout << "\nBalances after first set of transactions:" << std::endl;
        printWalletInfo("Miner", miner, chain);
        printWalletInfo("Alice", alice, chain);
        printWalletInfo("Bob", bob, chain);

        // Create more transactions
        std::cout << "\nCreating more transactions..." << std::endl;
        try {
            // Alice sends some coins to Bob
            auto tx3 = alice.createTransaction(bob.getId(), 10.0);
            chain.addTransaction(tx3);

            // Bob sends some coins to Charlie
            auto tx4 = bob.createTransaction(charlie.getId(), 25.0);
            chain.addTransaction(tx4);
            
            std::cout << "Transactions created successfully!" << std::endl;
        } catch (const std::exception& e) {
            std::cout << "Transaction error: " << e.what() << std::endl;
        }

        // Mine these transactions
        std::cout << "\nMining new block..." << std::endl;
        chain.minePendingTransactions(miner.getId());

        // Show final balances
        std::cout << "\nFinal balances:" << std::endl;
        printWalletInfo("Miner", miner, chain);
        printWalletInfo("Alice", alice, chain);
        printWalletInfo("Bob", bob, chain);
        printWalletInfo("Charlie", charlie, chain);

        // Verify chain integrity
        std::cout << "\nVerifying blockchain integrity..." << std::endl;
        if (chain.isChainValid()) {
            std::cout << "Blockchain is valid!" << std::endl;
        } else {
            std::cout << "Blockchain validation failed!" << std::endl;
        }

        // Print final chain information
        printChainInfo(chain);

        // Try an invalid transaction (spending more than available)
        std::cout << "\nTrying to create invalid transaction..." << std::endl;
        try {
            auto invalidTx = charlie.createTransaction(alice.getId(), 1000.0);
            chain.addTransaction(invalidTx);
        } catch (const std::exception& e) {
            std::cout << "Expected error occurred: " << e.what() << std::endl;
        }

    } catch (const std::exception& e) {
        std::cerr << "Fatal error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
