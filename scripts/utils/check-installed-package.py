"""Exercise the installed SDK from scripts/check-package, without API requests."""

import sys
import socket
import asyncio
from pathlib import Path
from importlib import metadata, resources
from unittest.mock import patch

import gumnut
from gumnut import Gumnut, AsyncGumnut
from gumnut.types import AssetResponse, AssetListParams
from gumnut.resources.assets import AssetsResource, AsyncAssetsResource


def reject_network(*_args: object, **_kwargs: object) -> None:
    raise AssertionError("Package checks must not open network connections")


patch.object(socket.socket, "connect", reject_network).start()
patch.object(socket, "create_connection", reject_network).start()

package_file = Path(gumnut.__file__).resolve()
environment = Path(sys.prefix).resolve()
assert environment in package_file.parents, f"Imported SDK outside installed environment: {package_file}"
distribution = metadata.distribution("gumnut-sdk")
assert distribution.metadata["Name"] == "gumnut-sdk"
assert distribution.version == gumnut.__version__, "Installed metadata and runtime versions differ"
assert package_file == Path(distribution.locate_file("gumnut/__init__.py")).resolve()
assert resources.files("gumnut").joinpath("py.typed").is_file(), "Installed SDK lacks py.typed"
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
print(f"Installed gumnut-sdk {distribution.version} passed: {package_file}")
