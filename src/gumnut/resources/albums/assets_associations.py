# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.albums import assets_association_add_params, assets_association_remove_params
from ...types.albums.assets_association_add_response import AssetsAssociationAddResponse

__all__ = ["AssetsAssociationsResource", "AsyncAssetsAssociationsResource"]


class AssetsAssociationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssetsAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AssetsAssociationsResourceWithStreamingResponse(self)

    def add(
        self,
        album_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetsAssociationAddResponse:
        """Adds one or more existing assets to the specified album.

        Assets must already be
        in the same library as the album (this tool does not upload new assets). Assets
        already in the album are silently skipped and returned separately as
        `duplicate_assets`. Idempotent: calling with the same IDs twice leaves the album
        in the same state.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to add the assets to.

          asset_ids: Asset IDs (with `asset_` prefix) to associate with the album. Get IDs from
              `list_assets`, `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return self._post(
            path_template("/api/albums/{album_id}/assets", album_id=album_id),
            body=maybe_transform({"asset_ids": asset_ids}, assets_association_add_params.AssetsAssociationAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetsAssociationAddResponse,
        )

    def remove(
        self,
        album_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detaches one or more assets from the given album.

        The assets remain in the
        library and in any other albums they belong to. Use `delete_asset` to delete the
        asset entirely. To empty an album completely, call `list_album_assets` to get
        the links and then remove them, or delete the album itself with `delete_album`.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to detach assets from.

          asset_ids: Asset IDs (with `asset_` prefix) to associate with the album. Get IDs from
              `list_assets`, `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/albums/{album_id}/assets", album_id=album_id),
            body=maybe_transform(
                {"asset_ids": asset_ids}, assets_association_remove_params.AssetsAssociationRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAssetsAssociationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncAssetsAssociationsResourceWithStreamingResponse(self)

    async def add(
        self,
        album_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetsAssociationAddResponse:
        """Adds one or more existing assets to the specified album.

        Assets must already be
        in the same library as the album (this tool does not upload new assets). Assets
        already in the album are silently skipped and returned separately as
        `duplicate_assets`. Idempotent: calling with the same IDs twice leaves the album
        in the same state.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to add the assets to.

          asset_ids: Asset IDs (with `asset_` prefix) to associate with the album. Get IDs from
              `list_assets`, `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return await self._post(
            path_template("/api/albums/{album_id}/assets", album_id=album_id),
            body=await async_maybe_transform(
                {"asset_ids": asset_ids}, assets_association_add_params.AssetsAssociationAddParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetsAssociationAddResponse,
        )

    async def remove(
        self,
        album_id: str,
        *,
        asset_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detaches one or more assets from the given album.

        The assets remain in the
        library and in any other albums they belong to. Use `delete_asset` to delete the
        asset entirely. To empty an album completely, call `list_album_assets` to get
        the links and then remove them, or delete the album itself with `delete_album`.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to detach assets from.

          asset_ids: Asset IDs (with `asset_` prefix) to associate with the album. Get IDs from
              `list_assets`, `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/albums/{album_id}/assets", album_id=album_id),
            body=await async_maybe_transform(
                {"asset_ids": asset_ids}, assets_association_remove_params.AssetsAssociationRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AssetsAssociationsResourceWithRawResponse:
    def __init__(self, assets_associations: AssetsAssociationsResource) -> None:
        self._assets_associations = assets_associations

        self.add = to_raw_response_wrapper(
            assets_associations.add,
        )
        self.remove = to_raw_response_wrapper(
            assets_associations.remove,
        )


class AsyncAssetsAssociationsResourceWithRawResponse:
    def __init__(self, assets_associations: AsyncAssetsAssociationsResource) -> None:
        self._assets_associations = assets_associations

        self.add = async_to_raw_response_wrapper(
            assets_associations.add,
        )
        self.remove = async_to_raw_response_wrapper(
            assets_associations.remove,
        )


class AssetsAssociationsResourceWithStreamingResponse:
    def __init__(self, assets_associations: AssetsAssociationsResource) -> None:
        self._assets_associations = assets_associations

        self.add = to_streamed_response_wrapper(
            assets_associations.add,
        )
        self.remove = to_streamed_response_wrapper(
            assets_associations.remove,
        )


class AsyncAssetsAssociationsResourceWithStreamingResponse:
    def __init__(self, assets_associations: AsyncAssetsAssociationsResource) -> None:
        self._assets_associations = assets_associations

        self.add = async_to_streamed_response_wrapper(
            assets_associations.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            assets_associations.remove,
        )
