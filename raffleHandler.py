from Nike.dailyRaffle import dailyRaffle as nikeRaffle
from Worksout.dailyRaffle import dailyRaffle as worksOutRaffle


class RaffleSwitcher:
    def __init__(self, field):
        """Dispatch method"""
        self.method_name = 'raffle_' + str(field)

    def getFunction(self, data={}):
        print("method_name : ", self.method_name)
        return getattr(self, self.method_name, lambda: "Invalid Field")

    def raffle_nike(self, data):
        return nikeRaffle(data)

    def raffle_worksOut(self, data):
        return worksOutRaffle(data)


def main(event, context):
    try:
        fieldName = event.get("field")
        data = event.get("arguments")
        switcher = RaffleSwitcher(fieldName)
        function = switcher.getFunction(data)
        return function(data)
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        return False
