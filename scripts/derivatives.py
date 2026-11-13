"""Derivative settings for the Pellow River Postcards access copies."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Derivative:
    width_px: int
    format: str
    quality: int


ACCESS = Derivative(width_px=1600, format="JPEG", quality=82)
THUMBNAIL = Derivative(width_px=400, format="JPEG", quality=70)


def targets() -> list[Derivative]:
    return [ACCESS, THUMBNAIL]
