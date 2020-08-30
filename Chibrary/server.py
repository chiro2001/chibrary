import traceback
from flask import *
from Chibrary import config
from Chibrary.database import *

my_app = Flask(__name__)
db = ChibraryDB()

from Chibrary.utils import *
import Chibrary.user
import Chibrary.book
import Chibrary.bookSource


@my_app.errorhandler(Exception)
def error_handler_500(error):
    traceback.print_exc()
    return make_result(500, message="Caught Exception: %s" % traceback.format_exc()), 500


@my_app.errorhandler(404)
def error_handler_404(error):
    return make_result(404, message="%s" % str(error)), 404


def launch():
    # 建立local和web的书源
    db.source_add('local', 'chiro', '本地书籍。')
    db.source_add('web', 'chiro', '网络资源。')
    my_app.run(config.CHIBRARY_BIND, config.CHIBRARY_PORT, debug=False)
