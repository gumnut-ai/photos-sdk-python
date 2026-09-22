# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
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
from ...types.libraries import (
    invitation_join_params,
    invitation_list_params,
    invitation_create_params,
    invitation_preview_params,
)
from ...types.libraries.invitation_response import InvitationResponse
from ...types.libraries.invitation_join_response import InvitationJoinResponse
from ...types.libraries.invitation_link_response import InvitationLinkResponse
from ...types.libraries.invitation_preview_response import InvitationPreviewResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    """First-party session only.

    Owners manage links; signed-in recipients preview and join with the secret in the POST body. API keys and delegated OAuth credentials cannot call these methods.
    """

    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        expires_at: Union[str, datetime],
        library_id: str,
        max_joiners: int,
        role: Literal["viewer", "collaborator"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationLinkResponse:
        """Issue an invitation for one library.

        An identical active policy returns the same
        link with 200; a new policy returns 201. A matching inactive invitation returns
        409 without a link; retry with a new policy. Admission disabled returns 503;
        retry after it becomes available.

        Args:
          expires_at: Absolute expiration instant with a timezone offset; must be in the future.

          library_id: ID of the single library this invitation targets.

          max_joiners: Maximum number of distinct accounts that can redeem this invitation.

          role: Role offered to admitted members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/libraries/invitations",
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "library_id": library_id,
                    "max_joiners": max_joiners,
                    "role": role,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationLinkResponse,
        )

    def list(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["active", "exhausted", "expired", "disabled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[InvitationResponse]:
        """
        List invitation metadata across libraries owned by the caller, newest first.
        Secrets are never included.

        Args:
          library_id: Optional owner-library filter; omit to list invitations across all libraries you
              own.

          limit: Maximum records per page.

          starting_after_id: Continue after this invitation ID from the previous page.

          state: Return only invitations in this state, or all states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/libraries/invitations",
            page=SyncCursorPage[InvitationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                        "state": state,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=InvitationResponse,
        )

    def disable(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationResponse:
        """
        Prevent future admissions through this invitation without removing existing
        members. Repeating disablement returns the same inactive record.

        Args:
          invitation_id: Invitation identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._post(
            path_template("/api/libraries/invitations/{invitation_id}/disable", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationResponse,
        )

    def join(
        self,
        invitation_id: str,
        *,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationJoinResponse:
        """Admit the caller atomically or return their unchanged existing access.

        Retrying
        an uncertain join unchanged consumes no additional place. Invalid secrets or
        unavailable libraries return a generic 404; retry with a valid, available link.
        Expired, disabled, exhausted, or removal-cutoff invitations return 409; request
        a new invitation. Admission disabled returns 503; retry after it becomes
        available.

        Args:
          invitation_id: Invitation identifier.

          secret: Opaque secret from the invitation URL fragment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._post(
            path_template("/api/libraries/invitations/{invitation_id}/join", invitation_id=invitation_id),
            body=maybe_transform({"secret": secret}, invitation_join_params.InvitationJoinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationJoinResponse,
        )

    def link(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationLinkResponse:
        """Return an active invitation's existing link without changing its policy or
        usage.

        Inactive invitations return 409 without a link; retrying unchanged cannot
        reactivate one.

        Args:
          invitation_id: Invitation identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._get(
            path_template("/api/libraries/invitations/{invitation_id}/link", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationLinkResponse,
        )

    def preview(
        self,
        invitation_id: str,
        *,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationPreviewResponse:
        """
        Return library attribution and the caller's current eligibility without
        admitting them or reserving a place. Invalid secrets and unavailable libraries
        return the same generic 404; retry with a valid, available invitation link.

        Args:
          invitation_id: Invitation identifier.

          secret: Opaque secret from the invitation URL fragment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return self._post(
            path_template("/api/libraries/invitations/{invitation_id}/preview", invitation_id=invitation_id),
            body=maybe_transform({"secret": secret}, invitation_preview_params.InvitationPreviewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationPreviewResponse,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    """First-party session only.

    Owners manage links; signed-in recipients preview and join with the secret in the POST body. API keys and delegated OAuth credentials cannot call these methods.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        expires_at: Union[str, datetime],
        library_id: str,
        max_joiners: int,
        role: Literal["viewer", "collaborator"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationLinkResponse:
        """Issue an invitation for one library.

        An identical active policy returns the same
        link with 200; a new policy returns 201. A matching inactive invitation returns
        409 without a link; retry with a new policy. Admission disabled returns 503;
        retry after it becomes available.

        Args:
          expires_at: Absolute expiration instant with a timezone offset; must be in the future.

          library_id: ID of the single library this invitation targets.

          max_joiners: Maximum number of distinct accounts that can redeem this invitation.

          role: Role offered to admitted members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/libraries/invitations",
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "library_id": library_id,
                    "max_joiners": max_joiners,
                    "role": role,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationLinkResponse,
        )

    def list(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["active", "exhausted", "expired", "disabled", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvitationResponse, AsyncCursorPage[InvitationResponse]]:
        """
        List invitation metadata across libraries owned by the caller, newest first.
        Secrets are never included.

        Args:
          library_id: Optional owner-library filter; omit to list invitations across all libraries you
              own.

          limit: Maximum records per page.

          starting_after_id: Continue after this invitation ID from the previous page.

          state: Return only invitations in this state, or all states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/libraries/invitations",
            page=AsyncCursorPage[InvitationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                        "state": state,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            model=InvitationResponse,
        )

    async def disable(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationResponse:
        """
        Prevent future admissions through this invitation without removing existing
        members. Repeating disablement returns the same inactive record.

        Args:
          invitation_id: Invitation identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._post(
            path_template("/api/libraries/invitations/{invitation_id}/disable", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationResponse,
        )

    async def join(
        self,
        invitation_id: str,
        *,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationJoinResponse:
        """Admit the caller atomically or return their unchanged existing access.

        Retrying
        an uncertain join unchanged consumes no additional place. Invalid secrets or
        unavailable libraries return a generic 404; retry with a valid, available link.
        Expired, disabled, exhausted, or removal-cutoff invitations return 409; request
        a new invitation. Admission disabled returns 503; retry after it becomes
        available.

        Args:
          invitation_id: Invitation identifier.

          secret: Opaque secret from the invitation URL fragment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._post(
            path_template("/api/libraries/invitations/{invitation_id}/join", invitation_id=invitation_id),
            body=await async_maybe_transform({"secret": secret}, invitation_join_params.InvitationJoinParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationJoinResponse,
        )

    async def link(
        self,
        invitation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationLinkResponse:
        """Return an active invitation's existing link without changing its policy or
        usage.

        Inactive invitations return 409 without a link; retrying unchanged cannot
        reactivate one.

        Args:
          invitation_id: Invitation identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._get(
            path_template("/api/libraries/invitations/{invitation_id}/link", invitation_id=invitation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationLinkResponse,
        )

    async def preview(
        self,
        invitation_id: str,
        *,
        secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvitationPreviewResponse:
        """
        Return library attribution and the caller's current eligibility without
        admitting them or reserving a place. Invalid secrets and unavailable libraries
        return the same generic 404; retry with a valid, available invitation link.

        Args:
          invitation_id: Invitation identifier.

          secret: Opaque secret from the invitation URL fragment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invitation_id:
            raise ValueError(f"Expected a non-empty value for `invitation_id` but received {invitation_id!r}")
        return await self._post(
            path_template("/api/libraries/invitations/{invitation_id}/preview", invitation_id=invitation_id),
            body=await async_maybe_transform({"secret": secret}, invitation_preview_params.InvitationPreviewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvitationPreviewResponse,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_raw_response_wrapper(
            invitations.create,
        )
        self.list = to_raw_response_wrapper(
            invitations.list,
        )
        self.disable = to_raw_response_wrapper(
            invitations.disable,
        )
        self.join = to_raw_response_wrapper(
            invitations.join,
        )
        self.link = to_raw_response_wrapper(
            invitations.link,
        )
        self.preview = to_raw_response_wrapper(
            invitations.preview,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_raw_response_wrapper(
            invitations.create,
        )
        self.list = async_to_raw_response_wrapper(
            invitations.list,
        )
        self.disable = async_to_raw_response_wrapper(
            invitations.disable,
        )
        self.join = async_to_raw_response_wrapper(
            invitations.join,
        )
        self.link = async_to_raw_response_wrapper(
            invitations.link,
        )
        self.preview = async_to_raw_response_wrapper(
            invitations.preview,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = to_streamed_response_wrapper(
            invitations.list,
        )
        self.disable = to_streamed_response_wrapper(
            invitations.disable,
        )
        self.join = to_streamed_response_wrapper(
            invitations.join,
        )
        self.link = to_streamed_response_wrapper(
            invitations.link,
        )
        self.preview = to_streamed_response_wrapper(
            invitations.preview,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            invitations.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            invitations.disable,
        )
        self.join = async_to_streamed_response_wrapper(
            invitations.join,
        )
        self.link = async_to_streamed_response_wrapper(
            invitations.link,
        )
        self.preview = async_to_streamed_response_wrapper(
            invitations.preview,
        )
