"""Exercise the installed SDK's API surface from scripts/check-package, without API requests.

Custom code: kept separate from the generated check-installed-package.py so
regeneration never conflicts with it.
"""

import socket
import asyncio
from unittest.mock import patch

from gumnut import Gumnut, AsyncGumnut
from gumnut.types import AssetResponse, AssetListParams
from gumnut.resources.assets import AssetsResource, AsyncAssetsResource


def reject_network(*_args: object, **_kwargs: object) -> None:
    raise AssertionError("Package checks must not open network connections")


patch.object(socket.socket, "connect", reject_network).start()
patch.object(socket, "create_connection", reject_network).start()

assert AssetResponse.__module__.startswith("gumnut.types.")
assert AssetListParams.__module__.startswith("gumnut.types.")

with Gumnut(api_key="package-check", base_url="https://package-check.invalid") as client:
    assert isinstance(client.assets, AssetsResource)
assert client.is_closed(), "Synchronous client did not close"


async def check_async() -> None:
    async with AsyncGumnut(api_key="package-check", base_url="https://package-check.invalid") as client:
        assert isinstance(client.assets, AsyncAssetsResource)
    assert client.is_closed(), "Asynchronous client did not close"


asyncio.run(check_async())
print("Installed gumnut-sdk API surface passed")
