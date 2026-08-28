# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    asset_list_params,
    asset_trash_params,
    asset_counts_params,
    asset_create_params,
    asset_restore_params,
    asset_retrieve_params,
    asset_delete_list_params,
    asset_empty_trash_params,
    asset_update_asset_params,
    asset_cluster_by_geo_params,
    asset_check_existence_params,
    asset_bulk_update_assets_params,
)
from ..._files import deepcopy_with_paths
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
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
from ...types.asset_response import AssetResponse
from ...types.asset_count_response import AssetCountResponse
from ...types.asset_trash_response import AssetTrashResponse
from ...types.asset_delete_response import AssetDeleteResponse
from ...types.asset_restore_response import AssetRestoreResponse
from ...types.asset_existence_response import AssetExistenceResponse
from ...types.asset_delete_list_response import AssetDeleteListResponse
from ...types.asset_empty_trash_response import AssetEmptyTrashResponse
from ...types.asset_cluster_by_geo_response import AssetClusterByGeoResponse
from ...types.asset_bulk_update_assets_response import AssetBulkUpdateAssetsResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    """
    Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
    """

    @cached_property
    def versions(self) -> VersionsResource:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return VersionsResource(self._client)

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
        Uploads a new asset (image or video) and its metadata as multipart form data,
        returning the created asset with 201. Uploads are deduplicated per library by
        the file's SHA-256 checksum: re-uploading a file whose bytes already exist in
        the target library stores nothing and returns the existing asset with 200.
        Storage caps are checked before the duplicate lookup, so an upload is refused
        with 507 whenever the account or the target library is already at its storage
        cap — even when the bytes would have deduplicated to an existing asset. A
        transient upstream storage error returns 502 — retryable after the `Retry-After`
        interval. When `library_id` is omitted and no default library can be chosen (the
        account has multiple live libraries), the request is refused with 400. Image
        metadata is extracted before the response returns; the rest of processing
        (thumbnails, search indexing, face detection, and video metadata extraction)
        continues asynchronously after the response.

        Args:
          asset_data: The image or video file, sent as a binary multipart part with a filename. The
              file's MIME type is derived from the filename extension and must be an image or
              video type; files with an unrecognized or non-media extension are rejected
              with 422. The filename is stored as the asset's original file name (maximum 1024
              characters). The API imposes no fixed per-file size limit; uploads are
              constrained only by the storage caps.

          device_asset_id: Identifier of this asset on the uploading device, chosen by the client (for
              example, the device's local asset ID). Stored verbatim and usable for
              device-based existence checks; plays no part in upload-time duplicate detection.

          device_id: Identifier of the uploading device or client, chosen by the client. Paired with
              `device_asset_id` for device-based existence checks.

          file_created_at: When the file was created on the uploading device, as an ISO 8601 datetime. Also
              serves as the fallback for the asset's local capture time when the file's
              embedded metadata carries no usable timestamp.

          file_modified_at: When the file was last modified on the uploading device, as an ISO 8601
              datetime.

          library_id: Library to upload into. For an all-library credential, omit to use the account's
              sole live library or create a fresh default when there are no live libraries;
              pass explicitly when the account has multiple live libraries. For a
              selected-library credential, omit to use its sole selected library; pass
              explicitly when it selects multiple libraries.

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
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """Fetches one asset and its associated metadata by ID.

        Use this when you already
        have a specific asset ID (e.g., from `list_assets`, `search_assets`, or
        `list_album_assets`) and need its full details. For bulk fetch of multiple known
        IDs, prefer `list_assets` with the `ids` parameter to avoid N round trips.
        `asset_urls` are signed URLs for client rendering only; to visually inspect the
        image pixels, call `view_asset` instead.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to fetch.

          include: Opt-in expansion fields. Supported values: `metadata` (camera/EXIF/GPS and
              location names), `faces`, `people`, `metrics` (ML quality scores), `file_data`
              (a group token populating the nested `file_data` object with the file/provenance
              scalars `device_asset_id`, `device_id`, `file_created_at`, `file_modified_at`,
              `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (every
              `asset_urls` rung beyond the lean one. Without it `asset_urls` carries only its
              lean rung — `thumbnail` for an image, or `thumbnail_image` for a video — so
              callers that render non-thumbnail variants or download the current rendering
              must pass it). Accepts multiple `include=` query params or a single
              comma-delimited value (e.g. `include=faces,people`). Unknown values return 422.
              When omitted, only the lean core is returned (`id`, `mime_type`,
              `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`, `kind`,
              `current_version_id`) and each data field above is null/absent until you request
              it.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, asset_retrieve_params.AssetRetrieveParams),
            ),
            cast_to=AssetResponse,
        )

    def list(
        self,
        *,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        stack_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AssetResponse]:
        """
        Returns a paginated list of assets ordered by local capture time (or trash time
        for trashed assets), newest first by default, optionally filtered by album,
        person, rating, media type, date range, geographic area, or asset ID. Use this
        tool for structured browsing and filtering — when the request can be expressed
        as exact filters on album membership, people, rating, media type, date range,
        geographic coordinates, or specific asset IDs.

        **Location filtering is by coordinate:** pass a radius (`center` + `radius`) or
        a bounding box (`bbox`) to restrict results to a geographic area. The two modes
        are mutually exclusive. To count or cluster geotagged assets across a map
        viewport (how many photos fall in each area) rather than list them, use
        `get_geo_clusters`.

        Album and person filters compose using AND.

        **Use `search_assets` instead** when the request involves natural-language image
        content ('photos of sunsets', 'pictures with my dog'), a place _name_ ('photos
        from Japan'), or any concept requiring semantic understanding of what's in the
        image. `list_assets` filters by coordinate but not by image content, place name,
        or caption text.

        **To present a curated set of specific assets to the user** (e.g., a hand-picked
        subset of `search_assets` results), call this tool with `ids=[...]` rather than
        building a custom gallery — the asset IDs you already have are enough to
        re-render them through the interactive widget.

        **Pagination** is cursor-based: while `has_more` is true, keep fetching with
        `starting_after_id`.

        Args:
          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name. To
              browse one album's full asset metadata, prefer this filter over
              `list_album_assets`, which returns link records.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express. Mutually exclusive with `center`/`radius`.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.
              Mutually exclusive with `bbox`.

          ids: Look up specific assets by ID (max 200; each ID has the `asset_` prefix).
              Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=asset_1,asset_2`). Combines with other filters (album_id, person_ids,
              stack_id, media_type, ratings, datetime range) using AND logic — the result is
              the intersection.

          include: Opt-in expansion fields. Supported values: `metadata` (camera/EXIF/GPS and
              location names), `faces`, `people`, `metrics` (ML quality scores), `file_data`
              (a group token populating the nested `file_data` object with the file/provenance
              scalars `device_asset_id`, `device_id`, `file_created_at`, `file_modified_at`,
              `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (every
              `asset_urls` rung beyond the lean one. Without it `asset_urls` carries only its
              lean rung — `thumbnail` for an image, or `thumbnail_image` for a video — so
              callers that render non-thumbnail variants or download the current rendering
              must pass it). Accepts multiple `include=` query params or a single
              comma-delimited value (e.g. `include=faces,people`). Unknown values return 422.
              When omitted, only the lean core is returned (`id`, `mime_type`,
              `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`, `kind`,
              `current_version_id`) and each data field above is null/absent until you request
              it.

          library_id: Library to list assets from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          limit: Maximum number of assets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              Convert a relative or natural-language date phrase ('in 2023') into an explicit
              bound before sending. `local_datetime` is the photo's wall-clock time in the
              device's own timezone. Naive values compare directly against `local_datetime`.
              Timezone-aware values: assets with a known offset are compared in UTC
              (`local_datetime - offset`); assets without an offset fall back to wall-clock
              comparison against `local_datetime`.

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same conversion requirement and awareness/offset semantics as
              `local_datetime_after`.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          order: Sort direction for the selected state's timestamp: capture time for
              `live`/`all`, or trash time for `trashed`. The asset ID tie-breaker uses the
              same direction.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50000).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          stack_id: Return only assets belonging to this stack (the `asset_stack_` ID carried by the
              `stack_id` field on every asset).

          starting_after_id: Cursor for pagination. Pass the `id` of the last asset in the previous
              response's `data` to fetch the next page. Repeat the same filters, `state`, and
              `order` on every page. Omit for the first page. `list_assets` cursors because it
              walks a stable capture-time ordering; the sibling `search_assets` ranks by
              relevance and so pages by number instead.

          state: Which set of assets to read from: `live` (default — only assets that are not
              trashed), `trashed` (only trashed assets, ordered by trash time), or `all` (both
              live and trashed, ordered by capture time like `live`). Ordering defaults to
              newest or most recently trashed first.

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
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "bbox": bbox,
                        "center": center,
                        "ids": ids,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "order": order,
                        "person_ids": person_ids,
                        "radius": radius,
                        "ratings": ratings,
                        "stack_id": stack_id,
                        "starting_after_id": starting_after_id,
                        "state": state,
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
    ) -> AssetDeleteResponse:
        """
        Deletes the asset entirely — the database record, the stored file, and all
        associated data (faces, album links, etc.). **Irreversible.** Prefer
        `trash_assets` for the user's standard delete action so accidents can be
        recovered.

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
        return self._delete(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDeleteResponse,
        )

    def bulk_update_assets(
        self,
        *,
        updates: Iterable[asset_bulk_update_assets_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetBulkUpdateAssetsResponse:
        """Updates metadata on multiple assets in one transactional call.

        Each item carries
        the target asset id and the per-asset change — different fields can be changed
        on different assets in the same request. Atomic: any per-item validation failure
        or unknown / cross-user id rejects the whole batch and writes nothing.

        For a single-asset edit, prefer `update_asset` — semantically identical but
        slightly more concise at the call site.

        Args:
          updates: List of per-asset updates. Each item carries the target asset id and the change
              to apply to it; different fields can be changed on different assets in the same
              request. Up to 200 items per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/assets/bulk-update",
            body=maybe_transform({"updates": updates}, asset_bulk_update_assets_params.AssetBulkUpdateAssetsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetBulkUpdateAssetsResponse,
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
          library_id: Library to check assets in. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          checksum_sha1s: List of base64-encoded SHA-1 checksums to check for existence

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

    def cluster_by_geo(
        self,
        *,
        bbox: str,
        cell_size: float,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetClusterByGeoResponse:
        """
        Clusters geotagged assets in a map viewport (bounding box) onto a grid of square
        cells and returns one entry per non-empty cell — its centroid, asset count, and
        a representative cover asset. Use this to render a clustered map or to count how
        many photos fall in each part of a viewport at a chosen zoom granularity.

        The result is a single un-paginated list capped at 1000 cells; a viewport that
        is too dense at the given `cell_size` returns 422 (coarsen `cell_size` or zoom
        in). To list the individual assets behind a cell, call `list_assets` with a
        tighter bounding box over the same filters. Album and person filters compose
        using AND. Rating and media type can further restrict the cluster.

        Args:
          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          cell_size: Grid cell edge in decimal degrees — the clustering granularity. Larger values
              give coarser clusters; the client maps map-zoom to `cell_size`. Must be at least
              0.0001 (~11 m).

          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          library_id: Library to cluster assets from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              Convert a relative or natural-language date phrase ('in 2023') into an explicit
              bound before sending. `local_datetime` is the photo's wall-clock time in the
              device's own timezone. Naive values compare directly against `local_datetime`.
              Timezone-aware values: assets with a known offset are compared in UTC
              (`local_datetime - offset`); assets without an offset fall back to wall-clock
              comparison against `local_datetime`.

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same conversion requirement and awareness/offset semantics as
              `local_datetime_after`.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          state: Which set of assets to cluster: `live` (default — excludes trashed assets),
              `trashed` (only trashed assets), or `all` (both).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/assets/geo-clusters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "cell_size": cell_size,
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "library_id": library_id,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "person_ids": person_ids,
                        "ratings": ratings,
                        "state": state,
                    },
                    asset_cluster_by_geo_params.AssetClusterByGeoParams,
                ),
            ),
            cast_to=AssetClusterByGeoResponse,
        )

    def counts(
        self,
        *,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        group_by: Literal["day", "week", "month", "year"] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        starting_after_bucket: Union[str, datetime, None] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCountResponse:
        """
        Counts assets bucketed by time period — use this to summarize a library (or a
        filtered slice) without paging through the full timeline. Returns one row per
        bucket, newest-first by default or oldest-first when `order=asc`, with optional
        filtering by album, album membership, people, rating, media type, date range, or
        trash state.

        To list the actual assets within a bucket, call `list_assets` with the same
        filters and a `local_datetime_after` / `local_datetime_before` window matching
        the bucket. Does not filter by image content or location; for content-based
        search use `search_assets`.

        **Pagination:** When `has_more` is true, pass the last `time_bucket` from `data`
        as `starting_after_bucket`. Repeat the same `group_by`, `order`, date bounds,
        and non-date filters. Count bounds, the cursor, and returned bucket starts are
        timezone-naive local-calendar values.

        Args:
          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          group_by: Calendar period to use for each count bucket.

          library_id: Library to count assets in. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          limit: Maximum number of time buckets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this local wall-clock datetime (ISO
              8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
              or timezone offset returns 422. Repeat this bound unchanged on every pagination
              page.

          local_datetime_before: Only include assets captured strictly before this local wall-clock datetime (ISO
              8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
              or timezone offset returns 422. Repeat this bound unchanged on every pagination
              page.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          order: Sort direction for capture-date buckets: `desc` returns newest buckets first;
              `asc` returns oldest buckets first.

          person_id: Deprecated compatibility alias for one `person_ids` value. Do not combine it
              with `person_ids`.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          starting_after_bucket: Cursor for time-bucket pagination. Pass the last returned `time_bucket`
              unchanged; buckets after it in the requested `order` are returned. Omit for the
              first page.

          state: Which set of assets to count: `live` (default — excludes trashed assets),
              `trashed` (only trashed assets), or `all` (both live and trashed).

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
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "group_by": group_by,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "order": order,
                        "person_id": person_id,
                        "person_ids": person_ids,
                        "ratings": ratings,
                        "starting_after_bucket": starting_after_bucket,
                        "state": state,
                    },
                    asset_counts_params.AssetCountsParams,
                ),
            ),
            cast_to=AssetCountResponse,
        )

    def delete_list(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetDeleteListResponse:
        """
        Hard-deletes each specified asset — the database record, the stored file, and
        all associated data (faces, album links, etc.). **Irreversible.** Prefer
        `trash_assets` for the user's standard delete action so accidents can be
        recovered.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/assets",
            body=maybe_transform({"ids": ids}, asset_delete_list_params.AssetDeleteListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, asset_delete_list_params.AssetDeleteListParams),
            ),
            cast_to=AssetDeleteListResponse,
        )

    def empty_trash(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetEmptyTrashResponse:
        """
        Permanently deletes every trashed asset and its associated stored data from the
        caller's library. **Irreversible**.

        Args:
          library_id: Library whose trashed assets to permanently delete. Optional if the user has a
              single live (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/assets/empty-trash",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, asset_empty_trash_params.AssetEmptyTrashParams),
            ),
            cast_to=AssetEmptyTrashResponse,
        )

    def restore(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetRestoreResponse:
        """
        Restores trashed assets so they reappear in default list/search results.
        Idempotent — assets that are already live are silently skipped.

        Pairs with `trash_assets`: assets soft-deleted there can be brought back here
        within the retention window. To restore a whole trashed library, use
        `restore_library`.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/assets/restore",
            body=maybe_transform({"ids": ids}, asset_restore_params.AssetRestoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, asset_restore_params.AssetRestoreParams),
            ),
            cast_to=AssetRestoreResponse,
        )

    def trash(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetTrashResponse:
        """Soft-deletes the given assets.

        Trashed assets are excluded from default
        list/search results and are purged after the configured retention window.
        **Reversible** via `restore_assets` until purge.

        To trash an entire library at once instead of enumerating asset IDs, use
        `trash_library`.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/assets/trash",
            body=maybe_transform({"ids": ids}, asset_trash_params.AssetTrashParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, asset_trash_params.AssetTrashParams),
            ),
            cast_to=AssetTrashResponse,
        )

    def update_asset(
        self,
        asset_id: str,
        *,
        description: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        original_datetime: Union[str, datetime, None] | Omit = omit,
        rating: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Edits the user-editable metadata for a single asset — description, rating, GPS
        coordinates, and original capture datetime. Rating accepts 0-5, where 0
        explicitly marks the asset unrated; passing null clears the USER override. Only
        fields included in the request body are changed; others are left untouched.
        Passing `null` for a field removes a previously-set value; the effective
        response may still contain a value from another metadata source. `latitude` and
        `longitude` must be set together (both written or both cleared).

        Setting or clearing GPS coordinates schedules an asynchronous refresh of derived
        location names.

        For editing multiple assets in one round trip, prefer `bulk_update_assets`.

        Args:
          asset_id: Asset ID (with `asset_` prefix) of the asset to update.

          description: User-set description for the asset. Pass `null` to remove a previously-set
              value; the effective response may still contain a description from another
              metadata source. Omit to leave unchanged. Distinct from the AI-generated
              `description` field on the response — this writes to `metadata.description`.

          latitude: GPS latitude in decimal degrees, `[-90, 90]`. Must be set together with
              `longitude`. Pass `null` (along with `longitude=null`) to remove a
              previously-set value; omit to leave unchanged.

          longitude: GPS longitude in decimal degrees, `[-180, 180]`. Must be set together with
              `latitude`. Pass `null` (along with `latitude=null`) to remove a previously-set
              value; omit to leave unchanged.

          original_datetime: When the asset was originally captured. Timezone-aware values preserve their UTC
              offset; timezone-naive values have no offset. Pass `null` to remove a
              previously-set value; the effective response may still contain a datetime from
              another metadata source. Omit to leave unchanged.

          rating: Star rating, `0`-`5`. `5` is the value a favorite carries. `0` explicitly marks
              the asset unrated, masking any rating embedded in the file. Pass `null` to
              remove a previously-set value and let the file's embedded rating (if any) show
              through; omit to leave unchanged. Values outside `0`-`5` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._patch(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            body=maybe_transform(
                {
                    "description": description,
                    "latitude": latitude,
                    "longitude": longitude,
                    "original_datetime": original_datetime,
                    "rating": rating,
                },
                asset_update_asset_params.AssetUpdateAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    """
    Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
    """

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return AsyncVersionsResource(self._client)

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
        Uploads a new asset (image or video) and its metadata as multipart form data,
        returning the created asset with 201. Uploads are deduplicated per library by
        the file's SHA-256 checksum: re-uploading a file whose bytes already exist in
        the target library stores nothing and returns the existing asset with 200.
        Storage caps are checked before the duplicate lookup, so an upload is refused
        with 507 whenever the account or the target library is already at its storage
        cap — even when the bytes would have deduplicated to an existing asset. A
        transient upstream storage error returns 502 — retryable after the `Retry-After`
        interval. When `library_id` is omitted and no default library can be chosen (the
        account has multiple live libraries), the request is refused with 400. Image
        metadata is extracted before the response returns; the rest of processing
        (thumbnails, search indexing, face detection, and video metadata extraction)
        continues asynchronously after the response.

        Args:
          asset_data: The image or video file, sent as a binary multipart part with a filename. The
              file's MIME type is derived from the filename extension and must be an image or
              video type; files with an unrecognized or non-media extension are rejected
              with 422. The filename is stored as the asset's original file name (maximum 1024
              characters). The API imposes no fixed per-file size limit; uploads are
              constrained only by the storage caps.

          device_asset_id: Identifier of this asset on the uploading device, chosen by the client (for
              example, the device's local asset ID). Stored verbatim and usable for
              device-based existence checks; plays no part in upload-time duplicate detection.

          device_id: Identifier of the uploading device or client, chosen by the client. Paired with
              `device_asset_id` for device-based existence checks.

          file_created_at: When the file was created on the uploading device, as an ISO 8601 datetime. Also
              serves as the fallback for the asset's local capture time when the file's
              embedded metadata carries no usable timestamp.

          file_modified_at: When the file was last modified on the uploading device, as an ISO 8601
              datetime.

          library_id: Library to upload into. For an all-library credential, omit to use the account's
              sole live library or create a fresh default when there are no live libraries;
              pass explicitly when the account has multiple live libraries. For a
              selected-library credential, omit to use its sole selected library; pass
              explicitly when it selects multiple libraries.

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
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """Fetches one asset and its associated metadata by ID.

        Use this when you already
        have a specific asset ID (e.g., from `list_assets`, `search_assets`, or
        `list_album_assets`) and need its full details. For bulk fetch of multiple known
        IDs, prefer `list_assets` with the `ids` parameter to avoid N round trips.
        `asset_urls` are signed URLs for client rendering only; to visually inspect the
        image pixels, call `view_asset` instead.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to fetch.

          include: Opt-in expansion fields. Supported values: `metadata` (camera/EXIF/GPS and
              location names), `faces`, `people`, `metrics` (ML quality scores), `file_data`
              (a group token populating the nested `file_data` object with the file/provenance
              scalars `device_asset_id`, `device_id`, `file_created_at`, `file_modified_at`,
              `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (every
              `asset_urls` rung beyond the lean one. Without it `asset_urls` carries only its
              lean rung — `thumbnail` for an image, or `thumbnail_image` for a video — so
              callers that render non-thumbnail variants or download the current rendering
              must pass it). Accepts multiple `include=` query params or a single
              comma-delimited value (e.g. `include=faces,people`). Unknown values return 422.
              When omitted, only the lean core is returned (`id`, `mime_type`,
              `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`, `kind`,
              `current_version_id`) and each data field above is null/absent until you request
              it.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, asset_retrieve_params.AssetRetrieveParams),
            ),
            cast_to=AssetResponse,
        )

    def list(
        self,
        *,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        stack_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetResponse, AsyncCursorPage[AssetResponse]]:
        """
        Returns a paginated list of assets ordered by local capture time (or trash time
        for trashed assets), newest first by default, optionally filtered by album,
        person, rating, media type, date range, geographic area, or asset ID. Use this
        tool for structured browsing and filtering — when the request can be expressed
        as exact filters on album membership, people, rating, media type, date range,
        geographic coordinates, or specific asset IDs.

        **Location filtering is by coordinate:** pass a radius (`center` + `radius`) or
        a bounding box (`bbox`) to restrict results to a geographic area. The two modes
        are mutually exclusive. To count or cluster geotagged assets across a map
        viewport (how many photos fall in each area) rather than list them, use
        `get_geo_clusters`.

        Album and person filters compose using AND.

        **Use `search_assets` instead** when the request involves natural-language image
        content ('photos of sunsets', 'pictures with my dog'), a place _name_ ('photos
        from Japan'), or any concept requiring semantic understanding of what's in the
        image. `list_assets` filters by coordinate but not by image content, place name,
        or caption text.

        **To present a curated set of specific assets to the user** (e.g., a hand-picked
        subset of `search_assets` results), call this tool with `ids=[...]` rather than
        building a custom gallery — the asset IDs you already have are enough to
        re-render them through the interactive widget.

        **Pagination** is cursor-based: while `has_more` is true, keep fetching with
        `starting_after_id`.

        Args:
          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name. To
              browse one album's full asset metadata, prefer this filter over
              `list_album_assets`, which returns link records.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express. Mutually exclusive with `center`/`radius`.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.
              Mutually exclusive with `bbox`.

          ids: Look up specific assets by ID (max 200; each ID has the `asset_` prefix).
              Accepts multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=asset_1,asset_2`). Combines with other filters (album_id, person_ids,
              stack_id, media_type, ratings, datetime range) using AND logic — the result is
              the intersection.

          include: Opt-in expansion fields. Supported values: `metadata` (camera/EXIF/GPS and
              location names), `faces`, `people`, `metrics` (ML quality scores), `file_data`
              (a group token populating the nested `file_data` object with the file/provenance
              scalars `device_asset_id`, `device_id`, `file_created_at`, `file_modified_at`,
              `checksum`, `checksum_sha1`, `file_size_bytes`), and `variants` (every
              `asset_urls` rung beyond the lean one. Without it `asset_urls` carries only its
              lean rung — `thumbnail` for an image, or `thumbnail_image` for a video — so
              callers that render non-thumbnail variants or download the current rendering
              must pass it). Accepts multiple `include=` query params or a single
              comma-delimited value (e.g. `include=faces,people`). Unknown values return 422.
              When omitted, only the lean core is returned (`id`, `mime_type`,
              `local_datetime`, dimensions, `description`, `thumbhash`, `asset_urls`, `kind`,
              `current_version_id`) and each data field above is null/absent until you request
              it.

          library_id: Library to list assets from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          limit: Maximum number of assets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              Convert a relative or natural-language date phrase ('in 2023') into an explicit
              bound before sending. `local_datetime` is the photo's wall-clock time in the
              device's own timezone. Naive values compare directly against `local_datetime`.
              Timezone-aware values: assets with a known offset are compared in UTC
              (`local_datetime - offset`); assets without an offset fall back to wall-clock
              comparison against `local_datetime`.

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same conversion requirement and awareness/offset semantics as
              `local_datetime_after`.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          order: Sort direction for the selected state's timestamp: capture time for
              `live`/`all`, or trash time for `trashed`. The asset ID tie-breaker uses the
              same direction.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50000).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          stack_id: Return only assets belonging to this stack (the `asset_stack_` ID carried by the
              `stack_id` field on every asset).

          starting_after_id: Cursor for pagination. Pass the `id` of the last asset in the previous
              response's `data` to fetch the next page. Repeat the same filters, `state`, and
              `order` on every page. Omit for the first page. `list_assets` cursors because it
              walks a stable capture-time ordering; the sibling `search_assets` ranks by
              relevance and so pages by number instead.

          state: Which set of assets to read from: `live` (default — only assets that are not
              trashed), `trashed` (only trashed assets, ordered by trash time), or `all` (both
              live and trashed, ordered by capture time like `live`). Ordering defaults to
              newest or most recently trashed first.

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
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "bbox": bbox,
                        "center": center,
                        "ids": ids,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "order": order,
                        "person_ids": person_ids,
                        "radius": radius,
                        "ratings": ratings,
                        "stack_id": stack_id,
                        "starting_after_id": starting_after_id,
                        "state": state,
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
    ) -> AssetDeleteResponse:
        """
        Deletes the asset entirely — the database record, the stored file, and all
        associated data (faces, album links, etc.). **Irreversible.** Prefer
        `trash_assets` for the user's standard delete action so accidents can be
        recovered.

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
        return await self._delete(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDeleteResponse,
        )

    async def bulk_update_assets(
        self,
        *,
        updates: Iterable[asset_bulk_update_assets_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetBulkUpdateAssetsResponse:
        """Updates metadata on multiple assets in one transactional call.

        Each item carries
        the target asset id and the per-asset change — different fields can be changed
        on different assets in the same request. Atomic: any per-item validation failure
        or unknown / cross-user id rejects the whole batch and writes nothing.

        For a single-asset edit, prefer `update_asset` — semantically identical but
        slightly more concise at the call site.

        Args:
          updates: List of per-asset updates. Each item carries the target asset id and the change
              to apply to it; different fields can be changed on different assets in the same
              request. Up to 200 items per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/assets/bulk-update",
            body=await async_maybe_transform(
                {"updates": updates}, asset_bulk_update_assets_params.AssetBulkUpdateAssetsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetBulkUpdateAssetsResponse,
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
          library_id: Library to check assets in. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          checksum_sha1s: List of base64-encoded SHA-1 checksums to check for existence

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

    async def cluster_by_geo(
        self,
        *,
        bbox: str,
        cell_size: float,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetClusterByGeoResponse:
        """
        Clusters geotagged assets in a map viewport (bounding box) onto a grid of square
        cells and returns one entry per non-empty cell — its centroid, asset count, and
        a representative cover asset. Use this to render a clustered map or to count how
        many photos fall in each part of a viewport at a chosen zoom granularity.

        The result is a single un-paginated list capped at 1000 cells; a viewport that
        is too dense at the given `cell_size` returns 422 (coarsen `cell_size` or zoom
        in). To list the individual assets behind a cell, call `list_assets` with a
        tighter bounding box over the same filters. Album and person filters compose
        using AND. Rating and media type can further restrict the cluster.

        Args:
          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          cell_size: Grid cell edge in decimal degrees — the clustering granularity. Larger values
              give coarser clusters; the client maps map-zoom to `cell_size`. Must be at least
              0.0001 (~11 m).

          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          library_id: Library to cluster assets from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          local_datetime_after: Only include assets captured strictly after this instant (ISO 8601; exclusive).
              Convert a relative or natural-language date phrase ('in 2023') into an explicit
              bound before sending. `local_datetime` is the photo's wall-clock time in the
              device's own timezone. Naive values compare directly against `local_datetime`.
              Timezone-aware values: assets with a known offset are compared in UTC
              (`local_datetime - offset`); assets without an offset fall back to wall-clock
              comparison against `local_datetime`.

          local_datetime_before: Only include assets captured strictly before this instant (ISO 8601; exclusive).
              Same conversion requirement and awareness/offset semantics as
              `local_datetime_after`.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          state: Which set of assets to cluster: `live` (default — excludes trashed assets),
              `trashed` (only trashed assets), or `all` (both).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/assets/geo-clusters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "cell_size": cell_size,
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "library_id": library_id,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "person_ids": person_ids,
                        "ratings": ratings,
                        "state": state,
                    },
                    asset_cluster_by_geo_params.AssetClusterByGeoParams,
                ),
            ),
            cast_to=AssetClusterByGeoResponse,
        )

    async def counts(
        self,
        *,
        album_filter: Literal["all", "in_album", "not_in_album"] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        group_by: Literal["day", "week", "month", "year"] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        media_type: Optional[Literal["image", "video"]] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        ratings: Optional[Iterable[int]] | Omit = omit,
        starting_after_bucket: Union[str, datetime, None] | Omit = omit,
        state: Literal["live", "trashed", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCountResponse:
        """
        Counts assets bucketed by time period — use this to summarize a library (or a
        filtered slice) without paging through the full timeline. Returns one row per
        bucket, newest-first by default or oldest-first when `order=asc`, with optional
        filtering by album, album membership, people, rating, media type, date range, or
        trash state.

        To list the actual assets within a bucket, call `list_assets` with the same
        filters and a `local_datetime_after` / `local_datetime_before` window matching
        the bucket. Does not filter by image content or location; for content-based
        search use `search_assets`.

        **Pagination:** When `has_more` is true, pass the last `time_bucket` from `data`
        as `starting_after_bucket`. Repeat the same `group_by`, `order`, date bounds,
        and non-date filters. Count bounds, the cursor, and returned bucket starts are
        timezone-naive local-calendar values.

        Args:
          album_filter: Filter by album membership in general, rather than by membership of one specific
              album. This filter is independent of `album_id`, but combining `not_in_album`
              with `album_id` is contradictory and returns 422. Defaults to `all`.

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          group_by: Calendar period to use for each count bucket.

          library_id: Library to count assets in. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          limit: Maximum number of time buckets to return per page (1–200). Defaults to 20.

          local_datetime_after: Only include assets captured strictly after this local wall-clock datetime (ISO
              8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
              or timezone offset returns 422. Repeat this bound unchanged on every pagination
              page.

          local_datetime_before: Only include assets captured strictly before this local wall-clock datetime (ISO
              8601; exclusive). Asset counts accept timezone-naive values only; a `Z` suffix
              or timezone offset returns 422. Repeat this bound unchanged on every pagination
              page.

          media_type: Filter to one media class (`image` or `video`). Omit to include both images and
              videos.

          order: Sort direction for capture-date buckets: `desc` returns newest buckets first;
              `asc` returns oldest buckets first.

          person_id: Deprecated compatibility alias for one `person_ids` value. Do not combine it
              with `person_ids`.

          person_ids: Filter to assets containing faces belonging to ALL of these people
              (intersection, not union). Accepts up to 200 IDs across repeated `person_ids=`
              query params or comma-delimited values. Person IDs are carried by the entries of
              an asset's `people` field (returned with `include=people`).

          ratings: Return assets whose effective rating is one of these exact values. Values must
              be integers from `0` through `5`; `5` is a favorite. `0` matches every unrated
              form: an explicit zero, a null or legacy out-of-range effective rating, or an
              asset with no metadata. Accepts repeated `ratings=` parameters or one
              comma-delimited value. Omit the parameter for no rating filter.

          starting_after_bucket: Cursor for time-bucket pagination. Pass the last returned `time_bucket`
              unchanged; buckets after it in the requested `order` are returned. Omit for the
              first page.

          state: Which set of assets to count: `live` (default — excludes trashed assets),
              `trashed` (only trashed assets), or `all` (both live and trashed).

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
                        "album_filter": album_filter,
                        "album_id": album_id,
                        "group_by": group_by,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "media_type": media_type,
                        "order": order,
                        "person_id": person_id,
                        "person_ids": person_ids,
                        "ratings": ratings,
                        "starting_after_bucket": starting_after_bucket,
                        "state": state,
                    },
                    asset_counts_params.AssetCountsParams,
                ),
            ),
            cast_to=AssetCountResponse,
        )

    async def delete_list(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetDeleteListResponse:
        """
        Hard-deletes each specified asset — the database record, the stored file, and
        all associated data (faces, album links, etc.). **Irreversible.** Prefer
        `trash_assets` for the user's standard delete action so accidents can be
        recovered.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/assets",
            body=await async_maybe_transform({"ids": ids}, asset_delete_list_params.AssetDeleteListParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"library_id": library_id}, asset_delete_list_params.AssetDeleteListParams
                ),
            ),
            cast_to=AssetDeleteListResponse,
        )

    async def empty_trash(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetEmptyTrashResponse:
        """
        Permanently deletes every trashed asset and its associated stored data from the
        caller's library. **Irreversible**.

        Args:
          library_id: Library whose trashed assets to permanently delete. Optional if the user has a
              single live (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/assets/empty-trash",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"library_id": library_id}, asset_empty_trash_params.AssetEmptyTrashParams
                ),
            ),
            cast_to=AssetEmptyTrashResponse,
        )

    async def restore(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetRestoreResponse:
        """
        Restores trashed assets so they reappear in default list/search results.
        Idempotent — assets that are already live are silently skipped.

        Pairs with `trash_assets`: assets soft-deleted there can be brought back here
        within the retention window. To restore a whole trashed library, use
        `restore_library`.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/assets/restore",
            body=await async_maybe_transform({"ids": ids}, asset_restore_params.AssetRestoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, asset_restore_params.AssetRestoreParams),
            ),
            cast_to=AssetRestoreResponse,
        )

    async def trash(
        self,
        *,
        ids: SequenceNotStr[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetTrashResponse:
        """Soft-deletes the given assets.

        Trashed assets are excluded from default
        list/search results and are purged after the configured retention window.
        **Reversible** via `restore_assets` until purge.

        To trash an entire library at once instead of enumerating asset IDs, use
        `trash_library`.

        Args:
          ids: Asset IDs (each with the `asset_` prefix) to operate on. Up to 200 ids per
              request.

          library_id: Library that owns the assets. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/assets/trash",
            body=await async_maybe_transform({"ids": ids}, asset_trash_params.AssetTrashParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, asset_trash_params.AssetTrashParams),
            ),
            cast_to=AssetTrashResponse,
        )

    async def update_asset(
        self,
        asset_id: str,
        *,
        description: Optional[str] | Omit = omit,
        latitude: Optional[float] | Omit = omit,
        longitude: Optional[float] | Omit = omit,
        original_datetime: Union[str, datetime, None] | Omit = omit,
        rating: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Edits the user-editable metadata for a single asset — description, rating, GPS
        coordinates, and original capture datetime. Rating accepts 0-5, where 0
        explicitly marks the asset unrated; passing null clears the USER override. Only
        fields included in the request body are changed; others are left untouched.
        Passing `null` for a field removes a previously-set value; the effective
        response may still contain a value from another metadata source. `latitude` and
        `longitude` must be set together (both written or both cleared).

        Setting or clearing GPS coordinates schedules an asynchronous refresh of derived
        location names.

        For editing multiple assets in one round trip, prefer `bulk_update_assets`.

        Args:
          asset_id: Asset ID (with `asset_` prefix) of the asset to update.

          description: User-set description for the asset. Pass `null` to remove a previously-set
              value; the effective response may still contain a description from another
              metadata source. Omit to leave unchanged. Distinct from the AI-generated
              `description` field on the response — this writes to `metadata.description`.

          latitude: GPS latitude in decimal degrees, `[-90, 90]`. Must be set together with
              `longitude`. Pass `null` (along with `longitude=null`) to remove a
              previously-set value; omit to leave unchanged.

          longitude: GPS longitude in decimal degrees, `[-180, 180]`. Must be set together with
              `latitude`. Pass `null` (along with `latitude=null`) to remove a previously-set
              value; omit to leave unchanged.

          original_datetime: When the asset was originally captured. Timezone-aware values preserve their UTC
              offset; timezone-naive values have no offset. Pass `null` to remove a
              previously-set value; the effective response may still contain a datetime from
              another metadata source. Omit to leave unchanged.

          rating: Star rating, `0`-`5`. `5` is the value a favorite carries. `0` explicitly marks
              the asset unrated, masking any rating embedded in the file. Pass `null` to
              remove a previously-set value and let the file's embedded rating (if any) show
              through; omit to leave unchanged. Values outside `0`-`5` are rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._patch(
            path_template("/api/assets/{asset_id}", asset_id=asset_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "latitude": latitude,
                    "longitude": longitude,
                    "original_datetime": original_datetime,
                    "rating": rating,
                },
                asset_update_asset_params.AssetUpdateAssetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
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
        self.bulk_update_assets = to_raw_response_wrapper(
            assets.bulk_update_assets,
        )
        self.check_existence = to_raw_response_wrapper(
            assets.check_existence,
        )
        self.cluster_by_geo = to_raw_response_wrapper(
            assets.cluster_by_geo,
        )
        self.counts = to_raw_response_wrapper(
            assets.counts,
        )
        self.delete_list = to_raw_response_wrapper(
            assets.delete_list,
        )
        self.empty_trash = to_raw_response_wrapper(
            assets.empty_trash,
        )
        self.restore = to_raw_response_wrapper(
            assets.restore,
        )
        self.trash = to_raw_response_wrapper(
            assets.trash,
        )
        self.update_asset = to_raw_response_wrapper(
            assets.update_asset,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return VersionsResourceWithRawResponse(self._assets.versions)


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
        self.bulk_update_assets = async_to_raw_response_wrapper(
            assets.bulk_update_assets,
        )
        self.check_existence = async_to_raw_response_wrapper(
            assets.check_existence,
        )
        self.cluster_by_geo = async_to_raw_response_wrapper(
            assets.cluster_by_geo,
        )
        self.counts = async_to_raw_response_wrapper(
            assets.counts,
        )
        self.delete_list = async_to_raw_response_wrapper(
            assets.delete_list,
        )
        self.empty_trash = async_to_raw_response_wrapper(
            assets.empty_trash,
        )
        self.restore = async_to_raw_response_wrapper(
            assets.restore,
        )
        self.trash = async_to_raw_response_wrapper(
            assets.trash,
        )
        self.update_asset = async_to_raw_response_wrapper(
            assets.update_asset,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return AsyncVersionsResourceWithRawResponse(self._assets.versions)


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
        self.bulk_update_assets = to_streamed_response_wrapper(
            assets.bulk_update_assets,
        )
        self.check_existence = to_streamed_response_wrapper(
            assets.check_existence,
        )
        self.cluster_by_geo = to_streamed_response_wrapper(
            assets.cluster_by_geo,
        )
        self.counts = to_streamed_response_wrapper(
            assets.counts,
        )
        self.delete_list = to_streamed_response_wrapper(
            assets.delete_list,
        )
        self.empty_trash = to_streamed_response_wrapper(
            assets.empty_trash,
        )
        self.restore = to_streamed_response_wrapper(
            assets.restore,
        )
        self.trash = to_streamed_response_wrapper(
            assets.trash,
        )
        self.update_asset = to_streamed_response_wrapper(
            assets.update_asset,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return VersionsResourceWithStreamingResponse(self._assets.versions)


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
        self.bulk_update_assets = async_to_streamed_response_wrapper(
            assets.bulk_update_assets,
        )
        self.check_existence = async_to_streamed_response_wrapper(
            assets.check_existence,
        )
        self.cluster_by_geo = async_to_streamed_response_wrapper(
            assets.cluster_by_geo,
        )
        self.counts = async_to_streamed_response_wrapper(
            assets.counts,
        )
        self.delete_list = async_to_streamed_response_wrapper(
            assets.delete_list,
        )
        self.empty_trash = async_to_streamed_response_wrapper(
            assets.empty_trash,
        )
        self.restore = async_to_streamed_response_wrapper(
            assets.restore,
        )
        self.trash = async_to_streamed_response_wrapper(
            assets.trash,
        )
        self.update_asset = async_to_streamed_response_wrapper(
            assets.update_asset,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
        """
        return AsyncVersionsResourceWithStreamingResponse(self._assets.versions)
