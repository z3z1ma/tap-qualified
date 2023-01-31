"""Stream type classes for tap-qualified."""
from pathlib import Path

from tap_qualified.client import QualifiedStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class RepConversationStream(QualifiedStream):
    """A stream of conversations with reps."""

    name = "rep_conversations"
    path = "/rep_conversations"
    primary_keys = ["id"]
    schema_file = SCHEMAS_DIR / "rep_conversations.json"


class BotConversationStream(QualifiedStream):
    """A stream of conversations with bots."""

    name = "bot_conversations"
    path = "/bot_conversations"
    primary_keys = ["id"]
    schema_file = SCHEMAS_DIR / "bot_conversations.json"
