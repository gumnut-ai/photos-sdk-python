from __future__ import annotations

import os
from typing import Any

import httpx
import pytest
from respx import MockRouter

from gumnut import Gumnut
from gumnut._exceptions import (
    NotFoundError,
    APIStatusError,
    BadRequestError,
    PermissionDeniedError,
    UnprocessableEntityError,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

validation_errors = [
    {"loc": ["body", "name"], "msg": "Field required", "type": "missing"},
    {"loc": ["query", "limit"], "msg": "Input should be less than or equal to 200", "type": "less_than_equal"},
    {"loc": ["body", "ids", 3], "msg": "Input should be a valid string", "type": "string_type"},
]


def raise_status_error(client: Gumnut, respx_mock: MockRouter, response: httpx.Response) -> APIStatusError:
    respx_mock.get("/error").mock(return_value=response)
    with pytest.raises(APIStatusError) as exc_info:
        client.get("/error", cast_to=httpx.Response)
    return exc_info.value


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize(
    "status_code,body,error_class,expected",
    [
        (404, {"detail": "Asset not found"}, NotFoundError, "404 Asset not found"),
        (422, {"detail": "Album name is taken"}, UnprocessableEntityError, "422 Album name is taken"),
        (403, {"detail": "No access", "code": "not_shared"}, PermissionDeniedError, "403 No access"),
        (
            422,
            {"detail": validation_errors},
            UnprocessableEntityError,
            "422 body.name: Field required; query.limit: Input should be less than or equal to 200; "
            "body.ids.3: Input should be a valid string",
        ),
        (422, {"detail": [{"msg": "Value error"}]}, UnprocessableEntityError, "422 Value error"),
    ],
)
def test_message_uses_detail(
    client: Gumnut,
    respx_mock: MockRouter,
    status_code: int,
    body: dict[str, Any],
    error_class: type[APIStatusError],
    expected: str,
) -> None:
    error = raise_status_error(client, respx_mock, httpx.Response(status_code, json=body))

    assert type(error) is error_class
    assert str(error) == expected
    assert error.message == expected
    assert error.status_code == status_code
    assert error.body == body


@pytest.mark.respx(base_url=base_url)
@pytest.mark.parametrize(
    "body",
    [
        {"error": "bad request"},
        {"detail": ""},
        {"detail": []},
        {"detail": [{"loc": ["body"]}]},
        {"detail": {"reason": "nested"}},
        ["not", "an", "object"],
        "not an object",
    ],
)
def test_message_without_usable_detail_keeps_body(client: Gumnut, respx_mock: MockRouter, body: object) -> None:
    error = raise_status_error(client, respx_mock, httpx.Response(400, json=body))

    assert type(error) is BadRequestError
    assert error.message == f"Error code: 400 - {body}"
    assert error.body == body


@pytest.mark.respx(base_url=base_url)
def test_message_for_non_json_body_keeps_text(client: Gumnut, respx_mock: MockRouter) -> None:
    error = raise_status_error(client, respx_mock, httpx.Response(400, text="Bad Request"))

    assert error.message == "Bad Request"
    assert error.body == "Bad Request"
