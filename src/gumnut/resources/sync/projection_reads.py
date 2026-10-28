# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.sync import projection_read_read_params
from ..._base_client import make_request_options
from ...types.sync.projection_key_param import ProjectionKeyParam
from ...types.sync.relation_selector_param import RelationSelectorParam
from ...types.sync.projection_profile_param import ProjectionProfileParam
from ...types.sync.projection_read_response import ProjectionReadResponse

__all__ = ["ProjectionReadsResource", "AsyncProjectionReadsResource"]


class ProjectionReadsResource(SyncAPIResource):
    """
    Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
    """

    @cached_property
    def with_raw_response(self) -> ProjectionReadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectionReadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectionReadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return ProjectionReadsResourceWithStreamingResponse(self)

    @overload
    def read(
        self,
        *,
        keys: Iterable[ProjectionKeyParam],
        library_id: str,
        mode: Literal["roots"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          keys: Nonempty unique root selection; exceeding capacity returns 413

          library_id: Explicit live library binding for every root and dependency

          mode: Read exactly the explicit roots and their required dependencies

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def read(
        self,
        *,
        library_id: str,
        mode: Literal["baseline_begin"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          library_id: Explicit live library binding for every root and dependency

          mode: Capture finite family bounds and safe event start

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def read(
        self,
        *,
        enumeration_token: str,
        library_id: str,
        mode: Literal["baseline_page"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          enumeration_token: Signed finite selection; never an authorization or snapshot handle

          library_id: Explicit live library binding for every root and dependency

          mode: Continue one baseline family's finite selection

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def read(
        self,
        *,
        enumeration_token: Optional[str],
        library_id: str,
        mode: Literal["relation_page"],
        profile: ProjectionProfileParam,
        selector: RelationSelectorParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          enumeration_token: Null starts a finite relation scan; otherwise continue its signed selection

          library_id: Explicit live library binding for every root and dependency

          mode: Enumerate finite current children with their parent

          profile: Versioned source semantics to project

          selector: Bound relationship and parent identity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["keys", "library_id", "mode", "profile"],
        ["library_id", "mode", "profile"],
        ["enumeration_token", "library_id", "mode", "profile"],
        ["enumeration_token", "library_id", "mode", "profile", "selector"],
    )
    def read(
        self,
        *,
        keys: Iterable[ProjectionKeyParam] | Omit = omit,
        library_id: str,
        mode: Literal["roots"] | Literal["baseline_begin"] | Literal["baseline_page"] | Literal["relation_page"],
        profile: ProjectionProfileParam,
        enumeration_token: str | Optional[str] | Omit = omit,
        selector: RelationSelectorParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        return self._post(
            "/api/sync/projection-reads",
            body=maybe_transform(
                {
                    "keys": keys,
                    "library_id": library_id,
                    "mode": mode,
                    "profile": profile,
                    "enumeration_token": enumeration_token,
                    "selector": selector,
                },
                projection_read_read_params.ProjectionReadReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectionReadResponse,
        )


class AsyncProjectionReadsResource(AsyncAPIResource):
    """
    Read the Gumnut library catalog as coherent roots or finite baseline and relation pages. Enumeration tokens are opaque selection cursors, not authorization or retained snapshots. Install complete bundles and their progress atomically before advancing event catch-up.
    """

    @cached_property
    def with_raw_response(self) -> AsyncProjectionReadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectionReadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectionReadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncProjectionReadsResourceWithStreamingResponse(self)

    @overload
    async def read(
        self,
        *,
        keys: Iterable[ProjectionKeyParam],
        library_id: str,
        mode: Literal["roots"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          keys: Nonempty unique root selection; exceeding capacity returns 413

          library_id: Explicit live library binding for every root and dependency

          mode: Read exactly the explicit roots and their required dependencies

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def read(
        self,
        *,
        library_id: str,
        mode: Literal["baseline_begin"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          library_id: Explicit live library binding for every root and dependency

          mode: Capture finite family bounds and safe event start

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def read(
        self,
        *,
        enumeration_token: str,
        library_id: str,
        mode: Literal["baseline_page"],
        profile: ProjectionProfileParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          enumeration_token: Signed finite selection; never an authorization or snapshot handle

          library_id: Explicit live library binding for every root and dependency

          mode: Continue one baseline family's finite selection

          profile: Versioned source semantics to project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def read(
        self,
        *,
        enumeration_token: Optional[str],
        library_id: str,
        mode: Literal["relation_page"],
        profile: ProjectionProfileParam,
        selector: RelationSelectorParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        """
        Read explicit roots or finite baseline/relation pages with complete dependencies
        from one current read-only source snapshot per request. The gumnut-library
        version 1 profile uses signed finite selection tokens, not retained snapshots.
        Every accepted root is complete or the response fails.

        Args:
          enumeration_token: Null starts a finite relation scan; otherwise continue its signed selection

          library_id: Explicit live library binding for every root and dependency

          mode: Enumerate finite current children with their parent

          profile: Versioned source semantics to project

          selector: Bound relationship and parent identity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["keys", "library_id", "mode", "profile"],
        ["library_id", "mode", "profile"],
        ["enumeration_token", "library_id", "mode", "profile"],
        ["enumeration_token", "library_id", "mode", "profile", "selector"],
    )
    async def read(
        self,
        *,
        keys: Iterable[ProjectionKeyParam] | Omit = omit,
        library_id: str,
        mode: Literal["roots"] | Literal["baseline_begin"] | Literal["baseline_page"] | Literal["relation_page"],
        profile: ProjectionProfileParam,
        enumeration_token: str | Optional[str] | Omit = omit,
        selector: RelationSelectorParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectionReadResponse:
        return await self._post(
            "/api/sync/projection-reads",
            body=await async_maybe_transform(
                {
                    "keys": keys,
                    "library_id": library_id,
                    "mode": mode,
                    "profile": profile,
                    "enumeration_token": enumeration_token,
                    "selector": selector,
                },
                projection_read_read_params.ProjectionReadReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectionReadResponse,
        )


class ProjectionReadsResourceWithRawResponse:
    def __init__(self, projection_reads: ProjectionReadsResource) -> None:
        self._projection_reads = projection_reads

        self.read = to_raw_response_wrapper(
            projection_reads.read,
        )


class AsyncProjectionReadsResourceWithRawResponse:
    def __init__(self, projection_reads: AsyncProjectionReadsResource) -> None:
        self._projection_reads = projection_reads

        self.read = async_to_raw_response_wrapper(
            projection_reads.read,
        )


class ProjectionReadsResourceWithStreamingResponse:
    def __init__(self, projection_reads: ProjectionReadsResource) -> None:
        self._projection_reads = projection_reads

        self.read = to_streamed_response_wrapper(
            projection_reads.read,
        )


class AsyncProjectionReadsResourceWithStreamingResponse:
    def __init__(self, projection_reads: AsyncProjectionReadsResource) -> None:
        self._projection_reads = projection_reads

        self.read = async_to_streamed_response_wrapper(
            projection_reads.read,
        )
