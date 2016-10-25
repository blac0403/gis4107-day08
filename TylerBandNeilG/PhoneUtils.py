def main():
    test_isValidPhoneNumber()

def isValidPhoneNumber(phoneNumber):
    "Is each chunk around - a number?"
    if len(phoneNumber) == 12:
        if phoneNumber[0:3].isdigit():
            if phoneNumber[4:7].isdigit():
                if phoneNumber[8:12].isdigit():
                    if phoneNumber[3] =='-':
                        if phoneNumber[7]== '-':
                            return True

    return False

def test_isValidPhoneNumber():
    print isValidPhoneNumber("999-999-9999")

if __name__ == '__main__':
    main()