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
        Retrieves a list of entity change events for syncing.

        Events are lightweight records indicating that entities have changed. Each event
        contains the entity type, entity ID, and event type (e.g., "asset_created",
        "album_deleted"). Clients should fetch full entity data from the appropriate
        endpoints if needed.

        **Pagination:** Use the `after_cursor` parameter with the `cursor` value from
        the last event to fetch the next page. The `has_more` field indicates if more
        events exist.

        **Recommended sync pattern:**

        1. Capture current time as `sync_end`
        2. Fetch events with `created_at_lt=sync_end`
        3. For subsequent pages, use `after_cursor={last.cursor}&created_at_lt=sync_end`
        4. Continue until `has_more=false`
        5. For each event, fetch the entity data from the appropriate endpoint if needed
        6. Store `sync_end` as checkpoint for next sync

        **Handling deletions:** When `event_type` ends with "\\__deleted" or "\\__removed",
        the entity no longer exists. Remove it from your local cache/database. Some
        deletion events include a `payload` field with additional context (e.g.,
        `album_asset_removed` includes `album_id` and `asset_id` since the junction
        record is deleted).

        **Event types:**

        - `asset_created`, `asset_updated`, `asset_deleted`
        - `album_created`, `album_updated`, `album_deleted`
        - `person_created`, `person_updated`, `person_deleted`
        - `face_created`, `face_updated`, `face_deleted`
        - `album_asset_added`, `album_asset_removed`
        - `exif_created`, `exif_updated`

        Args:
          after_cursor: Cursor from the last event to paginate from. Pass the `cursor` field from the
              last event to get the next page.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601 format)

          created_at_lt: Only return events created before this timestamp (ISO 8601 format). Recommended
              for bounding sync operations.

          entity_types: Comma-separated list of entity types to include (e.g., 'asset,album'). Valid
              types: asset, album, person, face, album_asset, exif. Default: all types.

          library_id: Library to list events from. If not provided, uses the user's default library.

          limit: Maximum number of events to return (1-500)

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
        Retrieves a list of entity change events for syncing.

        Events are lightweight records indicating that entities have changed. Each event
        contains the entity type, entity ID, and event type (e.g., "asset_created",
        "album_deleted"). Clients should fetch full entity data from the appropriate
        endpoints if needed.

        **Pagination:** Use the `after_cursor` parameter with the `cursor` value from
        the last event to fetch the next page. The `has_more` field indicates if more
        events exist.

        **Recommended sync pattern:**

        1. Capture current time as `sync_end`
        2. Fetch events with `created_at_lt=sync_end`
        3. For subsequent pages, use `after_cursor={last.cursor}&created_at_lt=sync_end`
        4. Continue until `has_more=false`
        5. For each event, fetch the entity data from the appropriate endpoint if needed
        6. Store `sync_end` as checkpoint for next sync

        **Handling deletions:** When `event_type` ends with "\\__deleted" or "\\__removed",
        the entity no longer exists. Remove it from your local cache/database. Some
        deletion events include a `payload` field with additional context (e.g.,
        `album_asset_removed` includes `album_id` and `asset_id` since the junction
        record is deleted).

        **Event types:**

        - `asset_created`, `asset_updated`, `asset_deleted`
        - `album_created`, `album_updated`, `album_deleted`
        - `person_created`, `person_updated`, `person_deleted`
        - `face_created`, `face_updated`, `face_deleted`
        - `album_asset_added`, `album_asset_removed`
        - `exif_created`, `exif_updated`

        Args:
          after_cursor: Cursor from the last event to paginate from. Pass the `cursor` field from the
              last event to get the next page.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601 format)

          created_at_lt: Only return events created before this timestamp (ISO 8601 format). Recommended
              for bounding sync operations.

          entity_types: Comma-separated list of entity types to include (e.g., 'asset,album'). Valid
              types: asset, album, person, face, album_asset, exif. Default: all types.

          library_id: Library to list events from. If not provided, uses the user's default library.

          limit: Maximum number of events to return (1-500)

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
