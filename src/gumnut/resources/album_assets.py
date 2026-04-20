# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import album_asset_list_params
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
from ..types.album_asset_response import AlbumAssetResponse

__all__ = ["AlbumAssetsResource", "AsyncAlbumAssetsResource"]


class AlbumAssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlbumAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlbumAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlbumAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AlbumAssetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AlbumAssetResponse]:
        """
        Returns paginated _link_ records describing which assets are in which albums —
        each row contains `album_id` + `asset_id` + link timestamps, not the full asset
        or album metadata. Use this when you specifically need the junction records (for
        sync or change tracking).

        **For most use cases you want a different tool:** use `list_assets` with
        `album_id` to get the full asset metadata for a specific album; use
        `list_albums` with `asset_id` to find which albums contain an asset.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last album-asset in `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Return only link records for this album ID. Equivalent to 'list the assets in
              this album' — in most cases prefer `list_assets` with `album_id` to get the
              asset metadata directly instead of the lightweight link records.

          asset_id: Return only link records for this asset ID. Equivalent to 'which albums contain
              this asset' — in most cases prefer `list_albums` with `asset_id` to get the
              album metadata directly.

          ids: Look up specific album-asset link records by ID (max 100). The ID has the
              `album_asset_` prefix.

          library_id: Library to list from. Optional if the user has a single library; required when
              they have multiple.

          limit: Maximum number of link records per page (1–200). Defaults to 20.

          starting_after_id: Cursor for pagination. Pass the `id` of the last album-asset in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/album-assets",
            page=SyncCursorPage[AlbumAssetResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                    },
                    album_asset_list_params.AlbumAssetListParams,
                ),
            ),
            model=AlbumAssetResponse,
        )

    def get(
        self,
        album_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumAssetResponse:
        """
        Fetches one album-asset link record (the junction row between an album and an
        asset). Rarely needed directly; most callers want `get_asset` or `get_album`
        instead.

        Args:
          album_asset_id: Album-asset junction row ID (with `album_asset_` prefix). Obtain from
              `list_album_assets`. Not the same as `asset_id` or `album_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_asset_id:
            raise ValueError(f"Expected a non-empty value for `album_asset_id` but received {album_asset_id!r}")
        return self._get(
            path_template("/api/album-assets/{album_asset_id}", album_asset_id=album_asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumAssetResponse,
        )


class AsyncAlbumAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlbumAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlbumAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlbumAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncAlbumAssetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AlbumAssetResponse, AsyncCursorPage[AlbumAssetResponse]]:
        """
        Returns paginated _link_ records describing which assets are in which albums —
        each row contains `album_id` + `asset_id` + link timestamps, not the full asset
        or album metadata. Use this when you specifically need the junction records (for
        sync or change tracking).

        **For most use cases you want a different tool:** use `list_assets` with
        `album_id` to get the full asset metadata for a specific album; use
        `list_albums` with `asset_id` to find which albums contain an asset.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last album-asset in `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Return only link records for this album ID. Equivalent to 'list the assets in
              this album' — in most cases prefer `list_assets` with `album_id` to get the
              asset metadata directly instead of the lightweight link records.

          asset_id: Return only link records for this asset ID. Equivalent to 'which albums contain
              this asset' — in most cases prefer `list_albums` with `asset_id` to get the
              album metadata directly.

          ids: Look up specific album-asset link records by ID (max 100). The ID has the
              `album_asset_` prefix.

          library_id: Library to list from. Optional if the user has a single library; required when
              they have multiple.

          limit: Maximum number of link records per page (1–200). Defaults to 20.

          starting_after_id: Cursor for pagination. Pass the `id` of the last album-asset in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/album-assets",
            page=AsyncCursorPage[AlbumAssetResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                    },
                    album_asset_list_params.AlbumAssetListParams,
                ),
            ),
            model=AlbumAssetResponse,
        )

    async def get(
        self,
        album_asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumAssetResponse:
        """
        Fetches one album-asset link record (the junction row between an album and an
        asset). Rarely needed directly; most callers want `get_asset` or `get_album`
        instead.

        Args:
          album_asset_id: Album-asset junction row ID (with `album_asset_` prefix). Obtain from
              `list_album_assets`. Not the same as `asset_id` or `album_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_asset_id:
            raise ValueError(f"Expected a non-empty value for `album_asset_id` but received {album_asset_id!r}")
        return await self._get(
            path_template("/api/album-assets/{album_asset_id}", album_asset_id=album_asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumAssetResponse,
        )


class AlbumAssetsResourceWithRawResponse:
    def __init__(self, album_assets: AlbumAssetsResource) -> None:
        self._album_assets = album_assets

        self.list = to_raw_response_wrapper(
            album_assets.list,
        )
        self.get = to_raw_response_wrapper(
            album_assets.get,
        )


class AsyncAlbumAssetsResourceWithRawResponse:
    def __init__(self, album_assets: AsyncAlbumAssetsResource) -> None:
        self._album_assets = album_assets

        self.list = async_to_raw_response_wrapper(
            album_assets.list,
        )
        self.get = async_to_raw_response_wrapper(
            album_assets.get,
        )


class AlbumAssetsResourceWithStreamingResponse:
    def __init__(self, album_assets: AlbumAssetsResource) -> None:
        self._album_assets = album_assets

        self.list = to_streamed_response_wrapper(
            album_assets.list,
        )
        self.get = to_streamed_response_wrapper(
            album_assets.get,
        )


class AsyncAlbumAssetsResourceWithStreamingResponse:
    def __init__(self, album_assets: AsyncAlbumAssetsResource) -> None:
        self._album_assets = album_assets

        self.list = async_to_streamed_response_wrapper(
            album_assets.list,
        )
        self.get = async_to_streamed_response_wrapper(
            album_assets.get,
        )
