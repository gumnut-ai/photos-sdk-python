# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import (
    StackDeleteResponse,
    StackSetCoverResponse,
    StackListStacksResponse,
    StackCreateStackResponse,
    StackRemoveAssetsResponse,
    StackRetrieveStackResponse,
    StackAddAssetsToStackResponse,
)
from gumnut.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gumnut) -> None:
        stack = client.stacks.delete(
            "stack_id",
        )
        assert_matches_type(StackDeleteResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.delete(
            "stack_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackDeleteResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.delete(
            "stack_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackDeleteResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            client.stacks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assets_to_stack(self, client: Gumnut) -> None:
        stack = client.stacks.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        )
        assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_assets_to_stack(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_assets_to_stack(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_assets_to_stack(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            client.stacks.with_raw_response.add_assets_to_stack(
                stack_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stack(self, client: Gumnut) -> None:
        stack = client.stacks.create_stack(
            asset_ids=["string", "string"],
        )
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stack_with_all_params(self, client: Gumnut) -> None:
        stack = client.stacks.create_stack(
            asset_ids=["string", "string"],
            library_id="library_id",
            primary_asset_id="primary_asset_id",
        )
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_stack(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.create_stack(
            asset_ids=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_stack(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.create_stack(
            asset_ids=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackCreateStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_stacks(self, client: Gumnut) -> None:
        stack = client.stacks.list_stacks()
        assert_matches_type(SyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_stacks_with_all_params(self, client: Gumnut) -> None:
        stack = client.stacks.list_stacks(
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            origin="auto_burst",
            primary_asset_id="primary_asset_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(SyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_stacks(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.list_stacks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(SyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_stacks(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.list_stacks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(SyncCursorPage[StackListStacksResponse], stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_assets(self, client: Gumnut) -> None:
        stack = client.stacks.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        )
        assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_assets(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_assets(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_assets(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            client.stacks.with_raw_response.remove_assets(
                stack_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stack(self, client: Gumnut) -> None:
        stack = client.stacks.retrieve_stack(
            "stack_id",
        )
        assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stack(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.retrieve_stack(
            "stack_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stack(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.retrieve_stack(
            "stack_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_stack(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            client.stacks.with_raw_response.retrieve_stack(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_cover(self, client: Gumnut) -> None:
        stack = client.stacks.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        )
        assert_matches_type(StackSetCoverResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_cover(self, client: Gumnut) -> None:
        response = client.stacks.with_raw_response.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackSetCoverResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_cover(self, client: Gumnut) -> None:
        with client.stacks.with_streaming_response.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackSetCoverResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_cover(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            client.stacks.with_raw_response.set_cover(
                stack_id="",
                primary_asset_id="primary_asset_id",
            )


class TestAsyncStacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.delete(
            "stack_id",
        )
        assert_matches_type(StackDeleteResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.delete(
            "stack_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackDeleteResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.delete(
            "stack_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackDeleteResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            await async_client.stacks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assets_to_stack(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        )
        assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_assets_to_stack(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_assets_to_stack(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.add_assets_to_stack(
            stack_id="stack_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackAddAssetsToStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_assets_to_stack(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            await async_client.stacks.with_raw_response.add_assets_to_stack(
                stack_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stack(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.create_stack(
            asset_ids=["string", "string"],
        )
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stack_with_all_params(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.create_stack(
            asset_ids=["string", "string"],
            library_id="library_id",
            primary_asset_id="primary_asset_id",
        )
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_stack(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.create_stack(
            asset_ids=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackCreateStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_stack(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.create_stack(
            asset_ids=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackCreateStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_stacks(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.list_stacks()
        assert_matches_type(AsyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_stacks_with_all_params(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.list_stacks(
            ids=["string", "string"],
            library_id="library_id",
            limit=1,
            origin="auto_burst",
            primary_asset_id="primary_asset_id",
            starting_after_id="starting_after_id",
        )
        assert_matches_type(AsyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_stacks(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.list_stacks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(AsyncCursorPage[StackListStacksResponse], stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_stacks(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.list_stacks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(AsyncCursorPage[StackListStacksResponse], stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_assets(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        )
        assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_assets(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_assets(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.remove_assets(
            stack_id="stack_id",
            asset_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackRemoveAssetsResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_assets(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            await async_client.stacks.with_raw_response.remove_assets(
                stack_id="",
                asset_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stack(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.retrieve_stack(
            "stack_id",
        )
        assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stack(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.retrieve_stack(
            "stack_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stack(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.retrieve_stack(
            "stack_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackRetrieveStackResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stack(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            await async_client.stacks.with_raw_response.retrieve_stack(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_cover(self, async_client: AsyncGumnut) -> None:
        stack = await async_client.stacks.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        )
        assert_matches_type(StackSetCoverResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_cover(self, async_client: AsyncGumnut) -> None:
        response = await async_client.stacks.with_raw_response.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackSetCoverResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_cover(self, async_client: AsyncGumnut) -> None:
        async with async_client.stacks.with_streaming_response.set_cover(
            stack_id="stack_id",
            primary_asset_id="primary_asset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackSetCoverResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_cover(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stack_id` but received ''"):
            await async_client.stacks.with_raw_response.set_cover(
                stack_id="",
                primary_asset_id="primary_asset_id",
            )
