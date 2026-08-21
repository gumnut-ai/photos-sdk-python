# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import AssetResponse
from gumnut.types.assets import (
    VersionListResponse,
    AssetVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        version = client.assets.versions.list(
            asset_id="asset_id",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        version = client.assets.versions.list(
            asset_id="asset_id",
            include=["string", "string"],
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.assets.versions.with_raw_response.list(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.assets.versions.with_streaming_response.list(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.versions.with_raw_response.list(
                asset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gumnut) -> None:
        version = client.assets.versions.delete(
            version_id="version_id",
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gumnut) -> None:
        response = client.assets.versions.with_raw_response.delete(
            version_id="version_id",
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gumnut) -> None:
        with client.assets.versions.with_streaming_response.delete(
            version_id="version_id",
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(AssetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.versions.with_raw_response.delete(
                version_id="version_id",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.assets.versions.with_raw_response.delete(
                version_id="",
                asset_id="asset_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append(self, client: Gumnut) -> None:
        version = client.assets.versions.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_append_with_all_params(self, client: Gumnut) -> None:
        version = client.assets.versions.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
            include=["string", "string"],
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_append(self, client: Gumnut) -> None:
        response = client.assets.versions.with_raw_response.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_append(self, client: Gumnut) -> None:
        with client.assets.versions.with_streaming_response.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(AssetVersionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_append(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.versions.with_raw_response.append(
                asset_id="",
                file=b"Example data",
                kind="kind",
                params="params",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Gumnut) -> None:
        version = client.assets.versions.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Gumnut) -> None:
        version = client.assets.versions.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
            include=["string", "string"],
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Gumnut) -> None:
        response = client.assets.versions.with_raw_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Gumnut) -> None:
        with client.assets.versions.with_streaming_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(AssetVersionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.versions.with_raw_response.replace(
                version_id="version_id",
                asset_id="",
                file=b"Example data",
                kind="kind",
                params="params",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.assets.versions.with_raw_response.replace(
                version_id="",
                asset_id="asset_id",
                file=b"Example data",
                kind="kind",
                params="params",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revert(self, client: Gumnut) -> None:
        version = client.assets.versions.revert(
            version_id="version_id",
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revert(self, client: Gumnut) -> None:
        response = client.assets.versions.with_raw_response.revert(
            version_id="version_id",
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revert(self, client: Gumnut) -> None:
        with client.assets.versions.with_streaming_response.revert(
            version_id="version_id",
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(AssetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revert(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.versions.with_raw_response.revert(
                version_id="version_id",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.assets.versions.with_raw_response.revert(
                version_id="",
                asset_id="asset_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.list(
            asset_id="asset_id",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.list(
            asset_id="asset_id",
            include=["string", "string"],
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.versions.with_raw_response.list(
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.versions.with_streaming_response.list(
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.versions.with_raw_response.list(
                asset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.delete(
            version_id="version_id",
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.versions.with_raw_response.delete(
            version_id="version_id",
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.versions.with_streaming_response.delete(
            version_id="version_id",
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AssetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.versions.with_raw_response.delete(
                version_id="version_id",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.assets.versions.with_raw_response.delete(
                version_id="",
                asset_id="asset_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_append_with_all_params(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
            include=["string", "string"],
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_append(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.versions.with_raw_response.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_append(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.versions.with_streaming_response.append(
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AssetVersionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_append(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.versions.with_raw_response.append(
                asset_id="",
                file=b"Example data",
                kind="kind",
                params="params",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
            include=["string", "string"],
        )
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.versions.with_raw_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AssetVersionResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.versions.with_streaming_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=b"Example data",
            kind="kind",
            params="params",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AssetVersionResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.versions.with_raw_response.replace(
                version_id="version_id",
                asset_id="",
                file=b"Example data",
                kind="kind",
                params="params",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.assets.versions.with_raw_response.replace(
                version_id="",
                asset_id="asset_id",
                file=b"Example data",
                kind="kind",
                params="params",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revert(self, async_client: AsyncGumnut) -> None:
        version = await async_client.assets.versions.revert(
            version_id="version_id",
            asset_id="asset_id",
        )
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revert(self, async_client: AsyncGumnut) -> None:
        response = await async_client.assets.versions.with_raw_response.revert(
            version_id="version_id",
            asset_id="asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AssetResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revert(self, async_client: AsyncGumnut) -> None:
        async with async_client.assets.versions.with_streaming_response.revert(
            version_id="version_id",
            asset_id="asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AssetResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revert(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.versions.with_raw_response.revert(
                version_id="version_id",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.assets.versions.with_raw_response.revert(
                version_id="",
                asset_id="asset_id",
            )
