class player:

    def __init__(self, color):
        self.color = color


    def answer(self, arr, board, zobrist):
        value = -1

        print(arr)

        while not value in arr:
            imput = input("Enter column: ")
            print(imput)
            value = int(imput)
            print(value)

        return value