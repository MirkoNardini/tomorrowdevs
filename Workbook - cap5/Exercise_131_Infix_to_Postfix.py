from Exercise_129_Tokenizing_a_String  import token_list
from Exercise_130_Unary_and_Binary_Operators import binary

def inftopost(x):
    oper = []
    post = []

    for i in x:
        if '0'<= i <= '9':
            post.append(i)
        elif i == "+" or i == "-" or i == "*" or i == "/" or i == "ˆ" or i == "(" or i == ")" or i=='u+' or i=='u-':
            while oper!=[] and oper[len(oper)-1]!= '(' and x[len(x)-2]<oper[len(oper)-2]:
                a = oper[len(oper)-1]
                oper.pop(len(oper)-1)
                post.append(a)
            oper.append(i)
        elif i == '(':
            oper.append(i)
        elif i == ')':
            while oper[len(oper)-1]!='(':
                a = oper[len(oper) - 1]
                oper.pop(len(oper) - 1)
                post.append(a)
            oper.remove('(')

    while oper!= []:
        a = oper[len(oper) - 1]
        oper.pop(len(oper) - 1)
        post.append(a)

    b = 0
    while b < len(post):
        if post[b]=='u-' or post[b] =='u+':
            if  post[b+1]=='*' or post[b]=='/':
                c = post[b]
                post[b] = post[b+1]
                post[b+1] = c
            elif post[b-1]=='ˆ':
                c = post[b]
                post[b] = post[b-1]
                post[b+1] = c
        b = b+1


    return post

def main():
    exp = str(input("Inserire un'espressione matematica:"))
    exp = token_list(exp)
    exp = binary(exp)
    exp = inftopost(exp)
    print(exp)

if __name__ == "__main__":
    main()
