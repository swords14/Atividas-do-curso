pessoa = {
    "nome": "João",
    "sobrenome": "Silva",
    "idade"; 30,
    "curso": "Engenharia da computação",
    "endereço": "Rua A, número 123, Bairro Y"

    }

    print(pessoa)

    print(pessoa["nome"])
    print(pessoa["sobrenome"])
    print(pessoa["idade"])
    print(pessoa["curso"])
    print(pessoa["endereço"])


    del pessoa["curso"]

    pessoa["sobrenome"] = "Lopes"

    print(pessoa)

    print(pessoa["endereço"])

    pessoa2 = pessoa.copy()
    pessoa2["nome"] = "Maria"
    pessoa2["idade"] = 30

    print(pessoa2)
