# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.pagination import SyncCursorPage, AsyncCursorPage
from gumnut.types.libraries import MembershipResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Gumnut) -> None:
        member = client.libraries.members.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gumnut) -> None:
        response = client.libraries.members.with_raw_response.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gumnut) -> None:
        with client.libraries.members.with_streaming_response.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            client.libraries.members.with_raw_response.update(
                user_id="user_id",
                library_id="",
                role="viewer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.libraries.members.with_raw_response.update(
                user_id="",
                library_id="library_id",
                role="viewer",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        member = client.libraries.members.list(
            library_id="library_id",
        )
        assert_matches_type(SyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        member = client.libraries.members.list(
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
            state="active",
        )
        assert_matches_type(SyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.libraries.members.with_raw_response.list(
            library_id="library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.libraries.members.with_streaming_response.list(
            library_id="library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncCursorPage[MembershipResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            client.libraries.members.with_raw_response.list(
                library_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_leave(self, client: Gumnut) -> None:
        member = client.libraries.members.leave(
            "library_id",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_leave(self, client: Gumnut) -> None:
        response = client.libraries.members.with_raw_response.leave(
            "library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_leave(self, client: Gumnut) -> None:
        with client.libraries.members.with_streaming_response.leave(
            "library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_leave(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            client.libraries.members.with_raw_response.leave(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Gumnut) -> None:
        member = client.libraries.members.remove(
            user_id="user_id",
            library_id="library_id",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Gumnut) -> None:
        response = client.libraries.members.with_raw_response.remove(
            user_id="user_id",
            library_id="library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Gumnut) -> None:
        with client.libraries.members.with_streaming_response.remove(
            user_id="user_id",
            library_id="library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            client.libraries.members.with_raw_response.remove(
                user_id="user_id",
                library_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.libraries.members.with_raw_response.remove(
                user_id="",
                library_id="library_id",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGumnut) -> None:
        member = await async_client.libraries.members.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.members.with_raw_response.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.members.with_streaming_response.update(
            user_id="user_id",
            library_id="library_id",
            role="viewer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            await async_client.libraries.members.with_raw_response.update(
                user_id="user_id",
                library_id="",
                role="viewer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.libraries.members.with_raw_response.update(
                user_id="",
                library_id="library_id",
                role="viewer",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        member = await async_client.libraries.members.list(
            library_id="library_id",
        )
        assert_matches_type(AsyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        member = await async_client.libraries.members.list(
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
            state="active",
        )
        assert_matches_type(AsyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.members.with_raw_response.list(
            library_id="library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncCursorPage[MembershipResponse], member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.members.with_streaming_response.list(
            library_id="library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncCursorPage[MembershipResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            await async_client.libraries.members.with_raw_response.list(
                library_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_leave(self, async_client: AsyncGumnut) -> None:
        member = await async_client.libraries.members.leave(
            "library_id",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.members.with_raw_response.leave(
            "library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.members.with_streaming_response.leave(
            "library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_leave(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            await async_client.libraries.members.with_raw_response.leave(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncGumnut) -> None:
        member = await async_client.libraries.members.remove(
            user_id="user_id",
            library_id="library_id",
        )
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.members.with_raw_response.remove(
            user_id="user_id",
            library_id="library_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(MembershipResponse, member, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.members.with_streaming_response.remove(
            user_id="user_id",
            library_id="library_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(MembershipResponse, member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `library_id` but received ''"):
            await async_client.libraries.members.with_raw_response.remove(
                user_id="user_id",
                library_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.libraries.members.with_raw_response.remove(
                user_id="",
                library_id="library_id",
            )
