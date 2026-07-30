"""Run the Speak2Act pipeline (minimal placeholder).

This module should be extended to load ASR, NLP, and executor
components and wire them together. For now it provides a safe
smoke-run function used by tests.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run():
    """Simple placeholder run function for smoke tests.

    Returns:
        dict: a small example pipeline result.
    """
    logger.info("Starting Speak2Act pipeline (placeholder)...")
    # Placeholder result structure
    result = {
        "audio": None,
        "transcript": "",
        "intent": None,
        "entities": {},
    }
    logger.info("Pipeline finished (placeholder).")
    return result
