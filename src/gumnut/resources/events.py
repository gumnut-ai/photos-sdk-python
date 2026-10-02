# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ..types import event_get_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
    """
    Change events (create/update/delete) for entities in a library, for synchronising a local copy or auditing recent activity. Events reference entities by type and ID; fetch full data with the corresponding resource.
    """

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
        entity_types: Optional[SequenceNotStr[str]] | Omit = omit,
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

        **Sync pattern:**

        1. Load the stored cursor, or start with none for a first sync.
        2. Request a page with `after_cursor` set to that cursor.
        3. Treat each event as "this changed": re-read the current state of the entity
           it names and upsert it, or drop it when the read returns not-found. For
           `album_asset_*` events, re-read that album's membership rather than applying
           the add or remove directly.
        4. After applying the page, store its `next_cursor`.
        5. Repeat until `has_more` is false. The client is then caught up; the next sync
           resumes at step 1.

        Reading forward from a stored cursor returns every committed event after it,
        each once, so a cursor is the only checkpoint a client needs; never store a
        timestamp. Processing must be idempotent: a crash before step 4 replays the
        page. An event appears once every transaction older than its own has finished,
        so it can trail its commit. Events are not in commit order: two changes to one
        entity can arrive out of order, which is why step 3 re-reads state.

        Returns 400 for an unknown entity type or a malformed cursor, and for a cursor
        ahead of the database, as after a restore that went back in time. None clears on
        retry; after a cursor error, resync from no cursor.

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
        - `metadata_updated`
        - `stack_created`, `stack_updated`, `stack_deleted`

        **People and faces:** `person_updated` fires only when a person's own fields
        change — name, birth date, hidden, favorite, or thumbnail face. A person's face
        count, asset count, and cluster metrics follow its faces, so their changes
        arrive as `face_*` events only; refetch the person when a face event names it. A
        `face_updated` payload names the face's new `person_id` and its
        `previous_person_id`; a `face_deleted` payload carries `previous_person_id`.
        Refetch both persons when they're non-null. A `previous_person_id` may name a
        person that was deleted in the same change (a merge or a person deletion), so
        handle a 404 on the refetch.

        Args:
          after_cursor: Opaque cursor to resume after: the previous page's `next_cursor`. Omit for a
              first sync.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601). A display
              filter, not a sync checkpoint: `created_at` is when the writer's transaction
              started, so a later-committing event can carry an earlier timestamp.

          created_at_lt: Ignored. Reads are bounded by `next_cursor`; a timestamp bound could skip
              events.

          entity_types: Entity types to include (e.g., `asset`, `album`). Valid values: `asset`,
              `album`, `person`, `face`, `album_asset`, `metadata`, `stack`. Accepts multiple
              `entity_types=` query params or a single comma-delimited value (e.g.,
              `entity_types=asset,album`). Omit to receive events for all types.

          library_id: Library to stream events from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

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
    """
    Change events (create/update/delete) for entities in a library, for synchronising a local copy or auditing recent activity. Events reference entities by type and ID; fetch full data with the corresponding resource.
    """

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
        entity_types: Optional[SequenceNotStr[str]] | Omit = omit,
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

        **Sync pattern:**

        1. Load the stored cursor, or start with none for a first sync.
        2. Request a page with `after_cursor` set to that cursor.
        3. Treat each event as "this changed": re-read the current state of the entity
           it names and upsert it, or drop it when the read returns not-found. For
           `album_asset_*` events, re-read that album's membership rather than applying
           the add or remove directly.
        4. After applying the page, store its `next_cursor`.
        5. Repeat until `has_more` is false. The client is then caught up; the next sync
           resumes at step 1.

        Reading forward from a stored cursor returns every committed event after it,
        each once, so a cursor is the only checkpoint a client needs; never store a
        timestamp. Processing must be idempotent: a crash before step 4 replays the
        page. An event appears once every transaction older than its own has finished,
        so it can trail its commit. Events are not in commit order: two changes to one
        entity can arrive out of order, which is why step 3 re-reads state.

        Returns 400 for an unknown entity type or a malformed cursor, and for a cursor
        ahead of the database, as after a restore that went back in time. None clears on
        retry; after a cursor error, resync from no cursor.

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
        - `metadata_updated`
        - `stack_created`, `stack_updated`, `stack_deleted`

        **People and faces:** `person_updated` fires only when a person's own fields
        change — name, birth date, hidden, favorite, or thumbnail face. A person's face
        count, asset count, and cluster metrics follow its faces, so their changes
        arrive as `face_*` events only; refetch the person when a face event names it. A
        `face_updated` payload names the face's new `person_id` and its
        `previous_person_id`; a `face_deleted` payload carries `previous_person_id`.
        Refetch both persons when they're non-null. A `previous_person_id` may name a
        person that was deleted in the same change (a merge or a person deletion), so
        handle a 404 on the refetch.

        Args:
          after_cursor: Opaque cursor to resume after: the previous page's `next_cursor`. Omit for a
              first sync.

          created_at_gte: Only return events created at or after this timestamp (ISO 8601). A display
              filter, not a sync checkpoint: `created_at` is when the writer's transaction
              started, so a later-committing event can carry an earlier timestamp.

          created_at_lt: Ignored. Reads are bounded by `next_cursor`; a timestamp bound could skip
              events.

          entity_types: Entity types to include (e.g., `asset`, `album`). Valid values: `asset`,
              `album`, `person`, `face`, `album_asset`, `metadata`, `stack`. Accepts multiple
              `entity_types=` query params or a single comma-delimited value (e.g.,
              `entity_types=asset,album`). Omit to receive events for all types.

          library_id: Library to stream events from. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

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
