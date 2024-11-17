# Compiler settings
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
LDFLAGS = -lssl -lcrypto

# Source files
SRCS = main.cpp Block.cpp Transaction.cpp Wallet.cpp Blockchain.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = blockchain

# Detect OS for OpenSSL include path
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    # macOS (Homebrew OpenSSL path)
    CXXFLAGS += -I/usr/local/opt/openssl@3/include
    LDFLAGS += -L/usr/local/opt/openssl@3/lib
endif

# Targets
.PHONY: all clean run

all: $(TARGET)

# Link the target
$(TARGET): $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET) $(LDFLAGS)

# Compile source files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Run the blockchain demo
run: $(TARGET)
	./$(TARGET)

# Clean build files
clean:
	rm -f $(OBJS) $(TARGET)

# Debug build
debug: CXXFLAGS += -g -DDEBUG
debug: clean all

# Help target
help:
	@echo "Available targets:"
	@echo "  make        - Build the blockchain executable"
	@echo "  make run    - Build and run the blockchain demo"
	@echo "  make clean  - Remove build files"
	@echo "  make debug  - Build with debug symbols"
	@echo "  make help   - Show this help message" 