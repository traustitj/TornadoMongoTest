from CMS import BasicHandler
from tornado.gen import Task
import json
import tornado


class CategoriesHandler(BasicHandler):
    @tornado.gen.engine
    @tornado.web.asynchronous
    def get(self):
        key = self.get_argument("key", None)
        docs = None
        if key:
            docs = None
            if not docs:
                docs = yield Task(self.db.get_categories, key=key)
            else:
                docs = json.loads(docs)
        else:
            docs = None
            if not docs:
                docs = yield Task(self.db.get_categories)
            else:
                docs = json.loads(docs)

        self.set_header("content-type", "application/json")
        self.finish(json.dumps(docs))

