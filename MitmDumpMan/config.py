from environs import Env
from typing import AnyStr, List

env = Env()

# Filter URL
FilterURLS: List[AnyStr] = env.list('URLS', [])

# Search key word List
KeyWord: List[AnyStr] = env.list('KeyWord', [])
