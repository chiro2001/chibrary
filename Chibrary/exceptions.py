class ChibraryException:
    class BaseException(Exception):
        def __init__(self, exception_message=''):
            self.message = exception_message
            self.default_message = ''
            self.my_init()

        def my_init(self):
            # 重写my_init方法可以做到在继承的class里面实现__init__的效果
            pass

        def __str__(self):
            e_type = ''
            if len(self.default_message) != 0:
                e_type = '%s' % self.default_message
            return 'Chibrary Error: ' + e_type + '. ' + self.message

    class ConfigJsonNotFound(BaseException):
        def my_init(self):
            self.default_message = 'config.json not found'

    class ConfigJsonError(BaseException):
        def my_init(self):
            self.default_message = 'config.json error'

    class UserExists(BaseException):
        def my_init(self):
            self.default_message = 'user exists'

    class UserNotFound(BaseException):
        def my_init(self):
            self.default_message = 'user not found'

    class BookExists(BaseException):
        def my_init(self):
            self.default_message = 'Book exists'

    class BookNotFound(BaseException):
        def my_init(self):
            self.default_message = 'Book not found'

    class BookSourceExists(BaseException):
        def my_init(self):
            self.default_message = 'Book source exists'

    class BookSourceNotFound(BaseException):
        def my_init(self):
            self.default_message = 'Book source not found'

    class ArgsError(BaseException):
        def my_init(self):
            self.default_message = 'Args not fit'

    class FileConfigError(BaseException):
        def my_init(self):
            self.default_message = 'You must provide both or neither of data and url'
