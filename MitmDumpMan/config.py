from environs import Env
from typing import AnyStr, List, Dict

env = Env()

# Filter URL
ResourceList: Dict = env.dict('URLS', {
    "xiaohongshu": "xiaohongshu.com/api/sns/v10/search/notes"
})

# Search key word List
KeyWord: List[AnyStr] = env.list('KeyWord', [])
