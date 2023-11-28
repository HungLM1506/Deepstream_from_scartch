import platform


def is_aarch_64():
    if platform.uname()[4] == 'aarch_64':
        return True
    else:
        return platform.uname()[4]


# check = is_aarch_64()
# print(check)s
