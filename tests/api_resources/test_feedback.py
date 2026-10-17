# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gumnut import Gumnut, AsyncGumnut
from tests.utils import assert_matches_type
from gumnut.types import FeedbackResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit(self, client: Gumnut) -> None:
        feedback = client.feedback.submit(
            feedback_type="bug",
            message="x",
        )
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    def test_method_submit_with_all_params(self, client: Gumnut) -> None:
        feedback = client.feedback.submit(
            feedback_type="bug",
            message="x",
            task_completed=True,
            tool_names=["x"],
        )
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Gumnut) -> None:
        response = client.feedback.with_raw_response.submit(
            feedback_type="bug",
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Gumnut) -> None:
        with client.feedback.with_streaming_response.submit(
            feedback_type="bug",
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackResult, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_submit(self, async_client: AsyncGumnut) -> None:
        feedback = await async_client.feedback.submit(
            feedback_type="bug",
            message="x",
        )
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncGumnut) -> None:
        feedback = await async_client.feedback.submit(
            feedback_type="bug",
            message="x",
            task_completed=True,
            tool_names=["x"],
        )
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncGumnut) -> None:
        response = await async_client.feedback.with_raw_response.submit(
            feedback_type="bug",
            message="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackResult, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncGumnut) -> None:
        async with async_client.feedback.with_streaming_response.submit(
            feedback_type="bug",
            message="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackResult, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
