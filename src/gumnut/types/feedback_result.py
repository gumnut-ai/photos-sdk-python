# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FeedbackResult"]


class FeedbackResult(BaseModel):
    status: Literal["submitted"]
    """
    Confirmed acceptance for intake only; does not confirm review, spam-filter
    passage, follow-up, an issue, or a fix.
    """
