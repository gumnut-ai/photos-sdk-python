# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from photos import Photos, AsyncPhotos
from tests.utils import assert_matches_type
from photos.types import FaceResponse
from photos.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Photos) -> None:
        face = client.faces.retrieve(
            "face_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Photos) -> None:
        response = client.faces.with_raw_response.retrieve(
            "face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Photos) -> None:
        with client.faces.with_streaming_response.retrieve(
            "face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Photos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            client.faces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Photos) -> None:
        face = client.faces.update(
            face_id="face_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Photos) -> None:
        face = client.faces.update(
            face_id="face_id",
            person_id="person_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Photos) -> None:
        response = client.faces.with_raw_response.update(
            face_id="face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Photos) -> None:
        with client.faces.with_streaming_response.update(
            face_id="face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Photos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            client.faces.with_raw_response.update(
                face_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Photos) -> None:
        face = client.faces.list()
        assert_matches_type(SyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Photos) -> None:
        face = client.faces.list(
            asset_id="asset_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(SyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Photos) -> None:
        response = client.faces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert_matches_type(SyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Photos) -> None:
        with client.faces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert_matches_type(SyncCursorPage[FaceResponse], face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Photos) -> None:
        face = client.faces.delete(
            "face_id",
        )
        assert face is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Photos) -> None:
        response = client.faces.with_raw_response.delete(
            "face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = response.parse()
        assert face is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Photos) -> None:
        with client.faces.with_streaming_response.delete(
            "face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = response.parse()
            assert face is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Photos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            client.faces.with_raw_response.delete(
                "",
            )


class TestAsyncFaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.retrieve(
            "face_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPhotos) -> None:
        response = await async_client.faces.with_raw_response.retrieve(
            "face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPhotos) -> None:
        async with async_client.faces.with_streaming_response.retrieve(
            "face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPhotos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            await async_client.faces.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.update(
            face_id="face_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.update(
            face_id="face_id",
            person_id="person_id",
        )
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPhotos) -> None:
        response = await async_client.faces.with_raw_response.update(
            face_id="face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(FaceResponse, face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPhotos) -> None:
        async with async_client.faces.with_streaming_response.update(
            face_id="face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(FaceResponse, face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPhotos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            await async_client.faces.with_raw_response.update(
                face_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.list()
        assert_matches_type(AsyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.list(
            asset_id="asset_id",
            limit=1,
            person_id="person_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(AsyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPhotos) -> None:
        response = await async_client.faces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert_matches_type(AsyncCursorPage[FaceResponse], face, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPhotos) -> None:
        async with async_client.faces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert_matches_type(AsyncCursorPage[FaceResponse], face, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPhotos) -> None:
        face = await async_client.faces.delete(
            "face_id",
        )
        assert face is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPhotos) -> None:
        response = await async_client.faces.with_raw_response.delete(
            "face_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        face = await response.parse()
        assert face is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPhotos) -> None:
        async with async_client.faces.with_streaming_response.delete(
            "face_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            face = await response.parse()
            assert face is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPhotos) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `face_id` but received ''"):
            await async_client.faces.with_raw_response.delete(
                "",
            )
