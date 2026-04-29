# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import face_list_params, face_delete_params, face_update_params, face_retrieve_params
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
from ..types.face_response import FaceResponse

__all__ = ["FacesResource", "AsyncFacesResource"]


class FacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return FacesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaceResponse:
        """
        Fetches one face's details (bounding box, assigned person, timestamps,
        thumbnail). Use when you already have a `face_id`.

        Args:
          face_id: Face ID (with `face_` prefix) to fetch. Obtain from `list_faces` or from the
              `faces` array on `get_asset` / `list_assets` responses.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        return self._get(
            path_template("/api/faces/{face_id}", face_id=face_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, face_retrieve_params.FaceRetrieveParams),
            ),
            cast_to=FaceResponse,
        )

    def update(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaceResponse:
        """
        Assigns a face to a specific person, or detaches it (set `person_id` to null).
        This is the right tool for 'this face is Alice' or 'this face isn't Bob after
        all'.

        Currently only the `person_id` field is mutable. To create a brand-new identity
        first, call `create_person`; to delete the face detection entirely, use
        `delete_face`.

        Args:
          face_id: Face ID (with `face_` prefix) of the face detection to update.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          person_id: Target person ID (with `person_` prefix) to assign this face to. Pass `null` to
              detach the face from its current person without deleting either. Get IDs from
              `list_people`; use `create_person` first if the target identity doesn't exist
              yet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        return self._patch(
            path_template("/api/faces/{face_id}", face_id=face_id),
            body=maybe_transform({"person_id": person_id}, face_update_params.FaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, face_update_params.FaceUpdateParams),
            ),
            cast_to=FaceResponse,
        )

    def list(
        self,
        *,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> SyncCursorPage[FaceResponse]:
        """
        Returns a paginated list of individual face detections (with bounding boxes),
        ordered by creation time (newest first). Each row is a single face in a single
        asset — a person with many photos will have many face rows.

        **Use `list_people` instead** when the user wants the grouped identities ('list
        everyone in my library') rather than individual face detections. This tool is
        useful for curating clustering results, finding unassigned faces, or picking a
        thumbnail face for a person via `update_person.thumbnail_face_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last face in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only faces detected in this asset. Useful for 'show me all the faces in
              this photo'.

          ids: Look up specific faces by ID (max 100). IDs use the `face_` prefix.

          library_id: Library to list from. Optional if the user has a single library; required when
              they have multiple.

          limit: Maximum number of faces per page (1–200). Defaults to 20.

          person_id: Return only faces currently assigned to this person. Useful for reviewing or
              curating a person's face cluster.

          starting_after_id: Cursor for pagination. Pass the `id` of the last face in the previous response's
              `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/faces",
            page=SyncCursorPage[FaceResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    face_list_params.FaceListParams,
                ),
            ),
            model=FaceResponse,
        )

    def delete(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes one face detection row.

        The underlying asset and the person this face
        was assigned to are both preserved.

        **Use `update_face` with `person_id=null` instead** when the user wants to
        disassociate the face from a person without discarding the detection (so
        re-clustering can try again). Use `delete_person` to remove a person; use
        `trash_assets` (or `permanently_delete_assets` for irreversible removal) to
        remove the photo entirely.

        Args:
          face_id: Face ID (with `face_` prefix) of the face detection to delete.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/faces/{face_id}", face_id=face_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"library_id": library_id}, face_delete_params.FaceDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncFacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncFacesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaceResponse:
        """
        Fetches one face's details (bounding box, assigned person, timestamps,
        thumbnail). Use when you already have a `face_id`.

        Args:
          face_id: Face ID (with `face_` prefix) to fetch. Obtain from `list_faces` or from the
              `faces` array on `get_asset` / `list_assets` responses.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        return await self._get(
            path_template("/api/faces/{face_id}", face_id=face_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, face_retrieve_params.FaceRetrieveParams),
            ),
            cast_to=FaceResponse,
        )

    async def update(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        person_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaceResponse:
        """
        Assigns a face to a specific person, or detaches it (set `person_id` to null).
        This is the right tool for 'this face is Alice' or 'this face isn't Bob after
        all'.

        Currently only the `person_id` field is mutable. To create a brand-new identity
        first, call `create_person`; to delete the face detection entirely, use
        `delete_face`.

        Args:
          face_id: Face ID (with `face_` prefix) of the face detection to update.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          person_id: Target person ID (with `person_` prefix) to assign this face to. Pass `null` to
              detach the face from its current person without deleting either. Get IDs from
              `list_people`; use `create_person` first if the target identity doesn't exist
              yet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        return await self._patch(
            path_template("/api/faces/{face_id}", face_id=face_id),
            body=await async_maybe_transform({"person_id": person_id}, face_update_params.FaceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, face_update_params.FaceUpdateParams),
            ),
            cast_to=FaceResponse,
        )

    def list(
        self,
        *,
        asset_id: Optional[str] | Omit = omit,
        ids: Optional[SequenceNotStr[str]] | Omit = omit,
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
    ) -> AsyncPaginator[FaceResponse, AsyncCursorPage[FaceResponse]]:
        """
        Returns a paginated list of individual face detections (with bounding boxes),
        ordered by creation time (newest first). Each row is a single face in a single
        asset — a person with many photos will have many face rows.

        **Use `list_people` instead** when the user wants the grouped identities ('list
        everyone in my library') rather than individual face detections. This tool is
        useful for curating clustering results, finding unassigned faces, or picking a
        thumbnail face for a person via `update_person.thumbnail_face_id`.

        **Pagination** is cursor-based: when `has_more` is true, pass the `id` of the
        last face in `data` as `starting_after_id` to fetch the next page.

        Args:
          asset_id: Return only faces detected in this asset. Useful for 'show me all the faces in
              this photo'.

          ids: Look up specific faces by ID (max 100). IDs use the `face_` prefix.

          library_id: Library to list from. Optional if the user has a single library; required when
              they have multiple.

          limit: Maximum number of faces per page (1–200). Defaults to 20.

          person_id: Return only faces currently assigned to this person. Useful for reviewing or
              curating a person's face cluster.

          starting_after_id: Cursor for pagination. Pass the `id` of the last face in the previous response's
              `data` to fetch the next page. Omit for the first page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/faces",
            page=AsyncCursorPage[FaceResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "ids": ids,
                        "library_id": library_id,
                        "limit": limit,
                        "person_id": person_id,
                        "starting_after_id": starting_after_id,
                    },
                    face_list_params.FaceListParams,
                ),
            ),
            model=FaceResponse,
        )

    async def delete(
        self,
        face_id: str,
        *,
        library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes one face detection row.

        The underlying asset and the person this face
        was assigned to are both preserved.

        **Use `update_face` with `person_id=null` instead** when the user wants to
        disassociate the face from a person without discarding the detection (so
        re-clustering can try again). Use `delete_person` to remove a person; use
        `trash_assets` (or `permanently_delete_assets` for irreversible removal) to
        remove the photo entirely.

        Args:
          face_id: Face ID (with `face_` prefix) of the face detection to delete.

          library_id: Library the face belongs to. Optional if the user has a single library; required
              when they have multiple.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not face_id:
            raise ValueError(f"Expected a non-empty value for `face_id` but received {face_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/faces/{face_id}", face_id=face_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"library_id": library_id}, face_delete_params.FaceDeleteParams),
            ),
            cast_to=NoneType,
        )


