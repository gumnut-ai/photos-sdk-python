# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import user_update_params
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
from ..types.user_response import UserResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """The authenticated user's profile."""

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        demo_mode_enabled: bool | Omit = omit,
        face_detection_preference: Optional[bool] | Omit = omit,
        favorite_display_mode: Optional[Literal["favorite", "rating"]] | Omit = omit,
        home_country: Optional[str] | Omit = omit,
        home_subdivision: Optional[str] | Omit = omit,
        immich_library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResponse:
        """Updates preferences on the authenticated user's own account.

        Only the fields
        included in the request body are changed. This endpoint does not accept a user
        ID; it always updates the authenticated caller. Returns 404, without changing
        anything, when `immich_library_id` names a library the caller cannot choose; the
        response is the same whether or not that library exists. `home_country`,
        `home_subdivision` and `face_detection_preference` can be changed only from a
        signed-in app session: an API key or OAuth credential that sends any of them
        gets 403 and nothing changes. Setting `face_detection_preference` to true
        returns 409, which is not retryable, when automatic face detection is not
        available for the home region. Declaring such a home region sets the preference
        to false. Changing these settings keeps face data already stored.

        Args:
          demo_mode_enabled: Enable demo-mode person-name presentation. Omit to leave unchanged; send false
              to disable. Explicit null is not accepted.

          face_detection_preference: Turn automatic face detection on (true) or off (false) for the libraries the
              user owns. Omit to leave unchanged; explicit null is not accepted. The setting
              applies to photos processed from then on; face data already stored is kept.

          favorite_display_mode: Presentation a user prefers for the favorite/rating control.

              - `favorite`: a heart — filled at the top rating, empty otherwise.
              - `rating`: a 0-5 star control.

          home_country: Home country as an uppercase ISO 3166-1 alpha-2 code (e.g. 'US'). Omit to leave
              unchanged; explicit null is not accepted. Changing the country clears
              `home_subdivision` unless the same request sets it.

          home_subdivision: Home state or province: an ISO 3166-2 code without its country prefix (e.g. 'CA'
              for US-CA). Required when the home country is 'US'. Omit to leave unchanged;
              send `null` to clear it.

          immich_library_id: Preferred library. Must be a live library the caller owns or has the
              collaborator role in, and that the request's credential can access; any other id
              returns 404. Omit to leave unchanged; send `null` to clear the preference and
              use the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/users/me",
            body=maybe_transform(
                {
                    "demo_mode_enabled": demo_mode_enabled,
                    "face_detection_preference": face_detection_preference,
                    "favorite_display_mode": favorite_display_mode,
                    "home_country": home_country,
                    "home_subdivision": home_subdivision,
                    "immich_library_id": immich_library_id,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResponse:
        """Returns the profile of the authenticated user (the caller).

        Use this at the
        start of a session to ground subsequent calls (e.g., to confirm the caller's
        identity before making destructive changes). This tool does not accept a user
        ID; it always returns the authenticated caller.
        """
        return self._get(
            "/api/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    """The authenticated user's profile."""

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        demo_mode_enabled: bool | Omit = omit,
        face_detection_preference: Optional[bool] | Omit = omit,
        favorite_display_mode: Optional[Literal["favorite", "rating"]] | Omit = omit,
        home_country: Optional[str] | Omit = omit,
        home_subdivision: Optional[str] | Omit = omit,
        immich_library_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResponse:
        """Updates preferences on the authenticated user's own account.

        Only the fields
        included in the request body are changed. This endpoint does not accept a user
        ID; it always updates the authenticated caller. Returns 404, without changing
        anything, when `immich_library_id` names a library the caller cannot choose; the
        response is the same whether or not that library exists. `home_country`,
        `home_subdivision` and `face_detection_preference` can be changed only from a
        signed-in app session: an API key or OAuth credential that sends any of them
        gets 403 and nothing changes. Setting `face_detection_preference` to true
        returns 409, which is not retryable, when automatic face detection is not
        available for the home region. Declaring such a home region sets the preference
        to false. Changing these settings keeps face data already stored.

        Args:
          demo_mode_enabled: Enable demo-mode person-name presentation. Omit to leave unchanged; send false
              to disable. Explicit null is not accepted.

          face_detection_preference: Turn automatic face detection on (true) or off (false) for the libraries the
              user owns. Omit to leave unchanged; explicit null is not accepted. The setting
              applies to photos processed from then on; face data already stored is kept.

          favorite_display_mode: Presentation a user prefers for the favorite/rating control.

              - `favorite`: a heart — filled at the top rating, empty otherwise.
              - `rating`: a 0-5 star control.

          home_country: Home country as an uppercase ISO 3166-1 alpha-2 code (e.g. 'US'). Omit to leave
              unchanged; explicit null is not accepted. Changing the country clears
              `home_subdivision` unless the same request sets it.

          home_subdivision: Home state or province: an ISO 3166-2 code without its country prefix (e.g. 'CA'
              for US-CA). Required when the home country is 'US'. Omit to leave unchanged;
              send `null` to clear it.

          immich_library_id: Preferred library. Must be a live library the caller owns or has the
              collaborator role in, and that the request's credential can access; any other id
              returns 404. Omit to leave unchanged; send `null` to clear the preference and
              use the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/users/me",
            body=await async_maybe_transform(
                {
                    "demo_mode_enabled": demo_mode_enabled,
                    "face_detection_preference": face_detection_preference,
                    "favorite_display_mode": favorite_display_mode,
                    "home_country": home_country,
                    "home_subdivision": home_subdivision,
                    "immich_library_id": immich_library_id,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )

    async def me(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResponse:
        """Returns the profile of the authenticated user (the caller).

        Use this at the
        start of a session to ground subsequent calls (e.g., to confirm the caller's
        identity before making destructive changes). This tool does not accept a user
        ID; it always returns the authenticated caller.
        """
        return await self._get(
            "/api/users/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.me = to_raw_response_wrapper(
            users.me,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.me = async_to_raw_response_wrapper(
            users.me,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.me = to_streamed_response_wrapper(
            users.me,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.me = async_to_streamed_response_wrapper(
            users.me,
        )
