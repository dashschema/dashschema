from typing import Literal
from pydantic import BaseModel, Field

from .base import BaseWidget


class TitleWidget(BaseWidget):
    type: Literal["title"]

    @classmethod
    def widget_name(cls):
        return "Title"

    @classmethod
    def examples(cls):
        return [ cls(type="title", title="Title Text") ]


class DescriptionWidget(BaseWidget):
    type: Literal["description"]

    @classmethod
    def widget_name(cls):
        return "Description"

    @classmethod
    def examples(cls):
        return [cls(type="description", description="Some description text")]


class HorizontalRulerWidget(BaseWidget):
    type: Literal["horizontal-ruler"]

    @classmethod
    def widget_name(cls):
        return "Horizontal ruler"

    @classmethod
    def examples(cls):
        return [ cls(type="horizontal-ruler") ]


class VerticalRulerWidget(BaseWidget):
    type: Literal["vertical-ruler"]

    @classmethod
    def widget_name(cls):
        return "Vertical ruler"

    @classmethod
    def examples(cls):
        return [ cls(type="vertical-ruler") ]