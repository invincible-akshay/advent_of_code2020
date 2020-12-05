import utils.fileutils as futils

REQUIRED_SET = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_HCL_CHARSET = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     'a', 'b', 'c', 'd', 'e', 'f'}
VALID_ECL_CHARSET = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_passport(data):
    row_count = 0
    tmp_set = set()
    invalid_flag = False
    res_count = 0
    while row_count < len(data):
        line = data[row_count]
        if line == "":
            diff_set = REQUIRED_SET - tmp_set
            if len(diff_set) == 0 and not invalid_flag:
                res_count += 1
            tmp_set = set()
            invalid_flag = False
        else:
            if not invalid_flag:
                for kv in line.split():
                    split_vals = kv.split(":")
                    tmp_set.add(split_vals[0])
                    if not validate_kv(split_vals[0], split_vals[1]):
                        invalid_flag = True

        row_count += 1

    if not invalid_flag:
        diff_set = REQUIRED_SET - tmp_set
        if len(diff_set) == 0:
            res_count += 1
    return res_count


def validate_kv(k, v):
    if k not in REQUIRED_SET:
        return True
    elif k == "byr":
        return validate_num_in_range(v, 1920, 2002)
    elif k == "iyr":
        return validate_num_in_range(v, 2010, 2020)
    elif k == "eyr":
        return validate_num_in_range(v, 2020, 2030)
    elif k == "hgt":
        if len(v) < 3:
            return False
        if v[-2:] == "cm":
            return validate_num_in_range(v[:-2], 150, 193)
        elif v[-2:] == "in":
            return validate_num_in_range(v[:-2], 59, 76)
        else:
            return False
    elif k == "hcl":
        if len(v) == 7 and v[0] == "#":
            for ch in v[1:]:
                if ch not in VALID_HCL_CHARSET:
                    return False
        else:
            return False
    elif k == "ecl":
        if v not in VALID_ECL_CHARSET:
            return False
    elif k == "pid":
        if len(v) != 9:
            return False
        return validate_num_in_range(v, 0, 999999999)
    else:
        print("IMPOSSIBLE")
    return True


def validate_num_in_range(num, low, high):
    try:
        tmp = int(num)
        if tmp < low or tmp > high:
            return False
    except Exception as e:
        return False

    return True


inp = futils.read_list("../data/day4.txt")
print("{0} valid passports".format(validate_passport(inp)))
