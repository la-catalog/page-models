from unittest import TestCase, main

from pydantic import BaseModel, ValidationError, validator
from pydantic.typing import NoneType

from page_models.validators import val_str


class TestValStr(TestCase):
    def _val_strip_whitespace(self, string: str, strip: bool) -> str:
        class Example(BaseModel):
            string: str
            _string = validator("string", allow_reuse=True)(
                val_str(strip_whitespace=strip)
            )

        return Example(string=string).string

    def test_strip_whitespace(self):
        assert self._val_strip_whitespace(" 1 ", True) == "1"
        assert self._val_strip_whitespace(" 1 ", False) == " 1 "

    def _val_to_lower(self, string: str, to_lower: bool) -> str:
        class Example(BaseModel):
            string: str
            _string = validator("string", allow_reuse=True)(val_str(to_lower=to_lower))

        return Example(string=string).string

    def test_to_lower(self):
        assert self._val_to_lower("abc", to_lower=True) == "abc"
        assert self._val_to_lower("ABC", to_lower=True) == "abc"
        assert self._val_to_lower("abc", to_lower=False) == "abc"
        assert self._val_to_lower("ABC", to_lower=False) == "ABC"

    def _val_to_upper(self, string: str, to_upper: bool) -> str:
        class Example(BaseModel):
            string: str
            _string = validator("string", allow_reuse=True)(val_str(to_upper=to_upper))

        return Example(string=string).string

    def test_to_upper(self):
        assert self._val_to_upper("abc", to_upper=True) == "ABC"
        assert self._val_to_upper("ABC", to_upper=True) == "ABC"
        assert self._val_to_upper("abc", to_upper=False) == "abc"
        assert self._val_to_upper("ABC", to_upper=False) == "ABC"

    def _val_min_length(self, string: str) -> str:
        class Example(BaseModel):
            string: str
            _string = validator("string", allow_reuse=True)(val_str(min_length=5))

        return Example(string=string).string

    def test_min_length(self):
        self.assertRaises(ValidationError, self._val_min_length, "1234")
        assert self._val_min_length("12345") == "12345"

    def _val_max_length(self, string: str) -> str:
        class Example(BaseModel):
            string: str
            _string = validator("string", allow_reuse=True)(val_str(max_length=5))

        return Example(string=string).string

    def test_max_length(self):
        self.assertRaises(ValidationError, self._val_max_length, "123456")
        assert self._val_max_length("12345") == "12345"

    def _val_none_class(self, string: str, ignore_class: tuple = tuple()) -> str:
        class Example(BaseModel):
            string: str = None
            _string = validator("string", allow_reuse=True)(
                val_str(ignore_class=ignore_class)
            )

        return Example(string=string).string

    def test_none_class(self):
        self.assertRaises(ValidationError, self._val_none_class, string=None)
        assert self._val_none_class(string=None, ignore_class=(NoneType,)) == None

    def _val_none_value(self, string: str, ignore_value: tuple = tuple()) -> str:
        class Example(BaseModel):
            string: str = None
            _string = validator("string", allow_reuse=True)(
                val_str(ignore_value=ignore_value)
            )

        return Example(string=string).string

    def test_none_value(self):
        self.assertRaises(ValidationError, self._val_none_value, string=None)
        assert self._val_none_value(string=None, ignore_value=[None]) == None


if __name__ == "__main__":
    main()
