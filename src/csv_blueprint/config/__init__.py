"""YAML de-serialization classes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ColumnConfig:
    """Configuration for a single column."""

    name: str
    description: str
    rules: dict


@dataclass
class ValidationConfig:
    """CSV Blueprint configuration."""

    name: str
    description: str
    filename_pattern: str
    columns: list[ColumnConfig]
