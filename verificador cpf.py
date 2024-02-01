def mult_cpf(cpf, number):
    result_mult = []

    for digit in cpf:
        if number == 1: break

        mult = int(digit) * number
        result_mult.append(mult)
        number -= 1

    return result_mult



def sum_cpf(mults):
    Sum = 0

    for number in mults:
        Sum += number

    return Sum



def get_last_digits(sum):
    mult = sum * 10
    rest_div = mult % 11

   
    last_digit = 0 if rest_div > 9 else rest_div

    return str(last_digit)



def format_cpf(cpf):
    cpf_formated = "{}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    return cpf_formated



while True:
    cpf = input("Insira o cpf: ")
   
    if not cpf.isdigit():
        print("Insira apenas números, sem sinais ou letras!!")
        continue
    elif len(cpf) != 11:
        print("Quantidade de números insuficiente, certifique se digitou corretamente")
        continue



    mult1 = mult_cpf(cpf, 10)
    mult2 = mult_cpf(cpf, 11)

    sum1 = sum_cpf(mult1)
    sum2 = sum_cpf(mult2)

    digit1 = get_last_digits(sum1)
    digit2 = get_last_digits(sum2)

    cpf_formated = format_cpf(cpf)



    if digit1 == cpf[9] and digit2 == cpf[10]:
        print(f"o cpf {cpf_formated} é verídico")
    else:
        print(f"o cpf {cpf_formated} não é verídico")



    question = input("Deseja verificar mais algum cpf? (S/N) ").lower()

    if question == 'n': break