from datetime import datetime

from pydantic import Field
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config


@dataclass(config=core_config)
class Metadata(CoreModel):
    """
    Metadata about Query.

    created - When the query was created

    origin - Who triggered the pipeline
    """

    # Datetime fields (UTC time)
    created: datetime = Field(default_factory=datetime.utcnow)

    origin: str = None
