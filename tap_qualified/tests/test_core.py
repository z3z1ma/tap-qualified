"""Tests standard tap features using the built-in SDK tests library."""
import os

from singer_sdk.testing import get_tap_test_class

from tap_qualified.tap import TapQualified

BASE_CONFIG = {
    "api_key": os.getenv("TAP_QUALIFIED_API_KEY"),
}

# Run standard built-in tap tests from the SDK:
TestTapQualified = get_tap_test_class(tap_class=TapQualified, config=BASE_CONFIG)
