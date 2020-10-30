from Exercise_129_Tokenizing_a_String import token_list
from Exercise_130_Unary_and_Binary_Operators import binary
from Exercise_131_Infix_to_Postfiximport inftopost

def evaluetePost(x):

    values = []
    for i in x:
        if '0'<=i<='9':
            a = int(i)
            values.append(a)
        elif i == 'u-':
            a = values[len(values)-1]*(-1)
            values.pop(len(values) - 1)
            values.append(a)
        elif i == "+" or i == "-" or i == "*" or i == "/" or i == "ˆ":
            right = values[len(values)-1]
            values.pop(len(values) - 1)
            left = values[len(values)-1]
            values.pop(len(values) - 1)
            if i == '+':
                r = left + right
            elif i == '-':
                r = left - right
            elif i == '*':
                r = left * right
            elif i == '/':
                r = left / right
            elif i == 'ˆ':
                r = left**right
            values.append(r)

    return values[0]



def main():
    exp = str(input("Inserire un'espressione matematica:"))
    exp = token_list(exp)
    exp = binary(exp)
    exp = inftopost(exp)
    exp = evaluetePost(exp)
    print(exp)

main()
