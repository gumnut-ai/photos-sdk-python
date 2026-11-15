# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import (
    BodyResponse,
    BodyDeleteResponse,
)
from gumnut.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBodies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gumnut) -> None:
        body = client.bodies.retrieve(
            body_id="body_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gumnut) -> None:
        body = client.bodies.retrieve(
            body_id="body_id",
            include=["string", "string"],
            library_id="library_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gumnut) -> None:

        response = client.bodies.with_raw_response.retrieve(
            body_id="body_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = response.parse()
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gumnut) -> None:
        with client.bodies.with_streaming_response.retrieve(
            body_id="body_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = response.parse()
            assert_matches_type(BodyResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            client.bodies.with_raw_response.retrieve(
                body_id="",
            )

    @parametrize
    def test_method_update(self, client: Gumnut) -> None:
        body = client.bodies.update(
            body_id="body_id",
            person_id="person_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gumnut) -> None:
        body = client.bodies.update(
            body_id="body_id",
            person_id="person_id",
            library_id="library_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gumnut) -> None:

        response = client.bodies.with_raw_response.update(
            body_id="body_id",
            person_id="person_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = response.parse()
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gumnut) -> None:
        with client.bodies.with_streaming_response.update(
            body_id="body_id",
            person_id="person_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = response.parse()
            assert_matches_type(BodyResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            client.bodies.with_raw_response.update(
                body_id="",
                person_id="person_id",
            )

    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        body = client.bodies.list()
        assert_matches_type(SyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        body = client.bodies.list(
            asset_id="asset_id",
            ids=["string", "string"],
            include=["string", "string"],
            library_id="library_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(SyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:

        response = client.bodies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = response.parse()
        assert_matches_type(SyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.bodies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = response.parse()
            assert_matches_type(SyncCursorPage[BodyResponse], body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gumnut) -> None:
        body = client.bodies.delete(
            body_id="body_id",
        )
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gumnut) -> None:
        body = client.bodies.delete(
            body_id="body_id",
            library_id="library_id",
        )
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gumnut) -> None:

        response = client.bodies.with_raw_response.delete(
            body_id="body_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = response.parse()
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gumnut) -> None:
        with client.bodies.with_streaming_response.delete(
            body_id="body_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = response.parse()
            assert_matches_type(BodyDeleteResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            client.bodies.with_raw_response.delete(
                body_id="",
            )


class TestAsyncBodies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.retrieve(
            body_id="body_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.retrieve(
            body_id="body_id",
            include=["string", "string"],
            library_id="library_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGumnut) -> None:

        response = await async_client.bodies.with_raw_response.retrieve(
            body_id="body_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = await response.parse()
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGumnut) -> None:
        async with async_client.bodies.with_streaming_response.retrieve(
            body_id="body_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = await response.parse()
            assert_matches_type(BodyResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            await async_client.bodies.with_raw_response.retrieve(
                body_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.update(
            body_id="body_id",
            person_id="person_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.update(
            body_id="body_id",
            person_id="person_id",
            library_id="library_id",
        )
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGumnut) -> None:

        response = await async_client.bodies.with_raw_response.update(
            body_id="body_id",
            person_id="person_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = await response.parse()
        assert_matches_type(BodyResponse, body, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGumnut) -> None:
        async with async_client.bodies.with_streaming_response.update(
            body_id="body_id",
            person_id="person_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = await response.parse()
            assert_matches_type(BodyResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            await async_client.bodies.with_raw_response.update(
                body_id="",
                person_id="person_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.list()
        assert_matches_type(AsyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.list(
            asset_id="asset_id",
            ids=["string", "string"],
            include=["string", "string"],
            library_id="library_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(AsyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:

        response = await async_client.bodies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = await response.parse()
        assert_matches_type(AsyncCursorPage[BodyResponse], body, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.bodies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = await response.parse()
            assert_matches_type(AsyncCursorPage[BodyResponse], body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.delete(
            body_id="body_id",
        )
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGumnut) -> None:
        body = await async_client.bodies.delete(
            body_id="body_id",
            library_id="library_id",
        )
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGumnut) -> None:

        response = await async_client.bodies.with_raw_response.delete(
            body_id="body_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        body = await response.parse()
        assert_matches_type(BodyDeleteResponse, body, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGumnut) -> None:
        async with async_client.bodies.with_streaming_response.delete(
            body_id="body_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            body = await response.parse()
            assert_matches_type(BodyDeleteResponse, body, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `body_id` but received ''"):
            await async_client.bodies.with_raw_response.delete(
                body_id="",
            )
