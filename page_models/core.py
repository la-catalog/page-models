import json
from dataclasses import asdict

from pydantic import ConfigDict, Extra
from pydantic.json import pydantic_encoder

core_config = ConfigDict(extra=Extra.forbid)


class CoreModel:
    def json(
        self,
        *,
        skipkeys=False,
        ensure_ascii=True,
        check_circular=True,
        allow_nan=True,
        cls=None,
        indent=None,
        separators=None,
        sort_keys=False
    ) -> str:
        return json.dumps(
            self,
            skipkeys=skipkeys,
            ensure_ascii=ensure_ascii,
            check_circular=check_circular,
            allow_nan=allow_nan,
            cls=cls,
            indent=indent,
            separators=separators,
            default=pydantic_encoder,
            sort_keys=sort_keys,
        )

    def dict(self) -> dict:
        return asdict(self)
