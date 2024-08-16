#!/usr/bin/python3

import markdown
from typing import Any

def register_hooks(lste: Any) -> None:
    """
    Registers hooks for processing content before loading custom functions.

    Args:
        lste: An object that supports hook registration, which will call `enable_excerpts_markdown`
              when the 'excerpts' hook is triggered.
    """
    lste.hooks.add('excerpt', enable_excerpts_markdown)

def enable_excerpts_markdown(excerpt: str) -> str:
    """
    Updates the excerpt to generate HTML from markdown

    Args:
        content (str): The HTML content to be modified.
        file (str): The filename to look up meta information.
        lste: An object containing the content dictionary with meta fields. 

    Returns:
        str: The updated HTML excerpt.
    """
    excerpt = markdown.markdown(excerpt, extensions=['fenced_code', 'tables'])
    return excerpt
