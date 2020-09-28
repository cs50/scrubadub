import os
import hashlib

from typing import Optional, ClassVar, Sequence, List

from ...filth import Filth
from ..base import PostProcessor


class PrefixSuffixReplacer(PostProcessor):
    name = 'prefix_suffix_replacer'  # type: str

    def __init__(self, prefix: Optional[str] = None, suffix: Optional[str] = None, name: Optional[str] = None):
        super(PrefixSuffixReplacer, self).__init__(name=name)

        self.prefix = prefix or '{{'
        self.suffix = suffix or '}}'

    def process_filth(self, filth_list: Sequence[Filth]) -> Sequence[Filth]:
        for filth_item in filth_list:
            if filth_item.replacement_string is None:
                filth_item.replacement_string = filth_item.type.upper()

            if self.prefix is not None and self.suffix is not None:
                filth_item.replacement_string = self.prefix + filth_item.replacement_string + self.suffix
            elif self.prefix is not None:
                filth_item.replacement_string = self.prefix + filth_item.replacement_string
            elif self.suffix is not None:
                filth_item.replacement_string = filth_item.replacement_string + self.suffix

        return filth_list
