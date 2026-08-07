# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ..types import search_search_params, search_search_assets_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_response import SearchResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """
    Content-based search over a library's assets, with the same filters as asset listing.
    """

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        page: int | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches for assets by content, by typed structured filters on albums, people,
        date range, and location, or both. Content searches are ranked by relevance;
        filter-only searches return matches newest-first. Use this tool when the user
        describes _what's in_ the photos they want — subjects, scenes, places,
        activities, moods, objects — optionally narrowed by album, person, date, or
        location.

        Prefer typed filters for anything the request states exactly: `album_id` for
        album membership, `person_ids` for people,
        `local_datetime_before`/`local_datetime_after` for date ranges, and `center` +
        `radius` or `bbox` for location. There is no typed camera or place-name filter —
        pass those terms in the free-text `query`; the metadata full-text stage can
        match those terms, while dense retrieval adds visual-semantic matches. For
        example, 'photos of my kids at the beach last summer' becomes
        `query='kids at the beach'` + `local_datetime_after=2025-06-01` +
        `local_datetime_before=2025-09-01`.

        **Use `list_assets` instead** for a plain structured browse that album, person,
        date-range, location, or asset-ID filters can answer with no content `query` —
        it's cheaper and more deterministic than semantic search.

        **Location filtering is by coordinate,** in two mutually-exclusive modes: a
        radius (`center` + `radius`) or a bounding box (`bbox`).

        At least one of `query`, `album_id`, `person_ids`, `local_datetime_before`, or
        `local_datetime_after` must be provided; a location filter only narrows those
        results and is not a search criterion on its own.

        Args:
          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.

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

          library_id: Library to search. Optional if the user has a single live (non-trashed) library;
              required when they have multiple.

          limit: Maximum number of results per page (1–200). Defaults to 20.

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

          page: 1-indexed page number; increment it to fetch subsequent pages. `search_assets`
              pages by number rather than by cursor. A search with a content criterion ranks a
              fixed top-200 candidate population by relevance, so pages beyond that population
              are empty. A structured-filter-only search (album, people, date range — no
              content criterion) returns the full matching set newest-first, paginated without
              that cap.

          person_ids: Filter to assets containing ALL of these person IDs (intersection, not union).
              Accepts multiple `person_ids=` query params or a single comma-delimited value
              (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
              asset's `people` field (returned with `include=people`).

          query: Natural-language search text. It runs independently through dense visual
              retrieval and authoritative-metadata full-text retrieval, then the ranked lists
              are fused. Concrete visual concepts work well in the dense stage, while exact
              metadata terms can match through full-text search.

              Resolve album and people names to IDs and pass them as `album_id` and
              `person_ids`; convert date phrases like 'in 2023' into ISO 8601 bounds on
              `local_datetime_after`/`local_datetime_before` (here, `2023-01-01` and
              `2024-01-01`). None of those belong in `query`.

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50,000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "bbox": bbox,
                        "center": center,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "page": page,
                        "person_ids": person_ids,
                        "query": query,
                        "radius": radius,
                    },
                    search_search_params.SearchSearchParams,
                ),
            ),
            cast_to=SearchResponse,
        )

    def search_assets(
        self,
        *,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        image: Optional[FileTypes] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        page: int | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches for assets by content, by typed structured filters on albums, people,
        date range, and location, or both. Content searches are ranked by relevance;
        filter-only searches return matches newest-first. An uploaded `image` adds
        visual-similarity search; text and uploaded-image signals stay independent when
        both are provided.

        At least one search criterion must be provided. Location filtering is by
        coordinate in two mutually-exclusive modes: a radius (`center` + `radius`) or a
        bounding box (`bbox`); it narrows candidates and is not a search criterion on
        its own.

        Args:
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

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.

          image: Image file for an independent dense-image retrieval stage. When text is also
              provided, the stage ranks are fused rather than blending their embeddings.

          library_id: Library to search. Optional if the user has a single live (non-trashed) library;
              required when they have multiple.

          limit: Maximum number of results per page (1–200). Defaults to 20.

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

          page: 1-indexed page number; increment it to fetch subsequent pages. `search_assets`
              pages by number rather than by cursor. A search with a content criterion ranks a
              fixed top-200 candidate population by relevance, so pages beyond that population
              are empty. A structured-filter-only search (album, people, date range — no
              content criterion) returns the full matching set newest-first, paginated without
              that cap.

          person_ids: Filter to assets containing ALL of these person IDs (intersection, not union).
              Accepts multiple `person_ids=` form fields or a single comma-delimited value
              (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
              asset's `people` field (returned with `include=people`).

          query: Natural-language search text, matched against image embeddings and authoritative
              metadata. Album and people names belong in `album_id` and `person_ids`, and date
              ranges in `local_datetime_before`/`local_datetime_after`, not here.

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50,000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "album_id": album_id,
                "bbox": bbox,
                "center": center,
                "image": image,
                "library_id": library_id,
                "limit": limit,
                "local_datetime_after": local_datetime_after,
                "local_datetime_before": local_datetime_before,
                "page": page,
                "person_ids": person_ids,
                "query": query,
                "radius": radius,
            },
            [["image"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/search",
            body=maybe_transform(body, search_search_assets_params.SearchSearchAssetsParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, search_search_assets_params.SearchSearchAssetsParams),
            ),
            cast_to=SearchResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    """
    Content-based search over a library's assets, with the same filters as asset listing.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        page: int | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches for assets by content, by typed structured filters on albums, people,
        date range, and location, or both. Content searches are ranked by relevance;
        filter-only searches return matches newest-first. Use this tool when the user
        describes _what's in_ the photos they want — subjects, scenes, places,
        activities, moods, objects — optionally narrowed by album, person, date, or
        location.

        Prefer typed filters for anything the request states exactly: `album_id` for
        album membership, `person_ids` for people,
        `local_datetime_before`/`local_datetime_after` for date ranges, and `center` +
        `radius` or `bbox` for location. There is no typed camera or place-name filter —
        pass those terms in the free-text `query`; the metadata full-text stage can
        match those terms, while dense retrieval adds visual-semantic matches. For
        example, 'photos of my kids at the beach last summer' becomes
        `query='kids at the beach'` + `local_datetime_after=2025-06-01` +
        `local_datetime_before=2025-09-01`.

        **Use `list_assets` instead** for a plain structured browse that album, person,
        date-range, location, or asset-ID filters can answer with no content `query` —
        it's cheaper and more deterministic than semantic search.

        **Location filtering is by coordinate,** in two mutually-exclusive modes: a
        radius (`center` + `radius`) or a bounding box (`bbox`).

        At least one of `query`, `album_id`, `person_ids`, `local_datetime_before`, or
        `local_datetime_after` must be provided; a location filter only narrows those
        results and is not a search criterion on its own.

        Args:
          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.

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

          library_id: Library to search. Optional if the user has a single live (non-trashed) library;
              required when they have multiple.

          limit: Maximum number of results per page (1–200). Defaults to 20.

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

          page: 1-indexed page number; increment it to fetch subsequent pages. `search_assets`
              pages by number rather than by cursor. A search with a content criterion ranks a
              fixed top-200 candidate population by relevance, so pages beyond that population
              are empty. A structured-filter-only search (album, people, date range — no
              content criterion) returns the full matching set newest-first, paginated without
              that cap.

          person_ids: Filter to assets containing ALL of these person IDs (intersection, not union).
              Accepts multiple `person_ids=` query params or a single comma-delimited value
              (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
              asset's `people` field (returned with `include=people`).

          query: Natural-language search text. It runs independently through dense visual
              retrieval and authoritative-metadata full-text retrieval, then the ranked lists
              are fused. Concrete visual concepts work well in the dense stage, while exact
              metadata terms can match through full-text search.

              Resolve album and people names to IDs and pass them as `album_id` and
              `person_ids`; convert date phrases like 'in 2023' into ISO 8601 bounds on
              `local_datetime_after`/`local_datetime_before` (here, `2023-01-01` and
              `2024-01-01`). None of those belong in `query`.

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50,000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "album_id": album_id,
                        "bbox": bbox,
                        "center": center,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "local_datetime_after": local_datetime_after,
                        "local_datetime_before": local_datetime_before,
                        "page": page,
                        "person_ids": person_ids,
                        "query": query,
                        "radius": radius,
                    },
                    search_search_params.SearchSearchParams,
                ),
            ),
            cast_to=SearchResponse,
        )

    async def search_assets(
        self,
        *,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        album_id: Optional[str] | Omit = omit,
        bbox: Optional[str] | Omit = omit,
        center: Optional[str] | Omit = omit,
        image: Optional[FileTypes] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        local_datetime_after: Union[str, datetime, None] | Omit = omit,
        local_datetime_before: Union[str, datetime, None] | Omit = omit,
        page: int | Omit = omit,
        person_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        query: Optional[str] | Omit = omit,
        radius: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Searches for assets by content, by typed structured filters on albums, people,
        date range, and location, or both. Content searches are ranked by relevance;
        filter-only searches return matches newest-first. An uploaded `image` adds
        visual-similarity search; text and uploaded-image signals stay independent when
        both are provided.

        At least one search criterion must be provided. Location filtering is by
        coordinate in two mutually-exclusive modes: a radius (`center` + `radius`) or a
        bounding box (`bbox`); it narrows candidates and is not a search criterion on
        its own.

        Args:
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

          album_id: Return only assets in this album — the album's `album_` ID, not its name.

          bbox: Bounding-box (map viewport) location filter: four comma-separated decimal-degree
              numbers `min_longitude,min_latitude,max_longitude,max_latitude`
              (west,south,east,north), e.g. `-77.1,38.9,-77.0,39.0`. A box whose
              `min_longitude` exceeds `max_longitude` crosses the antimeridian: it selects the
              band running east from `min_longitude` over ±180° to `max_longitude`, so there
              is no need to split it client-side. Longitude order is therefore significant —
              transposed corners read as a crossing viewport, not as an error. A viewport 360°
              or wider must be sent as the full range `-180,...,180,...`, which the wrapped
              form cannot express.

          center: Center point of a radius location filter: two comma-separated decimal-degree
              numbers `longitude,latitude`, e.g. `-77.05,38.95`. Supply with `radius`.

          image: Image file for an independent dense-image retrieval stage. When text is also
              provided, the stage ranks are fused rather than blending their embeddings.

          library_id: Library to search. Optional if the user has a single live (non-trashed) library;
              required when they have multiple.

          limit: Maximum number of results per page (1–200). Defaults to 20.

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

          page: 1-indexed page number; increment it to fetch subsequent pages. `search_assets`
              pages by number rather than by cursor. A search with a content criterion ranks a
              fixed top-200 candidate population by relevance, so pages beyond that population
              are empty. A structured-filter-only search (album, people, date range — no
              content criterion) returns the full matching set newest-first, paginated without
              that cap.

          person_ids: Filter to assets containing ALL of these person IDs (intersection, not union).
              Accepts multiple `person_ids=` form fields or a single comma-delimited value
              (e.g., `person_123,person_abc`). Person IDs are carried by the entries of an
              asset's `people` field (returned with `include=people`).

          query: Natural-language search text, matched against image embeddings and authoritative
              metadata. Album and people names belong in `album_id` and `person_ids`, and date
              ranges in `local_datetime_before`/`local_datetime_after`, not here.

          radius: Radius of the `center` location filter, in meters (greater than 0, at most
              50,000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "album_id": album_id,
                "bbox": bbox,
                "center": center,
                "image": image,
                "library_id": library_id,
                "limit": limit,
                "local_datetime_after": local_datetime_after,
                "local_datetime_before": local_datetime_before,
                "page": page,
                "person_ids": person_ids,
                "query": query,
                "radius": radius,
            },
            [["image"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["image"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/search",
            body=await async_maybe_transform(body, search_search_assets_params.SearchSearchAssetsParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include}, search_search_assets_params.SearchSearchAssetsParams
                ),
            ),
            cast_to=SearchResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.search = to_raw_response_wrapper(
            search.search,
        )
        self.search_assets = to_raw_response_wrapper(
            search.search_assets,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.search = async_to_raw_response_wrapper(
            search.search,
        )
        self.search_assets = async_to_raw_response_wrapper(
            search.search_assets,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.search = to_streamed_response_wrapper(
            search.search,
        )
        self.search_assets = to_streamed_response_wrapper(
            search.search_assets,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.search = async_to_streamed_response_wrapper(
            search.search,
        )
        self.search_assets = async_to_streamed_response_wrapper(
            search.search_assets,
        )
