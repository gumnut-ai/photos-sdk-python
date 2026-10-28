# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .projection_reads import (
    ProjectionReadsResource,
    AsyncProjectionReadsResource,
    ProjectionReadsResourceWithRawResponse,
    AsyncProjectionReadsResourceWithRawResponse,
    ProjectionReadsResourceWithStreamingResponse,
    AsyncProjectionReadsResourceWithStreamingResponse,
)

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def projection_reads(self) -> ProjectionReadsResource:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return ProjectionReadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def projection_reads(self) -> AsyncProjectionReadsResource:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return AsyncProjectionReadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

    @cached_property
    def projection_reads(self) -> ProjectionReadsResourceWithRawResponse:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return ProjectionReadsResourceWithRawResponse(self._sync.projection_reads)


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

    @cached_property
    def projection_reads(self) -> AsyncProjectionReadsResourceWithRawResponse:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return AsyncProjectionReadsResourceWithRawResponse(self._sync.projection_reads)


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

    @cached_property
    def projection_reads(self) -> ProjectionReadsResourceWithStreamingResponse:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return ProjectionReadsResourceWithStreamingResponse(self._sync.projection_reads)


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

    @cached_property
    def projection_reads(self) -> AsyncProjectionReadsResourceWithStreamingResponse:
        """
        Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
        """
        return AsyncProjectionReadsResourceWithStreamingResponse(self._sync.projection_reads)
