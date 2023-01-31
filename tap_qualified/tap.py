"""Qualified tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_qualified.streams import BotConversationStream, RepConversationStream


class TapQualified(Tap):
    """Qualified tap class."""

    name = "tap-qualified"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            description="The user agent to use when making requests to the API service",
            default="Harness.io/Tap Qualified",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            stream_class(tap=self)
            for stream_class in (BotConversationStream, RepConversationStream)
        ]


if __name__ == "__main__":
    TapQualified.cli()
