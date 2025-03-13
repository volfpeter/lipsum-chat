from pathlib import Path
from typing import Any

from htmy import ComponentType, Properties, PropertyValue, Text, etree, html, md


def _add_css_class(class_: str, properties: dict[str, Any]) -> Properties:
    """Adds a CSS class to the given `Properties` object."""
    properties["class"] = f"{properties.get('class', '')} {class_}"
    return properties


class _styled_components:
    """Conversion rules for some of the HTML tags."""

    @staticmethod
    def h1(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `h1` tags that adds some extra CSS classes to the tag."""
        return html.h1(*children, **_add_css_class("text-xl font-bold pt-2 pb-4", properties))

    @staticmethod
    def h2(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `h2` tags that adds some extra CSS classes to the tag."""
        return html.h2(*children, **_add_css_class("text-lg font-bold py-2", properties))

    @staticmethod
    def h3(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `h3` tags that adds some extra CSS classes to the tag."""
        return html.h3(*children, **_add_css_class("text-lg font-semibold py-1", properties))

    @staticmethod
    def p(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `p` tags that adds some extra CSS classes to the tag."""
        return html.p(*children, **_add_css_class("py-1.5", properties))

    @staticmethod
    def ol(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `ol` tags that adds some extra CSS classes to the tag."""
        return html.ol(*children, **_add_css_class("list-decimal list-inside", properties))

    @staticmethod
    def ul(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `ul` tags that adds some extra CSS classes to the tag."""
        return html.ul(*children, **_add_css_class("list-disc list-inside", properties))

    @staticmethod
    def li(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `li` tags that adds some extra CSS classes to the tag."""
        return html.li(*children, **_add_css_class("py-0.5", properties))

    @staticmethod
    def a(*children: ComponentType, **properties: PropertyValue) -> ComponentType:
        """Rule for converting `a` tags that adds some extra CSS classes to the tag."""
        return html.a(*children, **_add_css_class("link", properties))


_md_converter = etree.ETreeConverter(
    {k: v for k, v in _styled_components.__dict__.items() if not k.startswith("_")}
).convert
"""The conversion function for the `MD` component."""


def markdown(path_or_text: Text | str | Path) -> md.MD:
    """Creates a `MD` component that uses custom styles for certain HTML tags."""
    return md.MD(path_or_text, converter=_md_converter)
