from pydantic import BaseModel, constr


class Attribute(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    value: constr(min_length=1, strip_whitespace=True)
