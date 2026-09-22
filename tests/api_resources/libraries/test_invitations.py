# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut._utils import parse_datetime
from gumnut.pagination import SyncCursorPage, AsyncCursorPage
from gumnut.types.libraries import (
    InvitationResponse,
    InvitationJoinResponse,
    InvitationLinkResponse,
    InvitationPreviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvitations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        )
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.list()
        assert_matches_type(SyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.list(
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
            state="active",
        )
        assert_matches_type(SyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(SyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(SyncCursorPage[InvitationResponse], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.disable(
            "invitation_id",
        )
        assert_matches_type(InvitationResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.disable(
            "invitation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.disable(
            "invitation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.libraries.invitations.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_join(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.join(
            invitation_id="invitation_id",
            secret="x",
        )
        assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_join(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.join(
            invitation_id="invitation_id",
            secret="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_join(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.join(
            invitation_id="invitation_id",
            secret="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_join(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.libraries.invitations.with_raw_response.join(
                invitation_id="",
                secret="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.link(
            "invitation_id",
        )
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.link(
            "invitation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.link(
            "invitation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_link(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.libraries.invitations.with_raw_response.link(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_preview(self, client: Gumnut) -> None:
        invitation = client.libraries.invitations.preview(
            invitation_id="invitation_id",
            secret="x",
        )
        assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_preview(self, client: Gumnut) -> None:
        response = client.libraries.invitations.with_raw_response.preview(
            invitation_id="invitation_id",
            secret="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = response.parse()
        assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_preview(self, client: Gumnut) -> None:
        with client.libraries.invitations.with_streaming_response.preview(
            invitation_id="invitation_id",
            secret="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = response.parse()
            assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_preview(self, client: Gumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            client.libraries.invitations.with_raw_response.preview(
                invitation_id="",
                secret="x",
            )


class TestAsyncInvitations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        )
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.create(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            library_id="library_id",
            max_joiners=1,
            role="viewer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.list()
        assert_matches_type(AsyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.list(
            library_id="library_id",
            limit=1,
            starting_after_id="starting_after_id",
            state="active",
        )
        assert_matches_type(AsyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(AsyncCursorPage[InvitationResponse], invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(AsyncCursorPage[InvitationResponse], invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.disable(
            "invitation_id",
        )
        assert_matches_type(InvitationResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.disable(
            "invitation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.disable(
            "invitation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.libraries.invitations.with_raw_response.disable(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_join(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.join(
            invitation_id="invitation_id",
            secret="x",
        )
        assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.join(
            invitation_id="invitation_id",
            secret="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.join(
            invitation_id="invitation_id",
            secret="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationJoinResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_join(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.libraries.invitations.with_raw_response.join(
                invitation_id="",
                secret="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.link(
            "invitation_id",
        )
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.link(
            "invitation_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.link(
            "invitation_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationLinkResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_link(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.libraries.invitations.with_raw_response.link(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_preview(self, async_client: AsyncGumnut) -> None:
        invitation = await async_client.libraries.invitations.preview(
            invitation_id="invitation_id",
            secret="x",
        )
        assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncGumnut) -> None:
        response = await async_client.libraries.invitations.with_raw_response.preview(
            invitation_id="invitation_id",
            secret="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invitation = await response.parse()
        assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncGumnut) -> None:
        async with async_client.libraries.invitations.with_streaming_response.preview(
            invitation_id="invitation_id",
            secret="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invitation = await response.parse()
            assert_matches_type(InvitationPreviewResponse, invitation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_preview(self, async_client: AsyncGumnut) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invitation_id` but received ''"):
            await async_client.libraries.invitations.with_raw_response.preview(
                invitation_id="",
                secret="x",
            )
