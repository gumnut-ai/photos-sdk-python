# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types.sync import ProjectionReadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjectionReads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_read_overload_1(self, client: Gumnut) -> None:
        projection_read = client.sync.projection_reads.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_raw_response_read_overload_1(self, client: Gumnut) -> None:

        response = client.sync.projection_reads.with_raw_response.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_streaming_response_read_overload_1(self, client: Gumnut) -> None:
        with client.sync.projection_reads.with_streaming_response.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read_overload_2(self, client: Gumnut) -> None:
        projection_read = client.sync.projection_reads.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_raw_response_read_overload_2(self, client: Gumnut) -> None:

        response = client.sync.projection_reads.with_raw_response.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_streaming_response_read_overload_2(self, client: Gumnut) -> None:
        with client.sync.projection_reads.with_streaming_response.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read_overload_3(self, client: Gumnut) -> None:
        projection_read = client.sync.projection_reads.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_raw_response_read_overload_3(self, client: Gumnut) -> None:

        response = client.sync.projection_reads.with_raw_response.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_streaming_response_read_overload_3(self, client: Gumnut) -> None:
        with client.sync.projection_reads.with_streaming_response.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read_overload_4(self, client: Gumnut) -> None:
        projection_read = client.sync.projection_reads.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_raw_response_read_overload_4(self, client: Gumnut) -> None:

        response = client.sync.projection_reads.with_raw_response.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    def test_streaming_response_read_overload_4(self, client: Gumnut) -> None:
        with client.sync.projection_reads.with_streaming_response.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjectionReads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_read_overload_1(self, async_client: AsyncGumnut) -> None:
        projection_read = await async_client.sync.projection_reads.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_raw_response_read_overload_1(self, async_client: AsyncGumnut) -> None:

        response = await async_client.sync.projection_reads.with_raw_response.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = await response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_streaming_response_read_overload_1(self, async_client: AsyncGumnut) -> None:
        async with async_client.sync.projection_reads.with_streaming_response.read(
            keys=[
                {
                    "id": "x",
                    "kind": "current_user",
                }
            ],
            library_id="x",
            mode="roots",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = await response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read_overload_2(self, async_client: AsyncGumnut) -> None:
        projection_read = await async_client.sync.projection_reads.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_raw_response_read_overload_2(self, async_client: AsyncGumnut) -> None:

        response = await async_client.sync.projection_reads.with_raw_response.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = await response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_streaming_response_read_overload_2(self, async_client: AsyncGumnut) -> None:
        async with async_client.sync.projection_reads.with_streaming_response.read(
            library_id="x",
            mode="baseline_begin",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = await response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read_overload_3(self, async_client: AsyncGumnut) -> None:
        projection_read = await async_client.sync.projection_reads.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_raw_response_read_overload_3(self, async_client: AsyncGumnut) -> None:

        response = await async_client.sync.projection_reads.with_raw_response.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = await response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_streaming_response_read_overload_3(self, async_client: AsyncGumnut) -> None:
        async with async_client.sync.projection_reads.with_streaming_response.read(
            enumeration_token="x",
            library_id="x",
            mode="baseline_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = await response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read_overload_4(self, async_client: AsyncGumnut) -> None:
        projection_read = await async_client.sync.projection_reads.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        )
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_raw_response_read_overload_4(self, async_client: AsyncGumnut) -> None:

        response = await async_client.sync.projection_reads.with_raw_response.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        projection_read = await response.parse()
        assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

    @parametrize
    async def test_streaming_response_read_overload_4(self, async_client: AsyncGumnut) -> None:
        async with async_client.sync.projection_reads.with_streaming_response.read(
            enumeration_token="enumeration_token",
            library_id="x",
            mode="relation_page",
            profile={
                "name": "gumnut-library",
                "version": 1,
            },
            selector={
                "parent_id": "x",
                "relation": "asset_faces",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            projection_read = await response.parse()
            assert_matches_type(ProjectionReadResponse, projection_read, path=["response"])

        assert cast(Any, response.is_closed) is True
