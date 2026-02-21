# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import AlbumAssetResponse
from gumnut.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlbumAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        album_asset = client.album_assets.list()
        assert_matches_type(SyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        album_asset = client.album_assets.list(
            album_id="album_id",
            asset_id="asset_id",
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
        )
        assert_matches_type(SyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.album_assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album_asset = response.parse()
        assert_matches_type(SyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.album_assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album_asset = response.parse()
            assert_matches_type(SyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Gumnut) -> None:
        album_asset = client.album_assets.get(
            "album_asset_id",
        )
        assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Gumnut) -> None:
        response = client.album_assets.with_raw_response.get(
            "album_asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album_asset = response.parse()
        assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Gumnut) -> None:
        with client.album_assets.with_streaming_response.get(
            "album_asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album_asset = response.parse()
            assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_asset_id` but received ''"):
            client.album_assets.with_raw_response.get(
                "",
            )


class TestAsyncAlbumAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        album_asset = await async_client.album_assets.list()
        assert_matches_type(AsyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        album_asset = await async_client.album_assets.list(
            album_id="album_id",
            asset_id="asset_id",
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
        )
        assert_matches_type(AsyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.album_assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album_asset = await response.parse()
        assert_matches_type(AsyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.album_assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album_asset = await response.parse()
            assert_matches_type(AsyncCursorPage[AlbumAssetResponse], album_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncGumnut) -> None:
        album_asset = await async_client.album_assets.get(
            "album_asset_id",
        )
        assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGumnut) -> None:
        response = await async_client.album_assets.with_raw_response.get(
            "album_asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        album_asset = await response.parse()
        assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGumnut) -> None:
        async with async_client.album_assets.with_streaming_response.get(
            "album_asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            album_asset = await response.parse()
            assert_matches_type(AlbumAssetResponse, album_asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_asset_id` but received ''"):
            await async_client.album_assets.with_raw_response.get(
                "",
            )
