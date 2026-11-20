# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List

import httpx
import pytest
from respx import MockRouter

from gumnut import Gumnut, AsyncGumnut
from gumnut._types import Omit

from .utils import update_env

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


def _sent_auth_headers(route: Any) -> List[List[str]]:
    return [[name for name in ["Authorization"] if name in call.request.headers] for call in route.calls]


def _client(*, with_key: bool, **kwargs: Any) -> Gumnut:
    if with_key:
        return Gumnut(base_url=base_url, api_key="My API Key", **kwargs)
    with update_env(GUMNUT_API_KEY=Omit()):
        return Gumnut(base_url=base_url, **kwargs)


def _async_client(*, with_key: bool, **kwargs: Any) -> AsyncGumnut:
    if with_key:
        return AsyncGumnut(base_url=base_url, api_key="My API Key", **kwargs)
    with update_env(GUMNUT_API_KEY=Omit()):
        return AsyncGumnut(base_url=base_url, **kwargs)


class TestNoAuthOperations:
    @pytest.mark.respx(base_url=base_url)
    def test_oauth_auth_url(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/oauth/auth-url").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            with _client(with_key=with_key) as client:
                client.oauth.with_raw_response.auth_url(redirect_uri="redirect_uri")

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    def test_oauth_exchange(self, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/oauth/exchange").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            with _client(with_key=with_key) as client:
                client.oauth.with_raw_response.exchange()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    def test_oauth_logout_endpoint(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/oauth/logout-endpoint").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            with _client(with_key=with_key) as client:
                client.oauth.with_raw_response.logout_endpoint()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    def test_ping_get(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/server/ping").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            with _client(with_key=with_key) as client:
                client.ping.with_raw_response.get()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    def test_other_methods_need_credentials(self, respx_mock: MockRouter) -> None:
        # Without retries, a request sent by mistake fails fast.
        with _client(with_key=False, max_retries=0) as client:
            with pytest.raises(
                TypeError,
                match="Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted",
            ):
                client.users.with_raw_response.me()

        assert not respx_mock.calls


class TestAsyncNoAuthOperations:
    @pytest.mark.respx(base_url=base_url)
    async def test_oauth_auth_url(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/oauth/auth-url").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            async with _async_client(with_key=with_key) as client:
                await client.oauth.with_raw_response.auth_url(redirect_uri="redirect_uri")

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    async def test_oauth_exchange(self, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/api/oauth/exchange").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            async with _async_client(with_key=with_key) as client:
                await client.oauth.with_raw_response.exchange()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    async def test_oauth_logout_endpoint(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/oauth/logout-endpoint").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            async with _async_client(with_key=with_key) as client:
                await client.oauth.with_raw_response.logout_endpoint()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    async def test_ping_get(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/api/server/ping").mock(return_value=httpx.Response(200, json={}))

        for with_key in (False, True):
            async with _async_client(with_key=with_key) as client:
                await client.ping.with_raw_response.get()

        assert _sent_auth_headers(route) == [[], []]

    @pytest.mark.respx(base_url=base_url)
    async def test_other_methods_need_credentials(self, respx_mock: MockRouter) -> None:
        # Without retries, a request sent by mistake fails fast.
        async with _async_client(with_key=False, max_retries=0) as client:
            with pytest.raises(
                TypeError,
                match="Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted",
            ):
                await client.users.with_raw_response.me()

        assert not respx_mock.calls
