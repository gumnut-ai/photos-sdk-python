# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import stack_list_stacks_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.stack_list_stacks_response import StackListStacksResponse
from ..types.stack_retrieve_stack_response import StackRetrieveStackResponse

__all__ = ["StacksResource", "AsyncStacksResource"]


class StacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return StacksResourceWithStreamingResponse(self)

    def list_stacks(
        self,
        *,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        origin: Optional[Literal["auto_burst", "user"]] | Omit = omit,
        primary_asset_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[StackListStacksResponse]:
        """
        Returns a paginated list of stacks — assets grouped for collapsed display,
        whether detected automatically or grouped by the user — ordered by `id`: stable,
        but arbitrary rather than chronological.

        `list_stacks` returns stack metadata only; it does not return the assets inside
        a stack. To get a stack's frames, use `list_assets` with `stack_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last stack in `data` as `starting_after_id` to fetch the next page.

        Args:
          ids: Look up specific stacks by ID (max 200; each ID has the `asset_stack_` prefix).
              Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=asset_stack_1,asset_stack_2`).

          library_id: Library to list stacks from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of stacks to return per page (1–200). Defaults to 20.

          origin: Return only stacks with this provenance.

          primary_asset_id: Return only the stack that pins this asset (with `asset_` prefix) as its cover.

          starting_after_id: Cursor for pagination. Pass the `id` of the last stack in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/stacks",
            page=SyncCursorPage[StackListStacksResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "origin": origin,
                        "primary_asset_id": primary_asset_id,
                        "starting_after_id": starting_after_id,
                    },
                    stack_list_stacks_params.StackListStacksParams,
                ),
            ),
            model=StackListStacksResponse,
        )

    def retrieve_stack(
        self,
        stack_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackRetrieveStackResponse:
        """Fetches one stack's metadata by ID (pinned cover, live member count,
        provenance).

        The response is metadata only and does not include the stack's
        assets — to get its frames, use `list_assets` with `stack_id`.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) to fetch. Obtain from `list_stacks`, or
              from the `stack_id` field carried by any asset that belongs to a stack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return self._get(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRetrieveStackResponse,
        )


class AsyncStacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncStacksResourceWithStreamingResponse(self)

    def list_stacks(
        self,
        *,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        origin: Optional[Literal["auto_burst", "user"]] | Omit = omit,
        primary_asset_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[StackListStacksResponse, AsyncCursorPage[StackListStacksResponse]]:
        """
        Returns a paginated list of stacks — assets grouped for collapsed display,
        whether detected automatically or grouped by the user — ordered by `id`: stable,
        but arbitrary rather than chronological.

        `list_stacks` returns stack metadata only; it does not return the assets inside
        a stack. To get a stack's frames, use `list_assets` with `stack_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last stack in `data` as `starting_after_id` to fetch the next page.

        Args:
          ids: Look up specific stacks by ID (max 200; each ID has the `asset_stack_` prefix).
              Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=asset_stack_1,asset_stack_2`).

          library_id: Library to list stacks from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of stacks to return per page (1–200). Defaults to 20.

          origin: Return only stacks with this provenance.

          primary_asset_id: Return only the stack that pins this asset (with `asset_` prefix) as its cover.

          starting_after_id: Cursor for pagination. Pass the `id` of the last stack in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/stacks",
            page=AsyncCursorPage[StackListStacksResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "origin": origin,
                        "primary_asset_id": primary_asset_id,
                        "starting_after_id": starting_after_id,
                    },
                    stack_list_stacks_params.StackListStacksParams,
                ),
            ),
            model=StackListStacksResponse,
        )

    async def retrieve_stack(
        self,
        stack_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackRetrieveStackResponse:
        """Fetches one stack's metadata by ID (pinned cover, live member count,
        provenance).

        The response is metadata only and does not include the stack's
        assets — to get its frames, use `list_assets` with `stack_id`.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) to fetch. Obtain from `list_stacks`, or
              from the `stack_id` field carried by any asset that belongs to a stack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return await self._get(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRetrieveStackResponse,
        )


class StacksResourceWithRawResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.list_stacks = to_raw_response_wrapper(
            stacks.list_stacks,
        )
        self.retrieve_stack = to_raw_response_wrapper(
            stacks.retrieve_stack,
        )


class AsyncStacksResourceWithRawResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.list_stacks = async_to_raw_response_wrapper(
            stacks.list_stacks,
        )
        self.retrieve_stack = async_to_raw_response_wrapper(
            stacks.retrieve_stack,
        )


class StacksResourceWithStreamingResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.list_stacks = to_streamed_response_wrapper(
            stacks.list_stacks,
        )
        self.retrieve_stack = to_streamed_response_wrapper(
            stacks.retrieve_stack,
        )


class AsyncStacksResourceWithStreamingResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.list_stacks = async_to_streamed_response_wrapper(
            stacks.list_stacks,
        )
        self.retrieve_stack = async_to_streamed_response_wrapper(
            stacks.retrieve_stack,
        )
