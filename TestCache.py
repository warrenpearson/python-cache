from DropdownCache import DropdownCache
import time


def check_cache(cache):
    if cache.get_repo_data() is None:
        cache.load_data()

    data = cache.get_repo_data()
    print data
    data = cache.get_template_data()
    print data

dd_cache = DropdownCache(3)

check_cache(dd_cache)
time.sleep(1)
check_cache(dd_cache)
time.sleep(4)
check_cache(dd_cache)
