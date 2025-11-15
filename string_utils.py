def split_before_each_uppercases(formula):
    new_list = []
    prev_upper = 0
    if formula != "":
       for i in range(1,len(formula)):
           if formula[i].isupper():
              new_list.append(formula[prev_upper:i])
              prev_upper = i
       new_list.append(formula[prev_upper:len(formula)])
    return new_list


def split_at_first_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
          return (formula[:i:], int(formula[i::]))
    return (formula, 1)
