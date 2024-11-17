from trie import Trie


def main():
    print("Aho-Corasick Algorithm")
    # Keywords to construct the Trie with
    keywords = ["lol", "scam", "pump", "dump", "cryptocurrency", "bitcoin", "ethereum"]
    # Text to search within
    text = "pump and dump scam is a common occurrence in the cryptocurrency world."

    # Initialize the Trie and construct it with the keywords
    trie = Trie()
    trie.construct(keywords)

    found_keywords = trie.search(text)

    print("Found keywords and their positions:")
    for keyword, position in found_keywords:
        print(f"'{keyword}' found at position {position}")


if __name__ == "__main__":
    main()
