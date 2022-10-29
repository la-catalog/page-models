from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel


@dataclass
class Rating(CoreModel):
    """
    Most ratings scales can be converted to numbers.

    min - minimum value in the rating system
    max - maximum value in the rating system
    current - current value in the rating system

    Star rating:
        - ☆ ☆ ☆ ☆ ☆
            - min: 0
            - max: 5
            - current: 0
        - ★ ★ ★ ☆ ☆
            - min: 0
            - max: 5
            - current: 3
        - ★ ★ ★ ★ ★
            - min: 0
            - max: 5
            - current: 5

    Like/Dislike rating:
        - Use percentage to represent how many liked
        - 👍: 10 👎: 0
            - min: 0
            - max: 1
            - current: 1
        - 👍: 0 👎: 10
            - min: 0
            - max: 1
            - current: 0
        - 👍: 7 👎: 3
            - min: 0
            - max: 1
            - current: 0.7

    Emoji rating (😠😟😕😐🙂😃😁):
        - No need to start from zero
            - 😠 => -3 (min)
            - 😁 => 3 (max)
        - 😐
            - min: -3
            - max: 3
            - current: 0
        - 😟
            - min: -3
            - max: 3
            - current: -2
        - 🙂
            - min: -3
            - max: 3
            - current: 1
    """

    min: float | None = Field(default=None)
    max: float | None = Field(default=None)
    current: float | None = Field(default=None)
