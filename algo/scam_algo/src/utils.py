import pickle
from typing import Dict, List, Tuple

import ahocorasick  # type: ignore
from pydantic import BaseModel


class AhoCorasickAutomaton(BaseModel):
    automaton: ahocorasick.Automaton = None

    class Config:
        arbitrary_types_allowed = True

    def construct_automaton(self, keywords: Dict[str, float]) -> None:
        """
        Constructs the Aho-Corasick automaton from the given keywords.

        :param keywords: dictionary of keywords and their weights
        :type keywords: Dict[str, float]
        """
        self.automaton = ahocorasick.Automaton()
        for keyword, weight in keywords.items():
            self.automaton.add_word(keyword, (keyword, weight))
        self.automaton.make_automaton()

    def search(self, text: str) -> List[Tuple[str, float]]:
        """
        Searches the given text for keywords using the Aho-Corasick automaton.

        :param text: input text to search
        :type text: str
        :return: list of found keywords and their weights
        :rtype: List[Tuple[str, float]]
        """
        results = []
        for end_index, (keyword, weight) in self.automaton.iter(text):
            results.append((keyword, weight))
        return results

    def save_to_file(self, path: str) -> None:
        """
        Saves the constructed automaton to a file using pickle.
        """
        with open(path, "wb") as file:
            pickle.dump(self.automaton, file)

    @classmethod
    def load_from_file(cls, path: str) -> "AhoCorasickAutomaton":
        """
        Loads the automaton from a file using pickle.
        """
        with open(path, "rb") as file:
            automaton = pickle.load(file)
        instance = cls()
        instance.automaton = automaton
        return instance


# Example usage
# if __name__ == "__main__":
#     keywords = {"example": 0.5, "test": 0.4}
#     automaton_instance = AhoCorasickAutomaton()

#     # Option 1: Construct the automaton if it's not loaded
#     automaton_instance.construct_automaton(keywords)
#     automaton_instance.save_to_file("automaton.pickle")

#     # Option 2: Load the automaton using pickle
#     loaded_automaton_instance = AhoCorasickAutomaton.load_from_file("automaton.pickle")
#     search_results = loaded_automaton_instance.search("test string with example and test")

#     for keyword, weight in search_results:
#         print(f"Found {keyword} with weight {weight}.")
