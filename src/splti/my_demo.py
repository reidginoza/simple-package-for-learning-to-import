import splpp

N = 10
LOW = -10
HIGH = 10


def get_important_stuff() -> list[int]:
    return splpp.rand_ints_via_np(N, LOW, HIGH)


def my_demo() -> None:
    res = get_important_stuff()
    print(res)


if __name__ == "__main__":
    my_demo()
