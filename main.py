"""Simple API

This is a working example of a simple api done with
bottle.py and intended to be used as a Google Cloud Run
service.

"""

import sys
import datetime
import bottle
from modules.bottles import BottleJson
import routes.auth
import routes.storage
import routes.example
import models.base
import routes.imagebank

app = BottleJson()

app.mount("/auth", routes.auth.app)
app.mount("/imagebank", routes.imagebank.app)
app.mount("/routes", routes.imagebank.app)


@app.get("/")
def root_index(*args, **kwargs):
    return dict(code=200)

@app.get("/hello")
@app.get("/hello/<name>")
def root_index(*args, name="Mike", **kwargs):
    return dict(code=200, hello="how-are-you") | {"from":name}


if __name__ == '__main__':
    error = False
    if (argv_len := len(sys.argv)) > 1:
        if sys.argv[1] == 'routes':
            for route in app.routes:
                print(route.rule, route.method, route, sep="\t")
        if sys.argv[1] == 'db' and 'migrate' in sys.argv:
            print("Database Migration:")
            now_iso = datetime.datetime.utcnow().isoformat()
            migration_name = now_iso
            models.base.migrate_database(migration_name)
        else:
            error = True
    elif error:
        print("Bad use")
    else:
        app.run(host="0.0.0.0", port=8081)
