import logging

from src.scam_algo import (
    AUTOMATON_PATH,
    GROUP_WEIGHT_FILE_PATH,
    KEYWORDS_FILE_PATH,
    MODEL_NAME,
    ScamDetector,
)


def main():
    logging.debug("Initializing ScamDetector...")
    detector = ScamDetector(
        model_name=MODEL_NAME,
        keywords_file_path=KEYWORDS_FILE_PATH,
        group_weight_file_path=GROUP_WEIGHT_FILE_PATH,
        automaton_path=AUTOMATON_PATH,
    )

    # Check scam likelihood
    message = "Hey, I have some issues with the offer on your website. HUGE PayPal invoice in my BIO!!"
    score = detector.calculate_scam_score(message)
    print(f"Scam likelihood score: {score}")


if __name__ == "__main__":
    main()
