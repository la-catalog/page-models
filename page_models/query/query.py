from pydantic import Field, validator
from pydantic.dataclasses import dataclass

from page_models.core import CoreModel, core_config
from page_models.query.metadata import Metadata
from page_models.validators import val_str


@dataclass(config=core_config)
class Query(CoreModel):
    """
    A page query.

    query - String searched in the marketplace
    metadata - Data that provides information about the query
    """

    query: str
    metadata: Metadata = Field()

    _query = validator("query", allow_reuse=True)(
        val_str(strip_whitespace=True, to_lower=True, min_length=1)
    )
