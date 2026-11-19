# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import io
import os
from typing import Any, Dict
from pathlib import Path
from unittest import mock

import httpx
import pytest
from respx import MockRouter

from gumnut import Gumnut, AsyncGumnut, APIStatusError
from gumnut._utils import parse_datetime
from gumnut._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def _low_retry_timeout(*_args: Any, **_kwargs: Any) -> float:
    return 0.1


def _sent_timeout(route: Any) -> Dict[str, Any]:
    return route.calls.last.request.extensions["timeout"]


def _sparse_file(path: Path, size: int) -> Path:
    with path.open("wb") as file:
        file.truncate(size)
    return path


class _UnsizedStream(io.RawIOBase):
    """A stream whose size can't be read without consuming it."""

    def __init__(self) -> None:
        self._data = b"Example data"

    def readable(self) -> bool:
        return True

    def readinto(self, buffer: Any) -> int:
        size = min(len(buffer), len(self._data))
        buffer[:size] = self._data[:size]
        self._data = self._data[size:]
        return size


class TestAssetsCreateRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_max_retries(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            client.assets.with_raw_response.create(
                asset_data=b"Example data",
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            client.with_options(max_retries=1).assets.with_raw_response.create(
                asset_data=b"Example data",
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    def test_timeout(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(200, json={}))

        client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            timeout=5,
        )
        assert _sent_timeout(route)["read"] == 5

        client.with_options(timeout=30).assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    def test_timeout_scales_with_file_size(self, client: Gumnut, respx_mock: MockRouter, tmp_path: Path) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(200, json={}))

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            client.assets.with_raw_response.create(
                asset_data=file,
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        client.assets.with_raw_response.create(
            asset_data=io.BufferedReader(_UnsizedStream()),
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 600


class TestAssetsVersionsAppendRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_max_retries(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            client.assets.versions.with_raw_response.append(
                asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            client.with_options(max_retries=1).assets.versions.with_raw_response.append(
                asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    def test_timeout(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(200, json={}))

        client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params", timeout=5
        )
        assert _sent_timeout(route)["read"] == 5

        client.with_options(timeout=30).assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    def test_timeout_scales_with_file_size(self, client: Gumnut, respx_mock: MockRouter, tmp_path: Path) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(200, json={}))

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            client.assets.versions.with_raw_response.append(
                asset_id="asset_id", file=file, kind="kind", params="params"
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=io.BufferedReader(_UnsizedStream()), kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600


class TestAssetsVersionsReplaceRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_max_retries(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(500)
        )

        with pytest.raises(APIStatusError):
            client.assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            client.with_options(max_retries=1).assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    def test_timeout(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(200, json={})
        )

        client.assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        client.assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params", timeout=5
        )
        assert _sent_timeout(route)["read"] == 5

        client.with_options(timeout=30).assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    def test_timeout_scales_with_file_size(self, client: Gumnut, respx_mock: MockRouter, tmp_path: Path) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(200, json={})
        )

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            client.assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=file, kind="kind", params="params"
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        client.assets.versions.with_raw_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=io.BufferedReader(_UnsizedStream()),
            kind="kind",
            params="params",
        )
        assert _sent_timeout(route)["read"] == 600


class TestOtherMethodsRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_sdk_defaults(self, client: Gumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/users/me").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            client.users.with_raw_response.me()
        assert route.call_count == DEFAULT_MAX_RETRIES + 1
        assert _sent_timeout(route) == DEFAULT_TIMEOUT.as_dict()


class TestAsyncAssetsCreateRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_max_retries(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            await async_client.assets.with_raw_response.create(
                asset_data=b"Example data",
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            await async_client.with_options(max_retries=1).assets.with_raw_response.create(
                asset_data=b"Example data",
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(200, json={}))

        await async_client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        await async_client.assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            timeout=5,
        )
        assert _sent_timeout(route)["read"] == 5

        await async_client.with_options(timeout=30).assets.with_raw_response.create(
            asset_data=b"Example data",
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout_scales_with_file_size(
        self, async_client: AsyncGumnut, respx_mock: MockRouter, tmp_path: Path
    ) -> None:
        route = respx_mock.post("/api/assets").mock(return_value=httpx.Response(200, json={}))

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            await async_client.assets.with_raw_response.create(
                asset_data=file,
                device_asset_id="IMG_0421",
                device_id="teds-iphone",
                file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
                file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        await async_client.assets.with_raw_response.create(
            asset_data=io.BufferedReader(_UnsizedStream()),
            device_asset_id="IMG_0421",
            device_id="teds-iphone",
            file_created_at=parse_datetime("2026-05-04T10:30:00+10:00"),
            file_modified_at=parse_datetime("2026-05-04T10:30:00+10:00"),
        )
        assert _sent_timeout(route)["read"] == 600


class TestAsyncAssetsVersionsAppendRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_max_retries(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            await async_client.assets.versions.with_raw_response.append(
                asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            await async_client.with_options(max_retries=1).assets.versions.with_raw_response.append(
                asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(200, json={}))

        await async_client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        await async_client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params", timeout=5
        )
        assert _sent_timeout(route)["read"] == 5

        await async_client.with_options(timeout=30).assets.versions.with_raw_response.append(
            asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout_scales_with_file_size(
        self, async_client: AsyncGumnut, respx_mock: MockRouter, tmp_path: Path
    ) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions").mock(return_value=httpx.Response(200, json={}))

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            await async_client.assets.versions.with_raw_response.append(
                asset_id="asset_id", file=file, kind="kind", params="params"
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        await async_client.assets.versions.with_raw_response.append(
            asset_id="asset_id", file=io.BufferedReader(_UnsizedStream()), kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600


class TestAsyncAssetsVersionsReplaceRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_max_retries(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(500)
        )

        with pytest.raises(APIStatusError):
            await async_client.assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1

        with pytest.raises(APIStatusError):
            await async_client.with_options(max_retries=1).assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
            )
        assert route.call_count == 1 + 2

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(200, json={})
        )

        await async_client.assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 600
        assert _sent_timeout(route)["connect"] == DEFAULT_TIMEOUT.connect

        await async_client.assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params", timeout=5
        )
        assert _sent_timeout(route)["read"] == 5

        await async_client.with_options(timeout=30).assets.versions.with_raw_response.replace(
            version_id="version_id", asset_id="asset_id", file=b"Example data", kind="kind", params="params"
        )
        assert _sent_timeout(route)["read"] == 30

    @pytest.mark.respx(base_url=base_url)
    async def test_timeout_scales_with_file_size(
        self, async_client: AsyncGumnut, respx_mock: MockRouter, tmp_path: Path
    ) -> None:
        route = respx_mock.post("/api/assets/asset_id/versions/version_id/replace").mock(
            return_value=httpx.Response(200, json={})
        )

        with _sparse_file(tmp_path / "large", 82500000).open("rb") as file:
            await async_client.assets.versions.with_raw_response.replace(
                version_id="version_id", asset_id="asset_id", file=file, kind="kind", params="params"
            )
        assert _sent_timeout(route)["read"] == 82500000 / 125000

        # A stream of unknown size gets the minimum.
        await async_client.assets.versions.with_raw_response.replace(
            version_id="version_id",
            asset_id="asset_id",
            file=io.BufferedReader(_UnsizedStream()),
            kind="kind",
            params="params",
        )
        assert _sent_timeout(route)["read"] == 600


class TestAsyncOtherMethodsRequestDefaults:
    @mock.patch("gumnut._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_sdk_defaults(self, async_client: AsyncGumnut, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/users/me").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            await async_client.users.with_raw_response.me()
        assert route.call_count == DEFAULT_MAX_RETRIES + 1
        assert _sent_timeout(route) == DEFAULT_TIMEOUT.as_dict()
