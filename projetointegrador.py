from tkinter import *

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

def j_estoque():
    janela_estoque.place(width=500, height=500)

def add_prod():
    produto = Produto(codigo, nome, preco, quantidade)
    produto.codigo = codigo.get()
    produto.nome = nome.get()
    produto.preco = preco.get()
    produto.quantidade =quantidade.get()
    estoque.append(produto)
    frase1 = f"Código: {codigo.get}, Nome: {nome.get}, Preço: R${preco.get}, Quantidade: {quantidade.get}"
    print("Produto adicionado com sucesso!")
    janela_estoque.place_forget()
    janela_prodadd.place(width=500, height=500)

def exibir_estoque():
    janela_quantidade.place(width=500, height=500)
    for produto in estoque:
        Label(janela_quantidade, text=f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R${produto.preco}, Quantidade: {produto.quantidade}").pack(pady=20)
        Button(janela_quantidade, text="Ok", command=voltar).pack(pady=20)

    Label(janela_quantidade,text="Não há estoque").pack(pady=20)
    Button(janela_quantidade, text="Ok", command=voltar).pack(pady=20)

def exibir_vendas():
    janela_exibvenda.place(width=500, height=500)
    for venda in vendas:
        Label(janela_exibvenda, text=f"Produto: {venda[0]}, Quantidade: {venda[1]}, Total: R${venda[2]}").pack(pady=20)
        Button(janela_exibvenda, text="Ok", command=voltar).pack(pady=20)

    Label(janela_exibvenda, text="Não há vendas").pack(pady=20)
    Button(janela_exibvenda, text="Ok", command=voltar).pack(pady=20)

def realizar_venda():
    janela_venda.place(width=500, height=500)

def processo_venda():
    for produto in estoque:
        if produto.codigo == codigo_venda.get():
            janela_venda2.place(width=500, height=500)
            return

    janela_nvenda.place(width=500, height=500)
    print("Produto não encontrado!")

def logica_venda():
    for produto in estoque:
        qtde = int(produto.quantidade)
        qtde_v = int(quantidade_venda.get())
        preco_v = float(produto.preco)
        if quantidade_venda.get() <= produto.quantidade:
            qtde -= qtde_v
            valor_total = qtde_v * preco_v
            vendas.append((produto.nome, qtde_v, valor_total))
            janela_vendaok.place(width=500, height=500)
            Label(janela_vendaok, text=f"Venda realizada! Total a pagar: R${valor_total}").pack(pady=20)
            Button(janela_vendaok, text="Ok", command=voltar).pack(pady=5)
        else:
            janela_nquantidade.place(width=500, height=500)

def voltar():
    janela_estoque.place_forget()
    janela_prodadd.place_forget()
    janela_quantidade.place_forget()
    janela_venda.place_forget()
    janela_venda2.place_forget()
    janela_nvenda.place_forget()
    janela_nquantidade.place_forget()
    janela_vendaok.place_forget()
    janela_exibvenda.place_forget()

#Tela Inicial
janela = Tk()
janela.geometry("500x500+500+500")

#Botôes e textos tela inicial
Label(janela, text="Tela Inicial").pack(pady=20)
Label(janela, text="Escolha uma opção:").pack(pady=20)
Button(janela, text="Adicionar Produtos", command=j_estoque).pack(pady=5)
Button(janela, text="Exibir Estoque", command=exibir_estoque).pack(pady=5)
Button(janela, text="Realizar Venda", command=realizar_venda).pack(pady=5)
Button(janela, text="Exibir Vendas", command=exibir_vendas).pack(pady=5)
Button(janela, text="SAIR", command=janela.destroy).pack(padx=10, pady=10)

#Campos
estoque = []
vendas = []

#Tela Adicionar Produtos
janela_estoque = Frame(janela)
janela_estoque.place_forget()
Label(janela_estoque, text="Insira as informações do produto a ser adicionado").pack(pady=20)
Label(janela_estoque, text="Código:").pack(pady=5)
codigo = Entry(janela_estoque, text="", font=(8), width=15)
codigo.place(relx=0.5, rely=0.20, anchor=CENTER)
Label(janela_estoque, text="Nome:").pack(pady=25)
nome = Entry(janela_estoque, text="", font=(8), width=15)
nome.place(relx=0.5, rely=0.30, anchor=CENTER)
Label(janela_estoque, text="Preço").pack(pady=5)
preco = Entry(janela_estoque, text="", font=(8), width=15)
preco.place(relx=0.5, rely=0.40, anchor=CENTER)
Label(janela_estoque, text="Quantidade no Estoque").pack(pady=25)
quantidade = Entry(janela_estoque, text="", font=(8), width=15)
quantidade.place(relx=0.5, rely=0.50, anchor=CENTER)
Button(janela_estoque, text="Adicionar", command=add_prod).pack(pady=10)

#Tela Confirmação de Adição de Produtos
janela_prodadd = Frame(janela)
janela_prodadd.place_forget()
Label(janela_prodadd, text="Produto Adicionado com Sucesso").pack(pady=20)
Button(janela_prodadd, text="Ok", command=voltar).pack(pady=5)

#Tela de Exibição do Estoque
janela_quantidade = Frame(janela)
janela_quantidade.place_forget()
Label(janela_quantidade, text="Estoque de Produtos").pack(pady=5)

#Tela de Venda
janela_venda = Frame(janela)
janela_venda.place_forget()
Label(janela_venda, text="Realizar Venda").pack(pady=20)
Label(janela_venda, text="Digite o código do produto a ser vendido: ").pack(pady=20)
codigo_venda = Entry(janela_venda, text="", font=(8), width=10)
codigo_venda.place(relx=0.5, rely=0.30, anchor=CENTER)
Button(janela_venda, text="Confirmar", command=processo_venda).pack(pady=50)

#Tela de Confirmação de Venda
janela_venda2 = Frame(janela)
janela_venda2.place_forget()
Label(janela_venda2, text="Confirmação da Venda de Produtos").pack(pady=20)
Label(janela_venda2, text="Digite a quantidade a ser vendida: ").pack(pady=10)
quantidade_venda = Entry(janela_venda2, text="", font=(8), width=15)
quantidade_venda.place(relx=0.5, rely=0.25, anchor=CENTER)
Button(janela_venda2, text="Confirmar Quantidade", command=logica_venda).pack(pady=50)

#Tela de Falha na Localização da Compra
janela_nvenda = Frame(janela)
janela_nvenda.place_forget()
Label(janela_nvenda, text="Produto não Encontrado").pack(pady=20)
Button(janela_nvenda, text="Ok", command=voltar).pack(pady=5)

#Tela Quantidade insuficiente
janela_nquantidade = Frame(janela)
janela_nquantidade.place_forget()
Label(janela_nquantidade, text="Quantidade insuficiente em estoque!").pack(pady=20)
Button(janela_nquantidade, text="Ok", command=voltar).pack(pady=5)

#Tela Venda OK
janela_vendaok = Frame(janela)
janela_vendaok.place_forget()

#Tela Exibir Vendas
janela_exibvenda = Frame(janela)
janela_exibvenda.place_forget()


janela.mainloop()
