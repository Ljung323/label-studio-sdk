# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class Workspace(pydantic_v1.BaseModel):
    id: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Unique ID of the workspace
    """

    title: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Workspace title
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Workspace description
    """

    is_public: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether the workspace is public or not
    """

    is_personal: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether the workspace is personal or not
    """

    is_archived: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether the workspace is archived or not
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Creation time of the workspace
    """

    updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field(default=None)
    """
    Last updated time of the workspace
    """

    created_by: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    User ID of the workspace creator
    """

    color: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Workspace color
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
