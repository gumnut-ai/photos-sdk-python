# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import album_list_params, album_create_params, album_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .assets_associations import (
    AssetsAssociationsResource,
    AsyncAssetsAssociationsResource,
    AssetsAssociationsResourceWithRawResponse,
    AsyncAssetsAssociationsResourceWithRawResponse,
    AssetsAssociationsResourceWithStreamingResponse,
    AsyncAssetsAssociationsResourceWithStreamingResponse,
)
from ...types.album_response import AlbumResponse

__all__ = ["AlbumsResource", "AsyncAlbumsResource"]


class AlbumsResource(SyncAPIResource):
    @cached_property
    def assets_associations(self) -> AssetsAssociationsResource:
        return AssetsAssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlbumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlbumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlbumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AlbumsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Creates an album (with optional name and description) and returns it.

        The album
        starts empty — follow up with `add_assets_to_album` to populate it. To rename an
        existing album, use `update_album` instead of creating a new one.

        Args:
          description: Optional free-form description shown alongside the album name.

          library_id: Library to create the album in. Optional if the user has a single library;
              required when they have multiple. Use `list_libraries` to enumerate.

          name: Display name for the new album. Optional; callers that need to name an album can
              set it here or via `update_album` after creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/albums",
            body=maybe_transform(
                {
                    "description": description,
                    "library_id": library_id,
                    "name": name,
                },
                album_create_params.AlbumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    def retrieve(
        self,
        album_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Fetches one album's metadata (name, description, cover, counts).

        Use when you
        already have an album ID. Does not include the album's assets — use
        `list_album_assets` or `list_assets` with `album_id` for that.

        Args:
          album_id: Album ID (with `album_` prefix) to fetch. Obtain from `list_albums` (optionally
              filtered by `asset_id` to find albums containing a specific asset),
              `list_album_assets`, or any response containing an album reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return self._get(
            path_template("/api/albums/{album_id}", album_id=album_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    def update(
        self,
        album_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Updates the `name` and/or `description` of an existing album.

        Only the fields
        included in the request body are changed. To modify the contents of an album,
        use `add_assets_to_album` / `remove_assets_from_album` instead — this tool only
        changes album metadata.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to rename or re-describe.

          description: New free-form description for the album. Omit to leave unchanged.

          name: New display name for the album. Omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return self._patch(
            path_template("/api/albums/{album_id}", album_id=album_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                album_update_params.AlbumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    def list(
        self,
        *,
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
    ) -> SyncCursorPage[AlbumResponse]:
        """Returns a paginated list of albums ordered by creation time (newest first).

        Use
        this to enumerate a user's albums or to find which albums contain a specific
        asset (via `asset_id`).

        `list_albums` returns album metadata only — to list the assets inside a
        particular album, use `list_album_assets` or `list_assets` with `album_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last album in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only albums that contain this asset. Useful for answering 'which albums
              is this photo in?' without calling `list_album_assets`.

          ids: Look up specific albums by ID (max 100; each ID has the `album_` prefix). Use
              for bulk fetch when IDs are already known.

          library_id: Library to list albums from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of albums to return per page (1–200). Defaults to 20.

          starting_after_id: Cursor for pagination. Pass the `id` of the last album in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/albums",
            page=SyncCursorPage[AlbumResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                    },
                    album_list_params.AlbumListParams,
                ),
            ),
            model=AlbumResponse,
        )

    def delete(
        self,
        album_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes the album itself.

        Assets that were in the album remain in the library —
        only the album and its asset-links are removed. Use `trash_assets` (or
        `permanently_delete_assets` for irreversible removal) to delete the underlying
        assets, or `remove_assets_from_album` to detach specific assets from an album
        you want to keep.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/albums/{album_id}", album_id=album_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAlbumsResource(AsyncAPIResource):
    @cached_property
    def assets_associations(self) -> AsyncAssetsAssociationsResource:
        return AsyncAssetsAssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlbumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlbumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlbumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncAlbumsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Creates an album (with optional name and description) and returns it.

        The album
        starts empty — follow up with `add_assets_to_album` to populate it. To rename an
        existing album, use `update_album` instead of creating a new one.

        Args:
          description: Optional free-form description shown alongside the album name.

          library_id: Library to create the album in. Optional if the user has a single library;
              required when they have multiple. Use `list_libraries` to enumerate.

          name: Display name for the new album. Optional; callers that need to name an album can
              set it here or via `update_album` after creation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/albums",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "library_id": library_id,
                    "name": name,
                },
                album_create_params.AlbumCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    async def retrieve(
        self,
        album_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Fetches one album's metadata (name, description, cover, counts).

        Use when you
        already have an album ID. Does not include the album's assets — use
        `list_album_assets` or `list_assets` with `album_id` for that.

        Args:
          album_id: Album ID (with `album_` prefix) to fetch. Obtain from `list_albums` (optionally
              filtered by `asset_id` to find albums containing a specific asset),
              `list_album_assets`, or any response containing an album reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return await self._get(
            path_template("/api/albums/{album_id}", album_id=album_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    async def update(
        self,
        album_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlbumResponse:
        """Updates the `name` and/or `description` of an existing album.

        Only the fields
        included in the request body are changed. To modify the contents of an album,
        use `add_assets_to_album` / `remove_assets_from_album` instead — this tool only
        changes album metadata.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to rename or re-describe.

          description: New free-form description for the album. Omit to leave unchanged.

          name: New display name for the album. Omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        return await self._patch(
            path_template("/api/albums/{album_id}", album_id=album_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                album_update_params.AlbumUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlbumResponse,
        )

    def list(
        self,
        *,
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
    ) -> AsyncPaginator[AlbumResponse, AsyncCursorPage[AlbumResponse]]:
        """Returns a paginated list of albums ordered by creation time (newest first).

        Use
        this to enumerate a user's albums or to find which albums contain a specific
        asset (via `asset_id`).

        `list_albums` returns album metadata only — to list the assets inside a
        particular album, use `list_album_assets` or `list_assets` with `album_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last album in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only albums that contain this asset. Useful for answering 'which albums
              is this photo in?' without calling `list_album_assets`.

          ids: Look up specific albums by ID (max 100; each ID has the `album_` prefix). Use
              for bulk fetch when IDs are already known.

          library_id: Library to list albums from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of albums to return per page (1–200). Defaults to 20.

          starting_after_id: Cursor for pagination. Pass the `id` of the last album in the previous
              response's `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/albums",
            page=AsyncCursorPage[AlbumResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "starting_after_id": starting_after_id,
                    },
                    album_list_params.AlbumListParams,
                ),
            ),
            model=AlbumResponse,
        )

    async def delete(
        self,
        album_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes the album itself.

        Assets that were in the album remain in the library —
        only the album and its asset-links are removed. Use `trash_assets` (or
        `permanently_delete_assets` for irreversible removal) to delete the underlying
        assets, or `remove_assets_from_album` to detach specific assets from an album
        you want to keep.

        Args:
          album_id: Album ID (with `album_` prefix) of the album to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not album_id:
            raise ValueError(f"Expected a non-empty value for `album_id` but received {album_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/albums/{album_id}", album_id=album_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AlbumsResourceWithRawResponse:
    def __init__(self, albums: AlbumsResource) -> None:
        self._albums = albums

        self.create = to_raw_response_wrapper(
            albums.create,
        )
        self.retrieve = to_raw_response_wrapper(
            albums.retrieve,
        )
        self.update = to_raw_response_wrapper(
            albums.update,
        )
        self.list = to_raw_response_wrapper(
            albums.list,
        )
        self.delete = to_raw_response_wrapper(
            albums.delete,
        )

    @cached_property
    def assets_associations(self) -> AssetsAssociationsResourceWithRawResponse:
        return AssetsAssociationsResourceWithRawResponse(self._albums.assets_associations)


class AsyncAlbumsResourceWithRawResponse:
    def __init__(self, albums: AsyncAlbumsResource) -> None:
        self._albums = albums

        self.create = async_to_raw_response_wrapper(
            albums.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            albums.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            albums.update,
        )
        self.list = async_to_raw_response_wrapper(
            albums.list,
        )
        self.delete = async_to_raw_response_wrapper(
            albums.delete,
        )

    @cached_property
    def assets_associations(self) -> AsyncAssetsAssociationsResourceWithRawResponse:
        return AsyncAssetsAssociationsResourceWithRawResponse(self._albums.assets_associations)


class AlbumsResourceWithStreamingResponse:
    def __init__(self, albums: AlbumsResource) -> None:
        self._albums = albums

        self.create = to_streamed_response_wrapper(
            albums.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            albums.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            albums.update,
        )
        self.list = to_streamed_response_wrapper(
            albums.list,
        )
        self.delete = to_streamed_response_wrapper(
            albums.delete,
        )

    @cached_property
    def assets_associations(self) -> AssetsAssociationsResourceWithStreamingResponse:
        return AssetsAssociationsResourceWithStreamingResponse(self._albums.assets_associations)


class AsyncAlbumsResourceWithStreamingResponse:
    def __init__(self, albums: AsyncAlbumsResource) -> None:
        self._albums = albums

        self.create = async_to_streamed_response_wrapper(
            albums.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            albums.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            albums.update,
        )
        self.list = async_to_streamed_response_wrapper(
            albums.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            albums.delete,
        )

    @cached_property
    def assets_associations(self) -> AsyncAssetsAssociationsResourceWithStreamingResponse:
        return AsyncAssetsAssociationsResourceWithStreamingResponse(self._albums.assets_associations)
