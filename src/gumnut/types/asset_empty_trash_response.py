# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetEmptyTrashResponse"]


class AssetEmptyTrashResponse(BaseModel):
    """
    Acknowledgment body returned by destructive endpoints (delete / trash / restore /
    permanently delete / remove-from-album / empty-trash).

    Carries no fields — the HTTP 200 + empty JSON object is itself the success
    signal. Exists so MCP tools generated from these endpoints have a real
    ``outputSchema`` (rather than the null schema FastMCP emits for 204
    responses), which ChatGPT's MCP submission tooling requires.
    """

    pass
