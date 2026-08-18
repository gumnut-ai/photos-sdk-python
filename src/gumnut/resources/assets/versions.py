# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.assets import version_list_params
from ...types.asset_response import AssetResponse
from ...types.assets.version_list_response import VersionListResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    """
    Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
    """

    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def list(
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
    ) -> VersionListResponse:
        """
        Returns every retained rendering of one asset, ordered by `position` ascending —
        the uploaded original first, the current rendering last. Not paginated. Each
        entry's `version_urls` follows the same `include` semantics as an asset's
        `asset_urls`: lean `thumbnail` by default, `include=variants` for the remaining
        rungs and the exact-byte `original`.

        Args:
          asset_id: Asset ID (with `asset_` prefix) whose versions to list.

          include: Optional response expansion. The single accepted value is `variants`: without it
              each row's `version_urls` carries only its lean thumbnail rung; with it, every
              rung plus the signed exact-byte `original`. Accepts multiple `include=` query
              params or a single comma-delimited value. Unknown values return 422.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/api/assets/{asset_id}/versions", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, version_list_params.VersionListParams),
            ),
            cast_to=VersionListResponse,
        )

    def delete(
        self,
        version_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Irreversibly deletes the current non-original version and restores its
        predecessor. The original returns 422; a buried version returns 409.

        Args:
          asset_id: Asset ID (with `asset_` prefix) whose version to delete.

          version_id: Version ID (with `asset_version_` prefix) to delete. Must be the asset's current
              non-original version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._delete(
            path_template("/api/assets/{asset_id}/versions/{version_id}", asset_id=asset_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    def revert(
        self,
        version_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Makes a retained version current and irreversibly deletes its descendants.
        Reverting to the current version is a no-op.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to revert.

          version_id: Version ID (with `asset_version_` prefix) to make current. Every version at a
              later position is deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._post(
            path_template(
                "/api/assets/{asset_id}/versions/{version_id}/revert", asset_id=asset_id, version_id=version_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    """
    Photos and videos in a library: upload, list and filter, update metadata, trash and restore.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def list(
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
    ) -> VersionListResponse:
        """
        Returns every retained rendering of one asset, ordered by `position` ascending —
        the uploaded original first, the current rendering last. Not paginated. Each
        entry's `version_urls` follows the same `include` semantics as an asset's
        `asset_urls`: lean `thumbnail` by default, `include=variants` for the remaining
        rungs and the exact-byte `original`.

        Args:
          asset_id: Asset ID (with `asset_` prefix) whose versions to list.

          include: Optional response expansion. The single accepted value is `variants`: without it
              each row's `version_urls` carries only its lean thumbnail rung; with it, every
              rung plus the signed exact-byte `original`. Accepts multiple `include=` query
              params or a single comma-delimited value. Unknown values return 422.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/api/assets/{asset_id}/versions", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, version_list_params.VersionListParams),
            ),
            cast_to=VersionListResponse,
        )

    async def delete(
        self,
        version_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Irreversibly deletes the current non-original version and restores its
        predecessor. The original returns 422; a buried version returns 409.

        Args:
          asset_id: Asset ID (with `asset_` prefix) whose version to delete.

          version_id: Version ID (with `asset_version_` prefix) to delete. Must be the asset's current
              non-original version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._delete(
            path_template("/api/assets/{asset_id}/versions/{version_id}", asset_id=asset_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )

    async def revert(
        self,
        version_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetResponse:
        """
        Makes a retained version current and irreversibly deletes its descendants.
        Reverting to the current version is a no-op.

        Args:
          asset_id: Asset ID (with `asset_` prefix) to revert.

          version_id: Version ID (with `asset_version_` prefix) to make current. Every version at a
              later position is deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._post(
            path_template(
                "/api/assets/{asset_id}/versions/{version_id}/revert", asset_id=asset_id, version_id=version_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.revert = to_raw_response_wrapper(
            versions.revert,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.revert = async_to_raw_response_wrapper(
            versions.revert,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.revert = to_streamed_response_wrapper(
            versions.revert,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.revert = async_to_streamed_response_wrapper(
            versions.revert,
        )
