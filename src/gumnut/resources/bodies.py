# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import body_list_params, body_delete_params, body_update_params, body_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.body_response import BodyResponse
from ..types.body_delete_response import BodyDeleteResponse

__all__ = ["BodiesResource", "AsyncBodiesResource"]


class BodiesResource(SyncAPIResource):
    """People found in photos without a face record."""

    @cached_property
    def with_raw_response(self) -> BodiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BodiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return BodiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        body_id: str,
        *,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyResponse:
        """
        Fetches one body by ID: its box, its person and whether that link was automatic
        or manual. Use when you already have a `body_id`.

        Args:
          body_id: Body ID (with `body_` prefix) to fetch. Carried by the entries of an asset's
              `bodies` field (returned with `include=bodies`).

          include: Opt-in expansion fields. Supported value: `candidates` (adds each body's
              `candidates`, the named people who may be the person in it). Accepts multiple
              `include=` query params or a single comma-delimited value. Unknown values
              return 422.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return self._get(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include": include,
                        "library_id": library_id,
                    },
                    body_retrieve_params.BodyRetrieveParams,
                ),
            ),
            cast_to=BodyResponse,
        )

    def update(
        self,
        body_id: str,
        *,
        person_id: Optional[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyResponse:
        """
        Links a body to a person, or removes its person (set `person_id` to null); a
        body with no person is still returned. Sending the current person ID marks the
        link as manual.

        To create a new identity first, call `create_person`. Use `delete_body` when the
        body is not a person at all.

        Args:
          body_id: Body ID (with `body_` prefix) of the body to update.

          person_id: Person ID (with `person_` prefix) to link this body to, or `null` to remove its
              person; the body stays, with no person.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return self._patch(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            body=maybe_transform({"person_id": person_id}, body_update_params.BodyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, body_update_params.BodyUpdateParams),
            ),
            cast_to=BodyResponse,
        )

    def list(
        self,
        *,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BodyResponse]:
        """
        Returns a paginated list of bodies, newest first, optionally filtered by asset,
        person, or ID. A body is a person in a photo without a face record, for example
        someone facing away from the camera. Its `person_id` is `null` until it is
        linked; link it with `update_body`. Pass `include=candidates` for people it may
        be.

        **Use `list_faces` instead** for face detections, and `list_people` for the
        people themselves.

        To choose photos of a person, use `list_assets` or `search_assets` with
        `person_ids`. A body match may not show their face, so when choosing photos of
        someone, prefer `person_link=face`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last body in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only bodies in this asset.

          ids: Look up specific bodies by ID (max 200). IDs use the `body_` prefix. Accepts
              multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=body_1,body_2`).

          include: Opt-in expansion fields. Supported value: `candidates` (adds each body's
              `candidates`, the named people who may be the person in it). Accepts multiple
              `include=` query params or a single comma-delimited value. Unknown values
              return 422.

          library_id: Library to list from. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          limit: Maximum number of bodies per page (1–200). Defaults to 20.

          person_id: Return only bodies linked to this person.

          starting_after_id: Cursor for pagination. Pass the `id` of the last body in the previous response's
              `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bodies",
            page=SyncCursorPage[BodyResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    body_list_params.BodyListParams,
                ),
            ),
            model=BodyResponse,
        )

    def delete(
        self,
        body_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyDeleteResponse:
        """
        Deletes a body that is not a person; the asset and any person it was linked to
        are both preserved. **Use `update_body` with `person_id=null` instead** when it
        is a person but not this one. Use `trash_assets` to remove the photo.

        Args:
          body_id: Body ID (with `body_` prefix) of the body to delete.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return self._delete(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, body_delete_params.BodyDeleteParams),
            ),
            cast_to=BodyDeleteResponse,
        )


