from typing import Any, cast

import pytest

from gumnut import Gumnut, BadRequestError


def test_mock_rejects_invalid_request(client: Gumnut) -> None:
    # Deliberately bypass compile-time validation to test the HTTP validator.
    with pytest.raises(BadRequestError) as error:
        client.albums.create(name=cast(Any, 123))

    assert error.value.response.headers["x-steady-request-valid"] == "false"