class FacesResourceWithRawResponse:
    def __init__(self, faces: FacesResource) -> None:
        self._faces = faces

        self.retrieve = to_raw_response_wrapper(
            faces.retrieve,
        )
        self.update = to_raw_response_wrapper(
            faces.update,
        )
        self.list = to_raw_response_wrapper(
            faces.list,
        )
        self.delete = to_raw_response_wrapper(
            faces.delete,
        )


class AsyncFacesResourceWithRawResponse:
    def __init__(self, faces: AsyncFacesResource) -> None:
        self._faces = faces

        self.retrieve = async_to_raw_response_wrapper(
            faces.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            faces.update,
        )
        self.list = async_to_raw_response_wrapper(
            faces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            faces.delete,
        )


class FacesResourceWithStreamingResponse:
    def __init__(self, faces: FacesResource) -> None:
        self._faces = faces

        self.retrieve = to_streamed_response_wrapper(
            faces.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            faces.update,
        )
        self.list = to_streamed_response_wrapper(
            faces.list,
        )
        self.delete = to_streamed_response_wrapper(
            faces.delete,
        )


class AsyncFacesResourceWithStreamingResponse:
    def __init__(self, faces: AsyncFacesResource) -> None:
        self._faces = faces

        self.retrieve = async_to_streamed_response_wrapper(
            faces.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            faces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            faces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            faces.delete,
        )
