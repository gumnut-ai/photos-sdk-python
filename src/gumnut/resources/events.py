# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import event_get_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.events_response import EventsResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        entity_types: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventsResponse:
        """
        Returns a paginated stream of change events (create/update/delete) for entities
        in the library. Each event is a lightweight record — `entity_type`, `entity_id`,
        `event_type`, and timestamps — pointing at a concrete entity that has changed.
        Follow up with `get_asset`, `get_album`, `get_person`, or `get_face` to fetch
        full entity data when needed.

        **Use this tool** when the user wants to synchronise a local copy of their
        library, audit recent activity, or detect deletions. **Don't use it** for
        content queries — use `search_assets` or `list_assets` instead. Events cannot be
        filtered by content or asset metadata.

        **Pagination:** cursor-based via `after_cursor`. When `has_more` is true, pass
        the last event's `cursor` value into `after_cursor` to fetch the next page.

        **Recommended sync pattern:**

        1. Capture current time as `sync_end`.
        2. Fetch events with `created_at_lt=sync_end`.
        3. For subsequent pages, use
           `after_cursor={last.cursor}&created_at_lt=sync_end`.
        4. Continue until `has_more=false`.
        5. For each event, fetch the entity data from the appropriate endpoint if
           needed.
        6. Store `sync_end` as checkpoint for next sync.

        **Handling deletions:** when `event_type` ends with `_deleted` or `_removed`,
        the entity no longer exists — remove it from the local cache. Some deletion
        events include a `payload` field with context (e.g., `album_asset_removed`
        carries `album_id` and `asset_id` since the junction row is gone).

        **Event types:**

        - `asset_created`, `asset_updated`, `asset_deleted`
        - `album_created`, `album_updated`, `album_deleted`
        - `person_created`, `person_updated`, `person_deleted`
        - `face_created`, `face_updated`, `face_deleted`
        - `album_asset_added`, `album_asset_removed`
        - `exif_created`, `exif_updated`, `exif_deleted`

        Args:
          after_cursor: Opaque cursor from the last event of the previous page. Pass the `cursor` field
              from the last event to fetch the next page. Omit for the first page.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601). Set this to
              the previous sync's checkpoint when doing incremental sync.

          created_at_lt: Only return events created strictly before this timestamp (ISO 8601).
              Recommended for bounding a sync operation — capture `now` once and reuse it as
              `created_at_lt` across all pages so newly arriving events don't shift the
              window.

          entity_types: Comma-separated list of entity types to include (e.g., `asset,album`). Valid
              values: `asset`, `album`, `person`, `face`, `album_asset`, `exif`. Omit to
              receive events for all types.

          library_id: Library to stream events from. Optional if the user has a single library;
              required when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of events to return per page (1–200). Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "entity_types": entity_types,
                        "library_id": library_id,
                        "limit": limit,
                    },
                    event_get_params.EventGetParams,
                ),
            ),
            cast_to=EventsResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        entity_types: Optional[str] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventsResponse:
        """
        Returns a paginated stream of change events (create/update/delete) for entities
        in the library. Each event is a lightweight record — `entity_type`, `entity_id`,
        `event_type`, and timestamps — pointing at a concrete entity that has changed.
        Follow up with `get_asset`, `get_album`, `get_person`, or `get_face` to fetch
        full entity data when needed.

        **Use this tool** when the user wants to synchronise a local copy of their
        library, audit recent activity, or detect deletions. **Don't use it** for
        content queries — use `search_assets` or `list_assets` instead. Events cannot be
        filtered by content or asset metadata.

        **Pagination:** cursor-based via `after_cursor`. When `has_more` is true, pass
        the last event's `cursor` value into `after_cursor` to fetch the next page.

        **Recommended sync pattern:**

        1. Capture current time as `sync_end`.
        2. Fetch events with `created_at_lt=sync_end`.
        3. For subsequent pages, use
           `after_cursor={last.cursor}&created_at_lt=sync_end`.
        4. Continue until `has_more=false`.
        5. For each event, fetch the entity data from the appropriate endpoint if
           needed.
        6. Store `sync_end` as checkpoint for next sync.

        **Handling deletions:** when `event_type` ends with `_deleted` or `_removed`,
        the entity no longer exists — remove it from the local cache. Some deletion
        events include a `payload` field with context (e.g., `album_asset_removed`
        carries `album_id` and `asset_id` since the junction row is gone).

        **Event types:**

        - `asset_created`, `asset_updated`, `asset_deleted`
        - `album_created`, `album_updated`, `album_deleted`
        - `person_created`, `person_updated`, `person_deleted`
        - `face_created`, `face_updated`, `face_deleted`
        - `album_asset_added`, `album_asset_removed`
        - `exif_created`, `exif_updated`, `exif_deleted`

        Args:
          after_cursor: Opaque cursor from the last event of the previous page. Pass the `cursor` field
              from the last event to fetch the next page. Omit for the first page.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601). Set this to
              the previous sync's checkpoint when doing incremental sync.

          created_at_lt: Only return events created strictly before this timestamp (ISO 8601).
              Recommended for bounding a sync operation — capture `now` once and reuse it as
              `created_at_lt` across all pages so newly arriving events don't shift the
              window.

          entity_types: Comma-separated list of entity types to include (e.g., `asset,album`). Valid
              values: `asset`, `album`, `person`, `face`, `album_asset`, `exif`. Omit to
              receive events for all types.

          library_id: Library to stream events from. Optional if the user has a single library;
              required when they have multiple. Use `list_libraries` to enumerate.

          limit: Maximum number of events to return per page (1–200). Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "entity_types": entity_types,
                        "library_id": library_id,
                        "limit": limit,
                    },
                    event_get_params.EventGetParams,
                ),
            ),
            cast_to=EventsResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_raw_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_raw_response_wrapper(
            events.get,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_streamed_response_wrapper(
            events.get,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
