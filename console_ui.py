class console_ui:
    __menu = """
             ===== Main Menu =====\n
             1. Get current values"
             2. Sort

             """

    def __init__(self):
        pass

    def getMenuSelection(self):
        print(self.__menu)
        selection = input("Choose a menu option: ")
        return selection