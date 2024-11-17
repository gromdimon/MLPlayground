/*
 * This is the implementation of the Transaction class for the blockchain.
 * 
 * Compilation:
 * g++ -o blockchain Transaction.cpp -lssl -lcrypto
 */

#include "Transaction.h"
#include <sstream>
#include <iomanip>

Transaction::Transaction(const std::string& sender, 
                       const std::string& recipient, 
                       double amount)
    : sender(sender),
      recipient(recipient),
      amount(amount),
      timestamp(std::time(nullptr)),
      signature("")
{
}

void Transaction::setSignature(const std::string& sig) {
    signature = sig;
}

std::string Transaction::toString() const {
    std::stringstream ss;
    ss << "Transaction:\n"
       << "  From: " << sender << "\n"
       << "  To: " << recipient << "\n"
       << "  Amount: " << std::fixed << std::setprecision(2) << amount << "\n"
       << "  Time: " << std::put_time(std::localtime(&timestamp), 
                                    "%Y-%m-%d %H:%M:%S") << "\n";
    return ss.str();
} 