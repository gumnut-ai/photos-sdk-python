# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.libraries import member_list_params, member_update_params
from ...types.libraries.membership_response import MembershipResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    """First-party session only.

    Manage membership in a library owned by the signed-in account, or leave a joined library. API keys and delegated OAuth credentials cannot call these methods.
    """

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def update(
        self,
        user_id: str,
        *,
        library_id: str,
        role: Literal["viewer", "collaborator"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """Change an active non-owner member's role.

        Repeating the same role is unchanged.
        An inactive membership or attempt to change the owner returns 409; retrying
        unchanged will not clear it.

        Args:
          library_id: Library identifier.

          user_id: Member account identifier.

          role: New role for an active member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            path_template("/api/libraries/{library_id}/members/{user_id}", library_id=library_id, user_id=user_id),
            body=maybe_transform({"role": role}, member_update_params.MemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )

    def list(
        self,
        library_id: str,
        *,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["active", "left", "removed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MembershipResponse]:
        """
        List non-owner membership records for a library owned by the caller, newest
        first. Inactive records remain available through the state filter.

        Args:
          library_id: Library identifier.

          limit: Maximum records per page.

          starting_after_id: Continue after this membership ID from the previous page.

          state: Return only memberships in this state, or all states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return self._get_api_list(
            path_template("/api/libraries/{library_id}/members", library_id=library_id),
            page=SyncCursorPage[MembershipResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                        "state": state,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MembershipResponse,
        )

    def leave(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """
        End the caller's own non-owner membership, even when library content is
        unavailable. Repeating departure returns the existing inactive state without
        changing an owner-removal cutoff. An owner cannot leave; retrying unchanged
        returns 409.

        Args:
          library_id: Library identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return self._post(
            path_template("/api/libraries/{library_id}/leave", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )

    def remove(
        self,
        user_id: str,
        *,
        library_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """End a non-owner membership while retaining its owner-removal cutoff.

        Repeating
        removal returns the same record without advancing the cutoff. The owner cannot
        be removed; retrying that request unchanged returns 409.

        Args:
          library_id: Library identifier.

          user_id: Member account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            path_template("/api/libraries/{library_id}/members/{user_id}", library_id=library_id, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )


class AsyncMembersResource(AsyncAPIResource):
    """First-party session only.

    Manage membership in a library owned by the signed-in account, or leave a joined library. API keys and delegated OAuth credentials cannot call these methods.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def update(
        self,
        user_id: str,
        *,
        library_id: str,
        role: Literal["viewer", "collaborator"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """Change an active non-owner member's role.

        Repeating the same role is unchanged.
        An inactive membership or attempt to change the owner returns 409; retrying
        unchanged will not clear it.

        Args:
          library_id: Library identifier.

          user_id: Member account identifier.

          role: New role for an active member.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            path_template("/api/libraries/{library_id}/members/{user_id}", library_id=library_id, user_id=user_id),
            body=await async_maybe_transform({"role": role}, member_update_params.MemberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )

    def list(
        self,
        library_id: str,
        *,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["active", "left", "removed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MembershipResponse, AsyncCursorPage[MembershipResponse]]:
        """
        List non-owner membership records for a library owned by the caller, newest
        first. Inactive records remain available through the state filter.

        Args:
          library_id: Library identifier.

          limit: Maximum records per page.

          starting_after_id: Continue after this membership ID from the previous page.

          state: Return only memberships in this state, or all states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return self._get_api_list(
            path_template("/api/libraries/{library_id}/members", library_id=library_id),
            page=AsyncCursorPage[MembershipResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                        "state": state,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            model=MembershipResponse,
        )

    async def leave(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """
        End the caller's own non-owner membership, even when library content is
        unavailable. Repeating departure returns the existing inactive state without
        changing an owner-removal cutoff. An owner cannot leave; retrying unchanged
        returns 409.

        Args:
          library_id: Library identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return await self._post(
            path_template("/api/libraries/{library_id}/leave", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )

    async def remove(
        self,
        user_id: str,
        *,
        library_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipResponse:
        """End a non-owner membership while retaining its owner-removal cutoff.

        Repeating
        removal returns the same record without advancing the cutoff. The owner cannot
        be removed; retrying that request unchanged returns 409.

        Args:
          library_id: Library identifier.

          user_id: Member account identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            path_template("/api/libraries/{library_id}/members/{user_id}", library_id=library_id, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipResponse,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.update = to_raw_response_wrapper(
            members.update,
        )
        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.leave = to_raw_response_wrapper(
            members.leave,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.update = async_to_raw_response_wrapper(
            members.update,
        )
        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.leave = async_to_raw_response_wrapper(
            members.leave,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.update = to_streamed_response_wrapper(
            members.update,
        )
        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.leave = to_streamed_response_wrapper(
            members.leave,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.update = async_to_streamed_response_wrapper(
            members.update,
        )
        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.leave = async_to_streamed_response_wrapper(
            members.leave,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )
