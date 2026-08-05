# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    stack_set_cover_params,
    stack_list_stacks_params,
    stack_create_stack_params,
    stack_remove_assets_params,
    stack_add_assets_to_stack_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.stack_delete_response import StackDeleteResponse
from ..types.stack_set_cover_response import StackSetCoverResponse
from ..types.stack_list_stacks_response import StackListStacksResponse
from ..types.stack_create_stack_response import StackCreateStackResponse
from ..types.stack_remove_assets_response import StackRemoveAssetsResponse
from ..types.stack_retrieve_stack_response import StackRetrieveStackResponse
from ..types.stack_add_assets_to_stack_response import StackAddAssetsToStackResponse

__all__ = ["StacksResource", "AsyncStacksResource"]


class StacksResource(SyncAPIResource):
    """
    Groups of related shots of the same moment, presented as a single unit with a cover asset.
    """

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

    def delete(
        self,
        stack_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackDeleteResponse:
        """
        Dissolves the stack: the grouping is removed and every member frame returns to
        loose, individual display. The photos themselves are untouched — nothing is
        trashed or deleted from the library; like `remove_assets_from_album`, this only
        removes an organizational grouping. Use `trash_assets` to soft-delete the
        underlying assets. If a concurrent mutation adds a frame mid-delete, returns 409
        and nothing is changed; retry the request.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to dissolve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return self._delete(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackDeleteResponse,
        )

    def add_assets_to_stack(
        self,
        stack_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackAddAssetsToStackResponse:
        """Adds one or more existing assets to the stack.

        An asset already in another stack
        is reconciled exactly as `create_stack` does. Ids already in this stack are
        silently skipped.

        An add that changes membership marks the stack user-owned (`origin = user`),
        which freezes it against burst re-detection; a request that changes nothing
        leaves `origin` unchanged.

        If a concurrent stack change invalidates the request mid-flight, it returns 409
        and nothing is changed; retry the request unchanged, except where the 409
        reports the target stack itself is gone, which is terminal.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to add the assets to.

          asset_ids: Asset IDs (with `asset_` prefix) to add to the stack — all in the stack's
              library.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return self._post(
            path_template("/api/stacks/{stack_id}/assets", stack_id=stack_id),
            body=maybe_transform(
                {"asset_ids": asset_ids}, stack_add_assets_to_stack_params.StackAddAssetsToStackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackAddAssetsToStackResponse,
        )

    def create_stack(
        self,
        *,
        asset_ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        primary_asset_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateStackResponse:
        """
        Groups two or more existing assets into a new user-owned stack (`origin = user`)
        for collapsed display. A user-owned stack is never re-segmented by burst
        re-detection.

        An asset already in another stack is repointed into the new one, folding that
        stack in whole if it was its pinned cover; a stack left with fewer than 2
        members dissolves. The photos themselves are untouched.

        If a concurrent stack change invalidates the request mid-flight, it returns 409
        and nothing is created; retry the request unchanged.

        Args:
          asset_ids: Asset IDs (with `asset_` prefix) to group into the new stack — at least 2
              distinct ids, all in the target library.

          library_id: Library to create the stack in. Optional if the user has a single library;
              required when they have multiple.

          primary_asset_id: Asset ID (with `asset_` prefix) to pin as the stack's cover; must be one of
              `asset_ids`. Omit to leave the cover unpinned — there is no automatic pick, and
              clients choose their own display cover for an unpinned stack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/stacks",
            body=maybe_transform(
                {
                    "asset_ids": asset_ids,
                    "library_id": library_id,
                    "primary_asset_id": primary_asset_id,
                },
                stack_create_stack_params.StackCreateStackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateStackResponse,
        )

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
              when they have multiple.

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

    def remove_assets(
        self,
        stack_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackRemoveAssetsResponse:
        """Pulls one or more frames out of the stack.

        The assets themselves are untouched —
        they remain in the library (and in any albums) and simply appear as individual
        photos again. IDs that are not current members of the stack are silently
        ignored.

        If a removed frame was the pinned cover, the pin is cleared with no automatic
        re-pick — clients choose their own display cover. A stack that survives the
        removal is marked user-owned (`origin = user`) so burst re-detection honors the
        edit; a removal that leaves fewer than 2 members dissolves the stack entirely,
        returning its remaining frames to loose display too. Trashed frames still count
        as members for that threshold (unlike `asset_count`, which excludes them), so a
        stack can survive with `asset_count` below 2.

        Up to 200 ids per request; over-cap requests return 422.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to pull frames out of.

          asset_ids: Asset IDs (with `asset_` prefix) to pull out of the stack. Get member IDs from
              `list_assets` with `stack_id`. Up to 200 ids per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return self._delete(
            path_template("/api/stacks/{stack_id}/assets", stack_id=stack_id),
            body=maybe_transform({"asset_ids": asset_ids}, stack_remove_assets_params.StackRemoveAssetsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRemoveAssetsResponse,
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
          stack_id: Stack ID (with `asset_stack_` prefix) to fetch. Carried by the `stack_id` field
              on any asset that belongs to a stack.

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

    def set_cover(
        self,
        stack_id: str,
        *,
        primary_asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackSetCoverResponse:
        """
        Pins one of the stack's own live members as its cover (`primary_asset_id`).
        Setting a cover marks the stack as user-owned (`origin = user`), which freezes
        it — membership included — against burst re-detection, so neither the chosen
        cover nor the frame grouping is ever silently reverted by a later detection
        pass.

        `primary_asset_id` cannot be null: there is no manual clear-cover operation. A
        pin clears automatically when the pinned frame is removed from the stack or
        permanently deleted.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to pin a cover on.

          primary_asset_id: Asset ID (with `asset_` prefix) to pin as the stack's cover. Must be a live,
              current member of this stack — get member IDs from `list_assets` with
              `stack_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return self._patch(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            body=maybe_transform({"primary_asset_id": primary_asset_id}, stack_set_cover_params.StackSetCoverParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackSetCoverResponse,
        )


class AsyncStacksResource(AsyncAPIResource):
    """
    Groups of related shots of the same moment, presented as a single unit with a cover asset.
    """

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

    async def delete(
        self,
        stack_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackDeleteResponse:
        """
        Dissolves the stack: the grouping is removed and every member frame returns to
        loose, individual display. The photos themselves are untouched — nothing is
        trashed or deleted from the library; like `remove_assets_from_album`, this only
        removes an organizational grouping. Use `trash_assets` to soft-delete the
        underlying assets. If a concurrent mutation adds a frame mid-delete, returns 409
        and nothing is changed; retry the request.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to dissolve.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return await self._delete(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackDeleteResponse,
        )

    async def add_assets_to_stack(
        self,
        stack_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackAddAssetsToStackResponse:
        """Adds one or more existing assets to the stack.

        An asset already in another stack
        is reconciled exactly as `create_stack` does. Ids already in this stack are
        silently skipped.

        An add that changes membership marks the stack user-owned (`origin = user`),
        which freezes it against burst re-detection; a request that changes nothing
        leaves `origin` unchanged.

        If a concurrent stack change invalidates the request mid-flight, it returns 409
        and nothing is changed; retry the request unchanged, except where the 409
        reports the target stack itself is gone, which is terminal.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to add the assets to.

          asset_ids: Asset IDs (with `asset_` prefix) to add to the stack — all in the stack's
              library.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return await self._post(
            path_template("/api/stacks/{stack_id}/assets", stack_id=stack_id),
            body=await async_maybe_transform(
                {"asset_ids": asset_ids}, stack_add_assets_to_stack_params.StackAddAssetsToStackParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackAddAssetsToStackResponse,
        )

    async def create_stack(
        self,
        *,
        asset_ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        primary_asset_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateStackResponse:
        """
        Groups two or more existing assets into a new user-owned stack (`origin = user`)
        for collapsed display. A user-owned stack is never re-segmented by burst
        re-detection.

        An asset already in another stack is repointed into the new one, folding that
        stack in whole if it was its pinned cover; a stack left with fewer than 2
        members dissolves. The photos themselves are untouched.

        If a concurrent stack change invalidates the request mid-flight, it returns 409
        and nothing is created; retry the request unchanged.

        Args:
          asset_ids: Asset IDs (with `asset_` prefix) to group into the new stack — at least 2
              distinct ids, all in the target library.

          library_id: Library to create the stack in. Optional if the user has a single library;
              required when they have multiple.

          primary_asset_id: Asset ID (with `asset_` prefix) to pin as the stack's cover; must be one of
              `asset_ids`. Omit to leave the cover unpinned — there is no automatic pick, and
              clients choose their own display cover for an unpinned stack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/stacks",
            body=await async_maybe_transform(
                {
                    "asset_ids": asset_ids,
                    "library_id": library_id,
                    "primary_asset_id": primary_asset_id,
                },
                stack_create_stack_params.StackCreateStackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateStackResponse,
        )

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
              when they have multiple.

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

    async def remove_assets(
        self,
        stack_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackRemoveAssetsResponse:
        """Pulls one or more frames out of the stack.

        The assets themselves are untouched —
        they remain in the library (and in any albums) and simply appear as individual
        photos again. IDs that are not current members of the stack are silently
        ignored.

        If a removed frame was the pinned cover, the pin is cleared with no automatic
        re-pick — clients choose their own display cover. A stack that survives the
        removal is marked user-owned (`origin = user`) so burst re-detection honors the
        edit; a removal that leaves fewer than 2 members dissolves the stack entirely,
        returning its remaining frames to loose display too. Trashed frames still count
        as members for that threshold (unlike `asset_count`, which excludes them), so a
        stack can survive with `asset_count` below 2.

        Up to 200 ids per request; over-cap requests return 422.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to pull frames out of.

          asset_ids: Asset IDs (with `asset_` prefix) to pull out of the stack. Get member IDs from
              `list_assets` with `stack_id`. Up to 200 ids per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return await self._delete(
            path_template("/api/stacks/{stack_id}/assets", stack_id=stack_id),
            body=await async_maybe_transform(
                {"asset_ids": asset_ids}, stack_remove_assets_params.StackRemoveAssetsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRemoveAssetsResponse,
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
          stack_id: Stack ID (with `asset_stack_` prefix) to fetch. Carried by the `stack_id` field
              on any asset that belongs to a stack.

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

    async def set_cover(
        self,
        stack_id: str,
        *,
        primary_asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackSetCoverResponse:
        """
        Pins one of the stack's own live members as its cover (`primary_asset_id`).
        Setting a cover marks the stack as user-owned (`origin = user`), which freezes
        it — membership included — against burst re-detection, so neither the chosen
        cover nor the frame grouping is ever silently reverted by a later detection
        pass.

        `primary_asset_id` cannot be null: there is no manual clear-cover operation. A
        pin clears automatically when the pinned frame is removed from the stack or
        permanently deleted.

        Args:
          stack_id: Stack ID (with `asset_stack_` prefix) of the stack to pin a cover on.

          primary_asset_id: Asset ID (with `asset_` prefix) to pin as the stack's cover. Must be a live,
              current member of this stack — get member IDs from `list_assets` with
              `stack_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stack_id:
            raise ValueError(f"Expected a non-empty value for `stack_id` but received {stack_id!r}")
        return await self._patch(
            path_template("/api/stacks/{stack_id}", stack_id=stack_id),
            body=await async_maybe_transform(
                {"primary_asset_id": primary_asset_id}, stack_set_cover_params.StackSetCoverParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackSetCoverResponse,
        )


class StacksResourceWithRawResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.delete = to_raw_response_wrapper(
            stacks.delete,
        )
        self.add_assets_to_stack = to_raw_response_wrapper(
            stacks.add_assets_to_stack,
        )
        self.create_stack = to_raw_response_wrapper(
            stacks.create_stack,
        )
        self.list_stacks = to_raw_response_wrapper(
            stacks.list_stacks,
        )
        self.remove_assets = to_raw_response_wrapper(
            stacks.remove_assets,
        )
        self.retrieve_stack = to_raw_response_wrapper(
            stacks.retrieve_stack,
        )
        self.set_cover = to_raw_response_wrapper(
            stacks.set_cover,
        )


class AsyncStacksResourceWithRawResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.delete = async_to_raw_response_wrapper(
            stacks.delete,
        )
        self.add_assets_to_stack = async_to_raw_response_wrapper(
            stacks.add_assets_to_stack,
        )
        self.create_stack = async_to_raw_response_wrapper(
            stacks.create_stack,
        )
        self.list_stacks = async_to_raw_response_wrapper(
            stacks.list_stacks,
        )
        self.remove_assets = async_to_raw_response_wrapper(
            stacks.remove_assets,
        )
        self.retrieve_stack = async_to_raw_response_wrapper(
            stacks.retrieve_stack,
        )
        self.set_cover = async_to_raw_response_wrapper(
            stacks.set_cover,
        )


class StacksResourceWithStreamingResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.delete = to_streamed_response_wrapper(
            stacks.delete,
        )
        self.add_assets_to_stack = to_streamed_response_wrapper(
            stacks.add_assets_to_stack,
        )
        self.create_stack = to_streamed_response_wrapper(
            stacks.create_stack,
        )
        self.list_stacks = to_streamed_response_wrapper(
            stacks.list_stacks,
        )
        self.remove_assets = to_streamed_response_wrapper(
            stacks.remove_assets,
        )
        self.retrieve_stack = to_streamed_response_wrapper(
            stacks.retrieve_stack,
        )
        self.set_cover = to_streamed_response_wrapper(
            stacks.set_cover,
        )


class AsyncStacksResourceWithStreamingResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.delete = async_to_streamed_response_wrapper(
            stacks.delete,
        )
        self.add_assets_to_stack = async_to_streamed_response_wrapper(
            stacks.add_assets_to_stack,
        )
        self.create_stack = async_to_streamed_response_wrapper(
            stacks.create_stack,
        )
        self.list_stacks = async_to_streamed_response_wrapper(
            stacks.list_stacks,
        )
        self.remove_assets = async_to_streamed_response_wrapper(
            stacks.remove_assets,
        )
        self.retrieve_stack = async_to_streamed_response_wrapper(
            stacks.retrieve_stack,
        )
        self.set_cover = async_to_streamed_response_wrapper(
            stacks.set_cover,
        )
