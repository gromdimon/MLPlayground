import json
import logging
import time
from pathlib import Path
from typing import Dict, List

import spacy
import yaml  # type: ignore

# TODO: Change the import for tests
from .utils import AhoCorasickAutomaton

# from scam_algorithm.src.utils import AhoCorasickAutomaton

# Local constants
LOGGING_LEVEL = logging.DEBUG  # logging.INFO for production
MODEL_NAME = "en_core_web_sm"
KEYWORDS_FILE_PATH = "config/scam_keywords.yml"
GROUP_WEIGHT_FILE_PATH = "config/scam_keywords_weights.json"
AUTOMATON_PATH = "config/ac_automaton.pickle"

# Configure logging (DEBUG level for development | INFO level for production)
logging.basicConfig(
    level=LOGGING_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s"
)


class ScamDetector:
    """
    This class is used to detect scam messages based on keywords.

    Attributes:
    - nlp: spaCy model
    - ahocorasick_model: AhoCorasickAutomaton model
    - group_weights: weights for different scam groups
    - scam_keywords: dictionary of scam keywords and their weights

    Methods:
    - _load_keywords_weights: load keywords weights from the JSON file
    - _preprocess_and_lemmatize: preprocess and lemmatize the input text
    - _load_and_lemmatize_keywords: load and lemmatize keywords from the YAML file
    - _load_automaton_model: load the AhoCorasickAutomatonModel from the JSON file
    - construct_automaton_model: construct and save the AhoCorasickAutomatonModel
    - check_keywords: check the input text for scam keywords
    - calculate_scam_score: calculate the scam score for the input text
    """

    def __init__(
        self,
        model_name: str,
        keywords_file_path: str,
        group_weight_file_path: str,
        automaton_path: str = "",
    ) -> None:
        """
        The constructor for ScamDetector class.

        :param model_name: name of the spaCy model to use
        :type model_name: str
        :param keywords_file_path: path to the YAML file with scam keywords
        :type keywords_file_path: str
        :param group_weights: weights for different scam groups
        :type group_weights: dict
        """
        logging.debug("Loading spaCy model...")
        self.nlp = spacy.load(model_name)
        self.ahocorasick_model: AhoCorasickAutomaton | None = None
        self.group_weights: Dict[str, float] = {}
        self.scam_keywords: Dict[str, float] = {}

        # Set up the keywords
        if not self._check_path_exists(
            keywords_file_path
        ) or not self._check_path_exists(group_weight_file_path):
            raise FileNotFoundError(
                "Keywords file or group weight file does not exist."
            )
        self._load_keywords_weights(group_weight_file_path)
        self._load_and_lemmatize_keywords(keywords_file_path)

        # Set up the automaton model
        if self._check_path_exists(automaton_path):
            self._load_automaton_model(automaton_path)
        else:
            self._construct_automaton_model(automaton_path)
        logging.debug("ScamDetector initialized.")

    @staticmethod
    def _check_path_exists(path: str) -> bool:
        """
        Check if the provided path exists.

        :param path: Path to check
        :type path: str
        :return: True if the path exists, False otherwise
        :rtype: bool
        """
        path_obj = Path(path)
        return path_obj.exists()

    def _load_keywords_weights(self, group_weight_file_path: str) -> None:
        """
        Load keywords weights from the JSON file.
        """
        with open(group_weight_file_path, "r") as file:
            self.group_weights = json.load(file)

    def _preprocess_and_lemmatize(self, text: str) -> List[str]:
        """
        Preprocess and lemmatize the input text.
        """
        doc = self.nlp(text.lower())
        return [token.lemma_ for token in doc]

    def _load_and_lemmatize_keywords(self, keywords_file_path: str) -> None:
        """
        Load and lemmatize keywords from the YAML file.
        """
        with open(keywords_file_path, "r") as file:
            data = yaml.safe_load(file)
        self.scam_keywords = {}
        for group, phrases in data["scam_keywords"].items():
            for phrase in phrases:
                lemmatized_phrase = " ".join(self._preprocess_and_lemmatize(phrase))
                self.scam_keywords[lemmatized_phrase] = self.group_weights.get(
                    group, 0.1
                )

    def _load_automaton_model(self, automaton_model_path: str) -> None:
        """
        Load the AhoCorasickAutomatonModel from the JSON file.
        """
        logging.debug("Loading AhoCorasickAutomatonModel...")
        start_time = time.time()
        loaded_automaton_instance = AhoCorasickAutomaton.load_from_file(
            automaton_model_path
        )
        self.ahocorasick_model = loaded_automaton_instance
        logging.debug(
            f"AhoCorasickAutomatonModel loaded in {round(time.time() - start_time, 8)} seconds."
        )

    def _construct_automaton_model(self, path: str) -> None:
        """
        Construct and save the AhoCorasickAutomatonModel.
        """
        logging.debug("Constructing AhoCorasickAutomatonModel...")
        # TODO: For production, consider removing the time logging
        start_time = time.time()
        automaton_instance = AhoCorasickAutomaton()
        automaton_instance.construct_automaton(self.scam_keywords)
        automaton_instance.save_to_file(path)
        self.ahocorasick_model = automaton_instance
        logging.debug(
            f"AhoCorasickAutomatonModel constructed in {round(time.time() - start_time, 8)} seconds."
        )

    def check_keywords(self, text: str) -> float:
        """
        Check the input text for scam keywords.

        :param text: input text to check
        :type text: str
        :return: scam score
        :rtype: float
        """
        logging.debug(f"Checking text for scam keywords: {text}")
        # TODO: For production, consider removing the time logging
        start_time = time.time()
        lemmatized_text = " ".join(self._preprocess_and_lemmatize(text))
        score = 0.0
        assert self.ahocorasick_model is not None
        results = self.ahocorasick_model.search(lemmatized_text)
        for _, weight in results:
            score += weight

        logging.debug(
            f"Scam keywords check took {round(time.time() - start_time, 8)} seconds."
        )
        return float(round(score, 3))

    def calculate_scam_score(self, text: str) -> float:
        """
        Calculate the scam score for the input text.

        :param text: input text to calculate scam score
        :type text: str
        :return: scam score
        :rtype: float
        """
        keyword_score = self.check_keywords(text)
        return min(keyword_score, 1)
