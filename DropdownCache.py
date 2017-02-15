from werkzeug.contrib.cache import SimpleCache
import time

class DropdownCache:
    def __init__(self, timeout):
        self.cache_timeout = timeout
        self.dd_cache = SimpleCache()

        self.load_data()

    def load_data(self):
        print 'Updating cache'
        time.sleep(2)
        repos = ['one', 'two', 'three']
        templates = ['a', 'b', 'c']
        self.dd_cache.set('repos', repos, self.cache_timeout)
        self.dd_cache.set('templates', templates, self.cache_timeout)

    def get_repo_data(self):
        return self.dd_cache.get('repos')

    def get_template_data(self):
        return self.dd_cache.get('templates')
