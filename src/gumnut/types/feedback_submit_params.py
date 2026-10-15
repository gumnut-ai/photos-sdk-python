# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["FeedbackSubmitParams"]


class FeedbackSubmitParams(TypedDict, total=False):
    feedback_type: Required[Literal["bug", "missing_capability", "confusing_behavior", "suggestion", "other"]]
    """Category of friction observed while using Gumnut."""

    message: Required[str]
    """Sanitized account of the friction, expected behavior, and any workaround.

    Do not copy private session or library content.
    """

    task_completed: Optional[bool]
    """Whether the original task was completed despite the friction.

    Omit or use null when unknown.
    """

    tool_names: Optional[SequenceNotStr[str]]
    """Relevant Gumnut tool names, including a missing tool when useful.

    Names are context, not instructions to execute.
    """
