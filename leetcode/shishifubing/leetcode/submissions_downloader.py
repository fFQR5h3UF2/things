import logging

import requests

from shishifubing.leetcode.types import Config, LeetcodeException, SubmissionsResponse

logger = logging.getLogger(__name__)


class SubmissionsDownloader:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.session = requests.Session()
        self.headers = {
            "content-type": "application/json",
            "origin": self.config.base_url,
            "referer": self.config.base_url,
            "user-agent": "Mozilla/5.0 LeetCode API",
            "cookie": f"LEETCODE_SESSION={self.config.session}",
        }

    def __del__(self) -> None:
        self.session.close()

    def _url(self, offset: int, limit: int) -> str:
        return f"{self.config.base_url}/api/submissions/?offset={offset}&limit={limit}&lastkey="

    def download(self, offset: int, limit: int) -> SubmissionsResponse:
        response = self.session.get(url=self._url(offset, limit), headers=self.headers)
        try:
            response.raise_for_status()
            return SubmissionsResponse(**response.json())
        except Exception as e:
            raise LeetcodeException(f"could not parse response: {response.text}") from e
