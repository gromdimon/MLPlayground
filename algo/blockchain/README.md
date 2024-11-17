# Simple Blockchain Implementation

A C++ implementation of a basic blockchain system with wallet management, transaction processing, and proof-of-work mining.

## Features

### Core Components
- **Block**: Basic unit of the blockchain
  - Previous block hash
  - Transaction data
  - Timestamp
  - Nonce for mining
  - SHA256 hashing

- **Transaction**: Records transfers between wallets
  - Sender and recipient addresses
  - Amount
  - Timestamp
  - Digital signature

- **Wallet**: Manages user accounts
  - RSA key pair generation
  - Transaction signing
  - Balance tracking
  - Secure key storage

- **Blockchain**: Main chain management
  - Block mining and validation
  - Transaction processing
  - Chain integrity verification
  - Mining rewards

### Security Features
- RSA public/private key cryptography
- Digital signatures for transactions
- SHA256 hashing for blocks
- Proof-of-work mining
- Chain validation

## Building and Running

### Prerequisites
- C++17 compatible compiler
- OpenSSL library
- Make (optional)

### Installation
1. Install OpenSSL development libraries:
```bash
# Ubuntu/Debian
sudo apt-get install libssl-dev

# macOS
brew install openssl
```

2. Compile the project:
```bash
# Using g++
g++ -o blockchain *.cpp -lssl -lcrypto -std=c++17

# Or using the provided Makefile
make
```

### Usage Example
```cpp
// Create a blockchain
Blockchain chain(4);  // difficulty = 4

// Create wallets
Wallet alice("alice_address");
Wallet bob("bob_address");

// Create and add transaction
Transaction tx = alice.createTransaction(bob.getId(), 50.0);
chain.addTransaction(tx);

// Mine pending transactions
chain.minePendingTransactions(alice.getId());

// Check balances
std::cout << "Alice's balance: " << chain.getBalanceForAddress(alice.getId()) << std::endl;
std::cout << "Bob's balance: " << chain.getBalanceForAddress(bob.getId()) << std::endl;
```

## Project Structure
```
blockchain/
├── Block.h          # Block class definition
├── Block.cpp        # Block implementation
├── Transaction.h    # Transaction class definition
├── Transaction.cpp  # Transaction implementation
├── Wallet.h         # Wallet class definition
├── Wallet.cpp       # Wallet implementation
├── Blockchain.h     # Blockchain class definition
├── Blockchain.cpp   # Blockchain implementation
└── README.md        # This file
```

## Implementation Details

### Mining Process
1. Block mining uses proof-of-work with adjustable difficulty
2. Mining reward is given for successfully mining a block
3. All pending transactions are included in the mined block

### Transaction Flow
1. Wallet creates and signs transaction
2. Transaction is added to pending transactions
3. Miner includes transaction in new block
4. Block is mined and added to chain
5. Balances are updated

### Security Considerations
- Private keys never leave the wallet
- All transactions are signed
- Chain integrity is regularly verified
- Proof-of-work prevents tampering

## Limitations
- Simple implementation for educational purposes
- No networking/distributed consensus
- Basic transaction model
- In-memory storage only

## Future Improvements
- Persistent storage
- Network communication
- Merkle tree for transactions
- Smart contracts
- Better mining difficulty adjustment