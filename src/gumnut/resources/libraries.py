# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import library_create_params, library_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.library_response import LibraryResponse
from ..types.library_list_response import LibraryListResponse

__all__ = ["LibrariesResource", "AsyncLibrariesResource"]


class LibrariesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LibrariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LibrariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LibrariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return LibrariesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Creates a new, empty library.

        A library is the top-level container for assets,
        albums, people, and faces — most users have exactly one. Only create a new
        library when the user explicitly asks for a separate container.

        Args:
          name: Display name for the new library. Required.

          description: Optional free-form description shown alongside the library name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/libraries",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                library_create_params.LibraryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    def retrieve(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Fetches one library's metadata (name, description, asset count).

        Use when you
        already have a specific `library_id`; for enumerating a user's libraries prefer
        `list_libraries`.

        Args:
          library_id: Library ID (with `lib_` prefix) to fetch. Obtain from `list_libraries` or any
              response containing a library reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return self._get(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    def update(
        self,
        library_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Updates the `name` and/or `description` of an existing library.

        Only the fields
        included in the request body are changed. Library contents (assets, albums,
        people, faces) are not affected.

        Args:
          library_id: Library ID (with `lib_` prefix) of the library to update.

          description: New free-form description for the library. Omit to leave unchanged.

          name: New display name for the library. Omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return self._patch(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                library_update_params.LibraryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryListResponse:
        """
        Returns every library the user owns (no pagination — users typically have one or
        a handful). Call this when another tool's `library_id` parameter is required but
        you don't yet know which libraries exist. A single-library user can usually omit
        `library_id` on other tools entirely.
        """
        return self._get(
            "/api/libraries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryListResponse,
        )

    def delete(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the library and all its associated database records — assets, albums,
        people, and faces — via cascading foreign-key delete. This is irreversible and
        should be used only when the user explicitly confirms they want to destroy an
        entire library.

        **Does not delete asset files from object storage.** The library's underlying
        asset files will be orphaned in storage. To purge files as well, call
        `delete_asset` on each asset first (that endpoint removes both the database
        record and the stored file), then delete the library.

        Args:
          library_id: Library ID (with `lib_` prefix) of the library to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLibrariesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLibrariesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLibrariesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLibrariesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncLibrariesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Creates a new, empty library.

        A library is the top-level container for assets,
        albums, people, and faces — most users have exactly one. Only create a new
        library when the user explicitly asks for a separate container.

        Args:
          name: Display name for the new library. Required.

          description: Optional free-form description shown alongside the library name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/libraries",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                library_create_params.LibraryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    async def retrieve(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Fetches one library's metadata (name, description, asset count).

        Use when you
        already have a specific `library_id`; for enumerating a user's libraries prefer
        `list_libraries`.

        Args:
          library_id: Library ID (with `lib_` prefix) to fetch. Obtain from `list_libraries` or any
              response containing a library reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return await self._get(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    async def update(
        self,
        library_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryResponse:
        """Updates the `name` and/or `description` of an existing library.

        Only the fields
        included in the request body are changed. Library contents (assets, albums,
        people, faces) are not affected.

        Args:
          library_id: Library ID (with `lib_` prefix) of the library to update.

          description: New free-form description for the library. Omit to leave unchanged.

          name: New display name for the library. Omit to leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        return await self._patch(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                library_update_params.LibraryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LibraryListResponse:
        """
        Returns every library the user owns (no pagination — users typically have one or
        a handful). Call this when another tool's `library_id` parameter is required but
        you don't yet know which libraries exist. A single-library user can usually omit
        `library_id` on other tools entirely.
        """
        return await self._get(
            "/api/libraries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LibraryListResponse,
        )

    async def delete(
        self,
        library_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the library and all its associated database records — assets, albums,
        people, and faces — via cascading foreign-key delete. This is irreversible and
        should be used only when the user explicitly confirms they want to destroy an
        entire library.

        **Does not delete asset files from object storage.** The library's underlying
        asset files will be orphaned in storage. To purge files as well, call
        `delete_asset` on each asset first (that endpoint removes both the database
        record and the stored file), then delete the library.

        Args:
          library_id: Library ID (with `lib_` prefix) of the library to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not library_id:
            raise ValueError(f"Expected a non-empty value for `library_id` but received {library_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/libraries/{library_id}", library_id=library_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LibrariesResourceWithRawResponse:
    def __init__(self, libraries: LibrariesResource) -> None:
        self._libraries = libraries

        self.create = to_raw_response_wrapper(
            libraries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            libraries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            libraries.update,
        )
        self.list = to_raw_response_wrapper(
            libraries.list,
        )
        self.delete = to_raw_response_wrapper(
            libraries.delete,
        )


class AsyncLibrariesResourceWithRawResponse:
    def __init__(self, libraries: AsyncLibrariesResource) -> None:
        self._libraries = libraries

        self.create = async_to_raw_response_wrapper(
            libraries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            libraries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            libraries.update,
        )
        self.list = async_to_raw_response_wrapper(
            libraries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            libraries.delete,
        )


class LibrariesResourceWithStreamingResponse:
    def __init__(self, libraries: LibrariesResource) -> None:
        self._libraries = libraries

        self.create = to_streamed_response_wrapper(
            libraries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            libraries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            libraries.update,
        )
        self.list = to_streamed_response_wrapper(
            libraries.list,
        )
        self.delete = to_streamed_response_wrapper(
            libraries.delete,
        )


class AsyncLibrariesResourceWithStreamingResponse:
    def __init__(self, libraries: AsyncLibrariesResource) -> None:
        self._libraries = libraries

        self.create = async_to_streamed_response_wrapper(
            libraries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            libraries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            libraries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            libraries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            libraries.delete,
        )
