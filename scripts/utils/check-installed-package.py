"""Verify installed metadata and typing assets without API requests."""

import sys
import socket
from pathlib import Path
from importlib import metadata, resources
from unittest.mock import patch

import gumnut as sdk


def reject_network(*_args: object, **_kwargs: object) -> None:
    raise AssertionError("Package checks must not open network connections")


patch.object(socket.socket, "connect", reject_network).start()
patch.object(socket, "create_connection", reject_network).start()

package_file = Path(sdk.__file__).resolve()
environment = Path(sys.prefix).resolve()
assert environment in package_file.parents, f"Imported SDK outside installed environment: {package_file}"
distribution = metadata.distribution("gumnut-sdk")
assert distribution.metadata["Name"] == "gumnut-sdk"
assert distribution.version == sdk.__version__ == "0.178.0", "Installed and generated versions differ"
module_path = "gumnut".replace(".", "/")
assert package_file == Path(distribution.locate_file(f"{module_path}/__init__.py")).resolve()
assert resources.files("gumnut").joinpath("py.typed").is_file(), "Installed SDK lacks py.typed"
print(f"Installed gumnut-sdk {distribution.version} passed: {package_file}")
