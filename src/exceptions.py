# Это вспомогательный класс, созданный, чтобы выкидывать исключения в едином стиле
# Пример приминения : Exceptions.throw(Exceptions.argument_type)
class Exceptions: #static
    argument_type = "Argument type exception"
    argument = "Argument exception"

    @staticmethod
    def throw(exception):
        raise TypeError(exception + '!')

    @staticmethod
    def throw(exception, message):
        raise TypeError("{}: {}!".format(exception, message))
