# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types.albums import (
    AssetsAssociationAddResponse,
    AssetsAssociationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssetsAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        assets_association = client.albums.assets_associations.list(
            "album_id",
        )
        assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.albums.assets_associations.with_raw_response.list(
            "album_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = response.parse()
        assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.albums.assets_associations.with_streaming_response.list(
            "album_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = response.parse()
            assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            client.albums.assets_associations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Gumnut) -> None:
        assets_association = client.albums.assets_associations.add(
            album_id="album_id",
            asset_ids=["string"],
        )
        assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Gumnut) -> None:
        response = client.albums.assets_associations.with_raw_response.add(
            album_id="album_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = response.parse()
        assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Gumnut) -> None:
        with client.albums.assets_associations.with_streaming_response.add(
            album_id="album_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = response.parse()
            assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            client.albums.assets_associations.with_raw_response.add(
                album_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Gumnut) -> None:
        assets_association = client.albums.assets_associations.remove(
            album_id="album_id",
            asset_ids=["string"],
        )
        assert assets_association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Gumnut) -> None:
        response = client.albums.assets_associations.with_raw_response.remove(
            album_id="album_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = response.parse()
        assert assets_association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Gumnut) -> None:
        with client.albums.assets_associations.with_streaming_response.remove(
            album_id="album_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = response.parse()
            assert assets_association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            client.albums.assets_associations.with_raw_response.remove(
                album_id="",
                asset_ids=["string"],
            )


class TestAsyncAssetsAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        assets_association = await async_client.albums.assets_associations.list(
            "album_id",
        )
        assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.albums.assets_associations.with_raw_response.list(
            "album_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = await response.parse()
        assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.albums.assets_associations.with_streaming_response.list(
            "album_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = await response.parse()
            assert_matches_type(AssetsAssociationListResponse, assets_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            await async_client.albums.assets_associations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncGumnut) -> None:
        assets_association = await async_client.albums.assets_associations.add(
            album_id="album_id",
            asset_ids=["string"],
        )
        assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncGumnut) -> None:
        response = await async_client.albums.assets_associations.with_raw_response.add(
            album_id="album_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = await response.parse()
        assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncGumnut) -> None:
        async with async_client.albums.assets_associations.with_streaming_response.add(
            album_id="album_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = await response.parse()
            assert_matches_type(AssetsAssociationAddResponse, assets_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            await async_client.albums.assets_associations.with_raw_response.add(
                album_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGumnut) -> None:
        assets_association = await async_client.albums.assets_associations.remove(
            album_id="album_id",
            asset_ids=["string"],
        )
        assert assets_association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGumnut) -> None:
        response = await async_client.albums.assets_associations.with_raw_response.remove(
            album_id="album_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assets_association = await response.parse()
        assert assets_association is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGumnut) -> None:
        async with async_client.albums.assets_associations.with_streaming_response.remove(
            album_id="album_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assets_association = await response.parse()
            assert assets_association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `album_id` but received ''"):
            await async_client.albums.assets_associations.with_raw_response.remove(
                album_id="",
                asset_ids=["string"],
            )
