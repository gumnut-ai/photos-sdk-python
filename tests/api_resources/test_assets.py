# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import (
    AssetResponse,
    AssetCountResponse,
    AssetExistenceResponse,
)
from gumnut._utils import parse_datetime
from gumnut.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Gumnut) -> None:
        asset = client.assets.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gumnut) -> None:
        asset = client.assets.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gumnut) -> None:
        asset = client.assets.retrieve(
            "asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.retrieve(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.retrieve(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        asset = client.assets.list()
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        asset = client.assets.list(
            album_id="album_id",
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            local_datetime_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            local_datetime_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            person_id="person_id",
            starting_after_id="starting_after_id",
            state="live",
        )
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncCursorPage[AssetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gumnut) -> None:
        asset = client.assets.delete(
            "asset_id",
        )
        assert asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.delete(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.delete(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_existence(self, client: Gumnut) -> None:
        asset = client.assets.check_existence()
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_existence_with_all_params(self, client: Gumnut) -> None:
        asset = client.assets.check_existence(
            library_id="library_id",
            checksum_sha1s=["string"],
            checksums=["string"],
            device_asset_ids=["string"],
            device_id="deviceId",
        )
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_existence(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.check_existence()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_existence(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.check_existence() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetExistenceResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_counts(self, client: Gumnut) -> None:
        asset = client.assets.counts()
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_counts_with_all_params(self, client: Gumnut) -> None:
        asset = client.assets.counts(
            album_id="album_id",
            group_by="group_by",
            library_id="library_id",
            limit=1,
            local_datetime_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            local_datetime_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            person_id="person_id",
            state="live",
        )
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_counts(self, client: Gumnut) -> None:
        response = client.assets.with_raw_response.counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_counts(self, client: Gumnut) -> None:
        with client.assets.with_streaming_response.counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCountResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.create(
            asset_data=b"Example data",
            device_asset_id="device_asset_id",
            device_id="device_id",
            file_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            file_modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.retrieve(
            "asset_id",
        )
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.retrieve(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.retrieve(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.list()
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.list(
            album_id="album_id",
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            local_datetime_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            local_datetime_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            person_id="person_id",
            starting_after_id="starting_after_id",
            state="live",
        )
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncCursorPage[AssetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.delete(
            "asset_id",
        )
        assert asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.delete(
            "asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.delete(
            "asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_existence(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.check_existence()
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_existence_with_all_params(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.check_existence(
            library_id="library_id",
            checksum_sha1s=["string"],
            checksums=["string"],
            device_asset_ids=["string"],
            device_id="deviceId",
        )
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_existence(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.check_existence()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetExistenceResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_existence(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.check_existence() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetExistenceResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_counts(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.counts()
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_counts_with_all_params(self, async_client: AsyncGumnut) -> None:
        asset = await async_client.assets.counts(
            album_id="album_id",
            group_by="group_by",
            library_id="library_id",
            limit=1,
            local_datetime_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            local_datetime_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            person_id="person_id",
            state="live",
        )
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_counts(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.with_raw_response.counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCountResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_counts(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.with_streaming_response.counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCountResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
