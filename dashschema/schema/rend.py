from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Palette(BaseModel):
    text_color: str = Field(..., description="Color of the text")
    background_color: str = Field(..., description="Color of the background")
    link_color: str = Field(..., description="Color of the links")
    chart_colors: List[str] = Field(..., description="List of colors in the palette")


class Layout(BaseModel):
    columns: int = Field(description="Number of columns in the dashboard", default=24)
    width: int = Field(..., description="Pixel Width of the dashboard")
    align: str = Field(description="Alignment of the dashboard", default="center")
    widget_columns: int = Field(
        description="Number of columns in the dashboard", default=12
    )
    widget_rows: int = Field(description="Number of rows in the dashboard", default=6)


class RenderConfig(BaseModel):
    font: str = Field(..., description="Font to use")
    layout: Layout = Field(..., description="Layout of the dashboard")
    palette: Optional[Palette] = Field(
        description="Palette to use for the dashboard", default=None
    )