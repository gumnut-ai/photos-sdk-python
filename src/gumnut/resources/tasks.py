# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import task_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.task_response import TaskResponse
from ..types.task_list_response import TaskListResponse
from ..types.task_list_for_asset_response import TaskListForAssetResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    """Status of background processing tasks."""

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["pending", "started", "success", "failure"]] | Omit = omit,
        task_type: Optional[
            Literal[
                "image_quality",
                "embedding",
                "face_detection",
                "face_clustering",
                "asset_description",
                "asset_storage_cleanup",
                "asset_version_storage_cleanup",
                "reverse_geocoding",
                "video_thumbnail_extract",
                "video_metadata_extract",
                "thumbhash",
                "display_proxy_generation",
                "burst_detection",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListResponse:
        """
        List background tasks for the authenticated user with optional filtering.

        Results are ordered newest first. Returns 404 when `library_id` names a library
        that does not exist or is not accessible to the authenticated user.

        Args:
          library_id: Restrict results to tasks owned by this library. When omitted, returns tasks
              across every library the authenticated user owns.

          limit: Maximum number of tasks to return.

          status: Return only tasks currently in this execution status.

          task_type: Return only tasks of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/tasks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "library_id": library_id,
                        "limit": limit,
                        "status": status,
                        "task_type": task_type,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskResponse:
        """
        Get the status of a background task by its ID.

        Returns 404 if no task with the given identifier exists among the authenticated
        user's libraries.

        Args:
          task_id: Task identifier — either the task's `id` or its `celery_task_id`; both are
              accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskResponse,
        )

    def list_for_asset(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListForAssetResponse:
        """Get all background tasks for a specific asset.

        Results are ordered newest first.

        Args:
          asset_id: ID of the asset whose tasks to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/api/tasks/asset/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskListForAssetResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    """Status of background processing tasks."""

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gumnut-ai/photos-sdk-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        library_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["pending", "started", "success", "failure"]] | Omit = omit,
        task_type: Optional[
            Literal[
                "image_quality",
                "embedding",
                "face_detection",
                "face_clustering",
                "asset_description",
                "asset_storage_cleanup",
                "asset_version_storage_cleanup",
                "reverse_geocoding",
                "video_thumbnail_extract",
                "video_metadata_extract",
                "thumbhash",
                "display_proxy_generation",
                "burst_detection",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListResponse:
        """
        List background tasks for the authenticated user with optional filtering.

        Results are ordered newest first. Returns 404 when `library_id` names a library
        that does not exist or is not accessible to the authenticated user.

        Args:
          library_id: Restrict results to tasks owned by this library. When omitted, returns tasks
              across every library the authenticated user owns.

          limit: Maximum number of tasks to return.

          status: Return only tasks currently in this execution status.

          task_type: Return only tasks of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/tasks/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "library_id": library_id,
                        "limit": limit,
                        "status": status,
                        "task_type": task_type,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    async def get(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskResponse:
        """
        Get the status of a background task by its ID.

        Returns 404 if no task with the given identifier exists among the authenticated
        user's libraries.

        Args:
          task_id: Task identifier — either the task's `id` or its `celery_task_id`; both are
              accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskResponse,
        )

    async def list_for_asset(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskListForAssetResponse:
        """Get all background tasks for a specific asset.

        Results are ordered newest first.

        Args:
          asset_id: ID of the asset whose tasks to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/api/tasks/asset/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskListForAssetResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.get = to_raw_response_wrapper(
            tasks.get,
        )
        self.list_for_asset = to_raw_response_wrapper(
            tasks.list_for_asset,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.get = async_to_raw_response_wrapper(
            tasks.get,
        )
        self.list_for_asset = async_to_raw_response_wrapper(
            tasks.list_for_asset,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.get = to_streamed_response_wrapper(
            tasks.get,
        )
        self.list_for_asset = to_streamed_response_wrapper(
            tasks.list_for_asset,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.get = async_to_streamed_response_wrapper(
            tasks.get,
        )
        self.list_for_asset = async_to_streamed_response_wrapper(
            tasks.list_for_asset,
        )
