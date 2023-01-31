"""REST client handling, including QualifiedStream base class."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator, JSONPathPaginator
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ShowpadPaginator(JSONPathPaginator):
    """Showpad API paginator class."""

    next_page_path = "$.meta.ending_cursor"
    has_more_path = "$.meta.has_more"

    def get_next(self, response: requests.Response) -> str | None:
        return next(extract_jsonpath(self.next_page_path, response.json()), None)

    def has_more(self, response: requests.Response) -> bool:
        return bool(next(extract_jsonpath(self.has_more_path, response.json()), False))


class QualifiedStream(RESTStream):
    """Qualified stream class."""

    url_base = "https://api.qualified.com/v1"
    records_jsonpath = "$.data[*]"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self, token=self.config.get("api_key")
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get(
                "user_agent", "Harness.io/Tap Qualified"
            )
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Return a token for identifying next page or None if no more pages."""
        return ShowpadPaginator(...)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["starting_after"] = next_page_token
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
