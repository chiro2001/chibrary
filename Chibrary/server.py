from flask import *
# from Chibrary.config import *
from Chibrary.database import *

my_app = Flask(__name__)
db = ChibraryDB()

import Chibrary.user
import Chibrary.book
import Chibrary.bookSource


def launch():
    my_app.run(CHIBRARY_BIND, CHIBRARY_PORT, debug=False)
