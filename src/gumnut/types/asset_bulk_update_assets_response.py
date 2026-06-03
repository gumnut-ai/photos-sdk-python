# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetBulkUpdateAssetsResponse"]


class AssetBulkUpdateAssetsResponse(BaseModel):
    """Acknowledgment body for ``POST /api/assets/bulk-update``.

    Empty by design; exists so MCP tools generated from this endpoint have a
    real ``outputSchema``. Distinct from ``DeletionResponse`` because that
    name is purpose-scoped to destructive operations — reusing it on a
    non-destructive endpoint would misname the wire shape in OpenAPI and
    generated SDKs.
    """

    pass
