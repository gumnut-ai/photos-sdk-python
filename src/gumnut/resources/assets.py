# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ..types import asset_list_params, asset_counts_params, asset_create_params, asset_check_existence_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
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
from ..types.asset_response import AssetResponse
from ..types.asset_count_response import AssetCountResponse
from ..types.asset_existence_response import AssetExistenceResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        asset_data: FileTypes,
        device_asset_id: str,
        device_id: str,
        file_created_at: Union[str, datetime],
        file_modified_at: Union[str, datetime],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Uploads a new asset file (image or video) along with its metadata to the
        specified library. If no library_id is provided and the user only has one
        library, uses that library. If the user has multiple libraries, library_id is
        required.

        Args:
          asset_data: The asset file to upload

          library_id: Library to upload asset to (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "asset_data": asset_data,
                "device_asset_id": device_asset_id,
                "device_id": device_id,
                "file_created_at": file_created_at,
                "file_modified_at": file_modified_at,
                "library_id": library_id,
            },
            [["asset_data"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["asset_data"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/assets",
            body=maybe_transform(body, asset_create_params.AssetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """Fetches one asset and its associated metadata.

        Use this when you already have a
        specific asset ID (e.g., from `list_assets`, `search_assets`, or
        `list_album_assets`) and need its full details. For bulk fetch of multiple known
        IDs, prefer `list_assets` with the `ids` parameter to avoid N round trips.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to fetch. Obtain from `list_assets`,
              `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AssetResponse]:
        """
        Returns a paginated list of assets ordered by local capture time (newest first).
        Use this tool for structured browsing and filtering — when the request can be
        expressed as exact filters on album membership, people, date range, or specific
        asset IDs.

        **Use `search_assets` instead** when the request involves natural-language image
        content ('photos of sunsets', 'pictures with my dog'), location or place
        ('photos from Japan'), or any concept requiring semantic understanding of what's
        in the image. `list_assets` does not filter by image content, location, or
        caption text.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last asset in `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Return only assets that are in the album with this ID. Equivalent to calling
              `list_album_assets` with `album_id` and then fetching each asset — prefer this
              param when you need the full asset metadata in one call.

          ids: Look up specific assets by ID (max 100; each ID has the `asset_` prefix). Use
              this for bulk fetch when you already have asset IDs. Combines with other filters
              (album_id, person_id, datetime range) using AND logic — the result is the
              intersection.

          library_id: Library to list assets from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate available libraries.

          limit: Maximum number of assets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              `local_datetime` is the photo's wall-clock time in the device's own timezone.
              Naive values compare directly against `local_datetime`. Timezone-aware values:
              assets with a known offset are compared in UTC (`local_datetime - offset`);
              assets without an offset fall back to wall-clock comparison against
              `local_datetime`. Equivalent in purpose to `captured_after` on `search_assets`
              (naming inconsistency is tracked as a follow-up).

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same awareness/offset semantics as `local_datetime_after`. Equivalent in purpose
              to `captured_before` on `search_assets` (naming inconsistency is tracked as a
              follow-up).

          person_id: Return only assets containing a face belonging to this person. Singular on this
              tool; the sibling `search_assets` uses `person_ids` (plural, ALL-of).

          starting_after_id: Cursor for pagination. Pass the `id` of the last asset in the previous
              response's `data` to fetch the next page. Omit for the first page. `list_assets`
              uses cursor pagination; the sibling `search_assets` uses 1-indexed `page`
              numbers (naming inconsistency is tracked as a follow-up).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/assets",
            page=SyncCursorPage[AssetResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            model=AssetResponse,
        )

    def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the asset entirely — the database record, the stored file, and all
        associated data (faces, album links, etc.). This is irreversible.

        **Use `remove_assets_from_album` instead** when the user only wants to remove an
        asset from a specific album but keep the file in their library. Use
        `delete_album` to remove an album without deleting its assets.

        Args:
          asset_id: Asset ID (with `asset_` prefix) of the asset to permanently delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check_existence(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        checksum_sha1s: Optional[SequenceNotStr[str]] | Omit = omit,
        checksums: Optional[SequenceNotStr[str]] | Omit = omit,
        device_asset_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetExistenceResponse:
        """
        Checks which assets exist in the user's library based on checksums or device
        identifiers. Provide exactly one of: checksums, checksum_sha1s, or (deviceId AND
        deviceAssetIds). List parameters are limited to 5000 items.

        Args:
          library_id: Library to check assets in (optional)

          checksum_sha1s: List of base64-encoded SHA-1 checksums to check for existence (for Immich
              compatibility)

          checksums: List of base64-encoded SHA-256 checksums to check for existence

          device_asset_ids: List of device asset IDs to check for existence (requires deviceId)

          device_id: Device ID to filter assets by (required with deviceAssetIds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/assets/exist",
            body=maybe_transform(
                {
                    "checksum_sha1s": checksum_sha1s,
                    "checksums": checksums,
                    "device_asset_ids": device_asset_ids,
                    "device_id": device_id,
                },
                asset_check_existence_params.AssetCheckExistenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"library_id": library_id}, asset_check_existence_params.AssetCheckExistenceParams
                ),
            ),
            cast_to=AssetExistenceResponse,
        )

    def counts(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        group_by: str | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCountResponse:
        """Returns asset counts grouped by time period.

        Supports optional filtering by
        album, person, or date range. Results are ordered by time bucket descending.

        **Pagination:** When `has_more` is true, pass the last `time_bucket` value from
        `data` as `local_datetime_before` to fetch the next page.

        Args:
          album_id: Filter by assets in a specific album

          group_by: Time period to group counts by. Currently only 'month' is supported.

          library_id: Library to count assets in (optional)

          limit: Maximum number of time buckets to return (1-200)

          local_datetime_after: Only include assets with local_datetime after this value (ISO 8601). Naive
              values compare directly against local_datetime. Timezone-aware values: assets
              with a known offset are compared in UTC (local_datetime - offset); assets
              without an offset fall back to wall-clock comparison against local_datetime.

          local_datetime_before: Only include assets with local_datetime before this value (ISO 8601). Naive
              values compare directly against local_datetime. Timezone-aware values: assets
              with a known offset are compared in UTC (local_datetime - offset); assets
              without an offset fall back to wall-clock comparison against local_datetime. Use
              the last time_bucket from a previous response to paginate.

          person_id: Filter by assets associated with a specific person ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/assets/counts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "group_by": group_by,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "person_id": person_id,
                    },
                    asset_counts_params.AssetCountsParams,
                ),
            ),
            cast_to=AssetCountResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        asset_data: FileTypes,
        device_asset_id: str,
        device_id: str,
        file_created_at: Union[str, datetime],
        file_modified_at: Union[str, datetime],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Uploads a new asset file (image or video) along with its metadata to the
        specified library. If no library_id is provided and the user only has one
        library, uses that library. If the user has multiple libraries, library_id is
        required.

        Args:
          asset_data: The asset file to upload

          library_id: Library to upload asset to (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "asset_data": asset_data,
                "device_asset_id": device_asset_id,
                "device_id": device_id,
                "file_created_at": file_created_at,
                "file_modified_at": file_modified_at,
                "library_id": library_id,
            },
            [["asset_data"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["asset_data"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/assets",
            body=await async_maybe_transform(body, asset_create_params.AssetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    async def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """Fetches one asset and its associated metadata.

        Use this when you already have a
        specific asset ID (e.g., from `list_assets`, `search_assets`, or
        `list_album_assets`) and need its full details. For bulk fetch of multiple known
        IDs, prefer `list_assets` with the `ids` parameter to avoid N round trips.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to fetch. Obtain from `list_assets`,
              `search_assets`, or `list_album_assets`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetResponse, AsyncCursorPage[AssetResponse]]:
        """
        Returns a paginated list of assets ordered by local capture time (newest first).
        Use this tool for structured browsing and filtering — when the request can be
        expressed as exact filters on album membership, people, date range, or specific
        asset IDs.

        **Use `search_assets` instead** when the request involves natural-language image
        content ('photos of sunsets', 'pictures with my dog'), location or place
        ('photos from Japan'), or any concept requiring semantic understanding of what's
        in the image. `list_assets` does not filter by image content, location, or
        caption text.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last asset in `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Return only assets that are in the album with this ID. Equivalent to calling
              `list_album_assets` with `album_id` and then fetching each asset — prefer this
              param when you need the full asset metadata in one call.

          ids: Look up specific assets by ID (max 100; each ID has the `asset_` prefix). Use
              this for bulk fetch when you already have asset IDs. Combines with other filters
              (album_id, person_id, datetime range) using AND logic — the result is the
              intersection.

          library_id: Library to list assets from. Optional if the user has a single library; required
              when they have multiple. Use `list_libraries` to enumerate available libraries.

          limit: Maximum number of assets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              `local_datetime` is the photo's wall-clock time in the device's own timezone.
              Naive values compare directly against `local_datetime`. Timezone-aware values:
              assets with a known offset are compared in UTC (`local_datetime - offset`);
              assets without an offset fall back to wall-clock comparison against
              `local_datetime`. Equivalent in purpose to `captured_after` on `search_assets`
              (naming inconsistency is tracked as a follow-up).

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same awareness/offset semantics as `local_datetime_after`. Equivalent in purpose
              to `captured_before` on `search_assets` (naming inconsistency is tracked as a
              follow-up).

          person_id: Return only assets containing a face belonging to this person. Singular on this
              tool; the sibling `search_assets` uses `person_ids` (plural, ALL-of).

          starting_after_id: Cursor for pagination. Pass the `id` of the last asset in the previous
              response's `data` to fetch the next page. Omit for the first page. `list_assets`
              uses cursor pagination; the sibling `search_assets` uses 1-indexed `page`
              numbers (naming inconsistency is tracked as a follow-up).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/assets",
            page=AsyncCursorPage[AssetResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            model=AssetResponse,
        )

    async def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the asset entirely — the database record, the stored file, and all
        associated data (faces, album links, etc.). This is irreversible.

        **Use `remove_assets_from_album` instead** when the user only wants to remove an
        asset from a specific album but keep the file in their library. Use
        `delete_album` to remove an album without deleting its assets.

        Args:
          asset_id: Asset ID (with `asset_` prefix) of the asset to permanently delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check_existence(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        checksum_sha1s: Optional[SequenceNotStr[str]] | Omit = omit,
        checksums: Optional[SequenceNotStr[str]] | Omit = omit,
        device_asset_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        device_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetExistenceResponse:
        """
        Checks which assets exist in the user's library based on checksums or device
        identifiers. Provide exactly one of: checksums, checksum_sha1s, or (deviceId AND
        deviceAssetIds). List parameters are limited to 5000 items.

        Args:
          library_id: Library to check assets in (optional)

          checksum_sha1s: List of base64-encoded SHA-1 checksums to check for existence (for Immich
              compatibility)

          checksums: List of base64-encoded SHA-256 checksums to check for existence

          device_asset_ids: List of device asset IDs to check for existence (requires deviceId)

          device_id: Device ID to filter assets by (required with deviceAssetIds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/assets/exist",
            body=await async_maybe_transform(
                {
                    "checksum_sha1s": checksum_sha1s,
                    "checksums": checksums,
                    "device_asset_ids": device_asset_ids,
                    "device_id": device_id,
                },
                asset_check_existence_params.AssetCheckExistenceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"library_id": library_id}, asset_check_existence_params.AssetCheckExistenceParams
                ),
            ),
            cast_to=AssetExistenceResponse,
        )

    async def counts(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        group_by: str | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCountResponse:
        """Returns asset counts grouped by time period.

        Supports optional filtering by
        album, person, or date range. Results are ordered by time bucket descending.

        **Pagination:** When `has_more` is true, pass the last `time_bucket` value from
        `data` as `local_datetime_before` to fetch the next page.

        Args:
          album_id: Filter by assets in a specific album

          group_by: Time period to group counts by. Currently only 'month' is supported.

          library_id: Library to count assets in (optional)

          limit: Maximum number of time buckets to return (1-200)

          local_datetime_after: Only include assets with local_datetime after this value (ISO 8601). Naive
              values compare directly against local_datetime. Timezone-aware values: assets
              with a known offset are compared in UTC (local_datetime - offset); assets
              without an offset fall back to wall-clock comparison against local_datetime.

          local_datetime_before: Only include assets with local_datetime before this value (ISO 8601). Naive
              values compare directly against local_datetime. Timezone-aware values: assets
              with a known offset are compared in UTC (local_datetime - offset); assets
              without an offset fall back to wall-clock comparison against local_datetime. Use
              the last time_bucket from a previous response to paginate.

          person_id: Filter by assets associated with a specific person ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/assets/counts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "album_id": album_id,
                        "group_by": group_by,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "person_id": person_id,
                    },
                    asset_counts_params.AssetCountsParams,
                ),
            ),
            cast_to=AssetCountResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            assets.list,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )
        self.check_existence = to_raw_response_wrapper(
            assets.check_existence,
        )
        self.counts = to_raw_response_wrapper(
            assets.counts,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            assets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )
        self.check_existence = async_to_raw_response_wrapper(
            assets.check_existence,
        )
        self.counts = async_to_raw_response_wrapper(
            assets.counts,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )
        self.check_existence = to_streamed_response_wrapper(
            assets.check_existence,
        )
        self.counts = to_streamed_response_wrapper(
            assets.counts,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
        self.check_existence = async_to_streamed_response_wrapper(
            assets.check_existence,
        )
        self.counts = async_to_streamed_response_wrapper(
            assets.counts,
        )
