from flask import *
from Chibrary.config import *
from Chibrary.database import *

app = Flask(__name__)
db = ChibraryDB()

import Chibrary.user


def launch():
    app.run(CHIBRARY_BIND, CHIBRARY_PORT, debug=False)
