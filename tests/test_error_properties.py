# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import httpx
import pytest
from respx import MockRouter

from gumnut import Gumnut, APIStatusError, APIConnectionError

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

body = {"code": "code"}


def raise_status_error(client: Gumnut, respx_mock: MockRouter, response: httpx.Response) -> APIStatusError:
    respx_mock.get("/error").mock(return_value=response)
    with pytest.raises(APIStatusError) as exc_info:
        client.with_options(max_retries=0).get("/error", cast_to=httpx.Response)
    return exc_info.value


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize("status_code", [400, 401, 403, 404, 409, 422, 429, 500])
def test_reads_properties_from_body(client: Gumnut, respx_mock: MockRouter, status_code: int) -> None:
    error = raise_status_error(client, respx_mock, httpx.Response(status_code, json=body))

    assert error.status_code == status_code
    assert error.code == "code"


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(409, json={}),
        httpx.Response(409, json=["not", "an", "object"]),
        httpx.Response(409, text="Conflict"),
    ],
)
def test_properties_unset_when_body_lacks_them(
    client: Gumnut, respx_mock: MockRouter, response: httpx.Response
) -> None:
    error = raise_status_error(client, respx_mock, response)

    assert error.code is None


def test_properties_unset_without_response() -> None:
    error = APIConnectionError(request=httpx.Request("GET", base_url))

    assert error.code is None
