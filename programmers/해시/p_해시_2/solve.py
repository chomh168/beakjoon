def solution(phone_book):
    phone_book.sort()
    answer = check(phone_book)
    return answer

def check(phone_book):
    for i, _ in enumerate(phone_book):
        if i == len(phone_book) - 1:
            break
        check = -1
        try:
            check = phone_book[i+1].index(phone_book[i])
        except:
            pass
        if check == 0:
            return False
    return True
