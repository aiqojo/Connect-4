from Board import *

def main():

    width = 7
    height = 6

    board = Board(width, height)

    print(board)

    while True:
        value = -1

        print("Red's turn!")
        value = input("Enter column")
        board.add_checker("r", value)
        print(board)

        if board.check_win():
            break

        print("Yellow's turn!")
        value = input("Enter column")
        board.add_checker("y", value)
        print(board)

        if board.check_win():
            break


if __name__ == "__main__":
    main()