class AsyncBodiesResource(AsyncAPIResource):
    """People found in photos without a face record."""

    @cached_property
    def with_raw_response(self) -> AsyncBodiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBodiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncBodiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        body_id: str,
        *,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyResponse:
        """
        Fetches one body by ID: its box, its person and whether that link was automatic
        or manual. Use when you already have a `body_id`.

        Args:
          body_id: Body ID (with `body_` prefix) to fetch. Carried by the entries of an asset's
              `bodies` field (returned with `include=bodies`).

          include: Opt-in expansion fields. Supported value: `candidates` (adds each body's
              `candidates`, the named people who may be the person in it). Accepts multiple
              `include=` query params or a single comma-delimited value. Unknown values
              return 422.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return await self._get(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include": include,
                        "library_id": library_id,
                    },
                    body_retrieve_params.BodyRetrieveParams,
                ),
            ),
            cast_to=BodyResponse,
        )

    async def update(
        self,
        body_id: str,
        *,
        person_id: Optional[str],
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyResponse:
        """
        Links a body to a person, or removes its person (set `person_id` to null); a
        body with no person is still returned. Sending the current person ID marks the
        link as manual.

        To create a new identity first, call `create_person`. Use `delete_body` when the
        body is not a person at all.

        Args:
          body_id: Body ID (with `body_` prefix) of the body to update.

          person_id: Person ID (with `person_` prefix) to link this body to, or `null` to remove its
              person; the body stays, with no person.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return await self._patch(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            body=await async_maybe_transform({"person_id": person_id}, body_update_params.BodyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, body_update_params.BodyUpdateParams),
            ),
            cast_to=BodyResponse,
        )

    def list(
        self,
        *,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        starting_after_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BodyResponse, AsyncCursorPage[BodyResponse]]:
        """
        Returns a paginated list of bodies, newest first, optionally filtered by asset,
        person, or ID. A body is a person in a photo without a face record, for example
        someone facing away from the camera. Its `person_id` is `null` until it is
        linked; link it with `update_body`. Pass `include=candidates` for people it may
        be.

        **Use `list_faces` instead** for face detections, and `list_people` for the
        people themselves.

        To choose photos of a person, use `list_assets` or `search_assets` with
        `person_ids`. A body match may not show their face, so when choosing photos of
        someone, prefer `person_link=face`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last body in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only bodies in this asset.

          ids: Look up specific bodies by ID (max 200). IDs use the `body_` prefix. Accepts
              multiple `ids=` query params or a single comma-delimited value (e.g.,
              `ids=body_1,body_2`).

          include: Opt-in expansion fields. Supported value: `candidates` (adds each body's
              `candidates`, the named people who may be the person in it). Accepts multiple
              `include=` query params or a single comma-delimited value. Unknown values
              return 422.

          library_id: Library to list from. Optional if the user has a single live (non-trashed)
              library; required when they have multiple.

          limit: Maximum number of bodies per page (1–200). Defaults to 20.

          person_id: Return only bodies linked to this person.

          starting_after_id: Cursor for pagination. Pass the `id` of the last body in the previous response's
              `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/bodies",
            page=AsyncCursorPage[BodyResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "include": include,
                        "library_id": library_id,
                        "limit": limit,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    body_list_params.BodyListParams,
                ),
            ),
            model=BodyResponse,
        )

    async def delete(
        self,
        body_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BodyDeleteResponse:
        """
        Deletes a body that is not a person; the asset and any person it was linked to
        are both preserved. **Use `update_body` with `person_id=null` instead** when it
        is a person but not this one. Use `trash_assets` to remove the photo.

        Args:
          body_id: Body ID (with `body_` prefix) of the body to delete.

          library_id: Library the body belongs to. Optional if the user has a single live
              (non-trashed) library; required when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not body_id:
            raise ValueError(f"Expected a non-empty value for `body_id` but received {body_id!r}")
        return await self._delete(
            path_template("/api/bodies/{body_id}", body_id=body_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, body_delete_params.BodyDeleteParams),
            ),
            cast_to=BodyDeleteResponse,
        )


class BodiesResourceWithRawResponse:
    def __init__(self, bodies: BodiesResource) -> None:
        self._bodies = bodies

        self.retrieve = to_raw_response_wrapper(
            bodies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            bodies.update,
        )
        self.list = to_raw_response_wrapper(
            bodies.list,
        )
        self.delete = to_raw_response_wrapper(
            bodies.delete,
        )


class AsyncBodiesResourceWithRawResponse:
    def __init__(self, bodies: AsyncBodiesResource) -> None:
        self._bodies = bodies

        self.retrieve = async_to_raw_response_wrapper(
            bodies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            bodies.update,
        )
        self.list = async_to_raw_response_wrapper(
            bodies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bodies.delete,
        )


class BodiesResourceWithStreamingResponse:
    def __init__(self, bodies: BodiesResource) -> None:
        self._bodies = bodies

        self.retrieve = to_streamed_response_wrapper(
            bodies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            bodies.update,
        )
        self.list = to_streamed_response_wrapper(
            bodies.list,
        )
        self.delete = to_streamed_response_wrapper(
            bodies.delete,
        )


class AsyncBodiesResourceWithStreamingResponse:
    def __init__(self, bodies: AsyncBodiesResource) -> None:
        self._bodies = bodies

        self.retrieve = async_to_streamed_response_wrapper(
            bodies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            bodies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bodies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bodies.delete,
        )
