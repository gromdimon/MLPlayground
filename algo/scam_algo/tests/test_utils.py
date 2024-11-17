from pathlib import Path

import ahocorasick  # type: ignore
import pytest

from scam_algorithm.src.utils import (
    AhoCorasickAutomaton,  # Adjust the import path as necessary
)

# Define mock keywords for testing
MOCK_KEYWORDS = {"example": 0.5, "test": 0.4}
MOCK_TEXT = "This is a test string with example and test"
MOCK_AUTOMATON_PATH = "tests/assets/test_automaton.pickle"


@pytest.fixture
def automaton_instance():
    """Fixture to create an AhoCorasickAutomaton instance with mock keywords."""
    instance = AhoCorasickAutomaton()
    instance.construct_automaton(MOCK_KEYWORDS)
    return instance


def test_automaton_construction(automaton_instance):
    """Test if the automaton is correctly constructed with the mock keywords."""
    assert automaton_instance.automaton is not None
    assert isinstance(automaton_instance.automaton, ahocorasick.Automaton)


def test_automaton_search(automaton_instance):
    """Test searching with the automaton returns correct matches and weights."""
    results = automaton_instance.search(MOCK_TEXT)
    assert len(results) > 0
    for keyword, weight in results:
        assert keyword in MOCK_KEYWORDS
        assert weight == MOCK_KEYWORDS[keyword]


def test_save_and_load_automaton(tmp_path):
    """Test saving and loading the automaton using pickle."""
    # Construct and save the automaton to a temporary path
    instance = AhoCorasickAutomaton()
    instance.construct_automaton(MOCK_KEYWORDS)
    temp_automaton_path = tmp_path / "temp_automaton.pickle"
    instance.save_to_file(str(temp_automaton_path))

    # Ensure the file exists
    assert temp_automaton_path.exists()

    # Load the automaton and test search functionality
    loaded_instance = AhoCorasickAutomaton.load_from_file(str(temp_automaton_path))
    results = loaded_instance.search(MOCK_TEXT)
    assert len(results) > 0
    for keyword, weight in results:
        assert keyword in MOCK_KEYWORDS
        assert weight == MOCK_KEYWORDS[keyword]
