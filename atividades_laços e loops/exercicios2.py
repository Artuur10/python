#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
#ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.



nome = input("informe seu nome: ")
senha =input("informe a senha: ")

while senha == nome:
    print("sua senha deve ser diferente do seu nome")
    senha = input("informe a senha: ")
print("informaçoes ok")