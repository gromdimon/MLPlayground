import pytest

from scam_algorithm.src.scam_algo import ScamDetector

# Mock data for testing
MODEL_NAME = "en_core_web_sm"
MOCK_KEYWORDS_FILE_PATH = "tests/assets/scam_keywords.yml"
MOCK_GROUP_WEIGHT_FILE_PATH = "tests/assets/scam_keywords_weights.json"
MOCK_AUTOMATON_PATH = "tests/assets/ac_automaton.pickle"


@pytest.fixture
def scam_detector():
    """Fixture to initialize ScamDetector with mock data."""
    detector = ScamDetector(
        model_name=MODEL_NAME,
        keywords_file_path=MOCK_KEYWORDS_FILE_PATH,
        group_weight_file_path=MOCK_GROUP_WEIGHT_FILE_PATH,
        automaton_path=MOCK_AUTOMATON_PATH,
    )
    return detector


def test_load_keywords(scam_detector):
    """Test loading of keyword weights."""
    assert isinstance(scam_detector.group_weights, dict)
    assert len(scam_detector.group_weights) > 0
    assert isinstance(scam_detector.scam_keywords, dict)
    assert len(scam_detector.scam_keywords) > 0


def test_preprocess_and_lemmatize(scam_detector):
    """Test the preprocessing and lemmatization of input text."""
    lemmatized_text = scam_detector._preprocess_and_lemmatize("Testing scam detection.")
    assert isinstance(lemmatized_text, list)
    assert len(lemmatized_text) > 0  # Ensure text is processed


def test_check_keywords_no_scam(scam_detector):
    """Test checking of keywords within a text."""
    score = scam_detector.check_keywords("Testing scam detection.")
    print(score, type(score))
    assert isinstance(score, float)
    assert score == 0.0  # No keywords found in the text


def test_check_keywords_with_scam(scam_detector):
    """Test checking of keywords within a text."""
    score = scam_detector.check_keywords("pump and dump scam")
    assert isinstance(score, float)
    assert score == 0.6  # Keywords found in the text
