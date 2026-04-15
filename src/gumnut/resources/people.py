# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import person_list_params, person_create_params, person_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.person_response import PersonResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        birth_date: Union[str, date, None] | Omit = omit,
        is_favorite: Optional[bool] | Omit = omit,
        is_hidden: Optional[bool] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        thumbnail_face_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Creates a new person entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/people",
            body=maybe_transform(
                {
                    "birth_date": birth_date,
                    "is_favorite": is_favorite,
                    "is_hidden": is_hidden,
                    "library_id": library_id,
                    "name": name,
                    "thumbnail_face_id": thumbnail_face_id,
                },
                person_create_params.PersonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    def retrieve(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Retrieves details for a specific person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._get(
            path_template("/api/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    def update(
        self,
        person_id: str,
        *,
        birth_date: Union[str, date, None] | Omit = omit,
        is_favorite: Optional[bool] | Omit = omit,
        is_hidden: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        thumbnail_face_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Updates the details of a specific person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._patch(
            path_template("/api/people/{person_id}", person_id=person_id),
            body=maybe_transform(
                {
                    "birth_date": birth_date,
                    "is_favorite": is_favorite,
                    "is_hidden": is_hidden,
                    "name": name,
                    "thumbnail_face_id": thumbnail_face_id,
                },
                person_update_params.PersonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        name_filter: Optional[Literal["named", "unnamed", "all"]] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PersonResponse]:
        """
        Retrieves a paginated list of people, ordered by creation time, descending.

        **Pagination:** When `has_more` is true, pass the `id` of the last person in
        `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Include only people associated with this album ID

          asset_id: Include only people associated with this asset ID

          ids: Filter by specific person IDs (max 100)

          library_id: Library ID (required if user has multiple libraries)

          limit: Max number of people to return (1-200)

          name: Filter by name using case-insensitive substring matching

          name_filter: Filter by name status: 'named' returns only people with a name, 'unnamed'
              returns only people without a name, 'all' returns everyone. Defaults to 'named',
              or 'all' when ids are provided.

          starting_after_id: Cursor for pagination. Pass the `id` of the last person from the previous page
              to get the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/people",
            page=SyncCursorPage[PersonResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "name": name,
                        "name_filter": name_filter,
                        "starting_after_id": starting_after_id,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            model=PersonResponse,
        )

    def delete(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a specific person.

        Orphaned faces will be re-clustered in the next
        clustering pass.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPeopleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        birth_date: Union[str, date, None] | Omit = omit,
        is_favorite: Optional[bool] | Omit = omit,
        is_hidden: Optional[bool] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        thumbnail_face_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Creates a new person entry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/people",
            body=await async_maybe_transform(
                {
                    "birth_date": birth_date,
                    "is_favorite": is_favorite,
                    "is_hidden": is_hidden,
                    "library_id": library_id,
                    "name": name,
                    "thumbnail_face_id": thumbnail_face_id,
                },
                person_create_params.PersonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    async def retrieve(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Retrieves details for a specific person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._get(
            path_template("/api/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    async def update(
        self,
        person_id: str,
        *,
        birth_date: Union[str, date, None] | Omit = omit,
        is_favorite: Optional[bool] | Omit = omit,
        is_hidden: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        thumbnail_face_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PersonResponse:
        """
        Updates the details of a specific person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._patch(
            path_template("/api/people/{person_id}", person_id=person_id),
            body=await async_maybe_transform(
                {
                    "birth_date": birth_date,
                    "is_favorite": is_favorite,
                    "is_hidden": is_hidden,
                    "name": name,
                    "thumbnail_face_id": thumbnail_face_id,
                },
                person_update_params.PersonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonResponse,
        )

    def list(
        self,
        *,
        album_id: Optional[str] | Omit = omit,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        name_filter: Optional[Literal["named", "unnamed", "all"]] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PersonResponse, AsyncCursorPage[PersonResponse]]:
        """
        Retrieves a paginated list of people, ordered by creation time, descending.

        **Pagination:** When `has_more` is true, pass the `id` of the last person in
        `data` as `starting_after_id` to fetch the next page.

        Args:
          album_id: Include only people associated with this album ID

          asset_id: Include only people associated with this asset ID

          ids: Filter by specific person IDs (max 100)

          library_id: Library ID (required if user has multiple libraries)

          limit: Max number of people to return (1-200)

          name: Filter by name using case-insensitive substring matching

          name_filter: Filter by name status: 'named' returns only people with a name, 'unnamed'
              returns only people without a name, 'all' returns everyone. Defaults to 'named',
              or 'all' when ids are provided.

          starting_after_id: Cursor for pagination. Pass the `id` of the last person from the previous page
              to get the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/people",
            page=AsyncCursorPage[PersonResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "album_id": album_id,
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "name": name,
                        "name_filter": name_filter,
                        "starting_after_id": starting_after_id,
                    },
                    person_list_params.PersonListParams,
                ),
            ),
            model=PersonResponse,
        )

    async def delete(
        self,
        person_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a specific person.

        Orphaned faces will be re-clustered in the next
        clustering pass.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/people/{person_id}", person_id=person_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.create = to_raw_response_wrapper(
            people.create,
        )
        self.retrieve = to_raw_response_wrapper(
            people.retrieve,
        )
        self.update = to_raw_response_wrapper(
            people.update,
        )
        self.list = to_raw_response_wrapper(
            people.list,
        )
        self.delete = to_raw_response_wrapper(
            people.delete,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.create = async_to_raw_response_wrapper(
            people.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            people.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            people.update,
        )
        self.list = async_to_raw_response_wrapper(
            people.list,
        )
        self.delete = async_to_raw_response_wrapper(
            people.delete,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.create = to_streamed_response_wrapper(
            people.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            people.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            people.update,
        )
        self.list = to_streamed_response_wrapper(
            people.list,
        )
        self.delete = to_streamed_response_wrapper(
            people.delete,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.create = async_to_streamed_response_wrapper(
            people.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            people.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            people.update,
        )
        self.list = async_to_streamed_response_wrapper(
            people.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            people.delete,
        )
