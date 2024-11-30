import streamlit as st

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para solicitar as notas
def solicitar_notas(disciplina, bimestres):
    notas = []
    for bimestre in bimestres:
        nota = st.number_input(f"Digite a nota de {disciplina} do {bimestre}º bimestre:", key=f"{disciplina}-{bimestre}")
        notas.append(nota)
    return notas

# Função para calcular a média global e determinar a situação do aluno
def calcular_media_global(notas_dict, oferta):
    # Calcular médias
    MM = calcular_media(notas_dict["matematica"])
    MP = calcular_media(notas_dict["portugues"])
    MEDF = calcular_media(notas_dict["educacao_fisica"])

    if oferta == 'B':
        # Oferta B, Primeiro Semestre
        MB = calcular_media(notas_dict["biologia"])
        MQ = calcular_media(notas_dict["quimica"])
        MF = calcular_media(notas_dict["fisica"])
        MCN = calcular_media([MB, MQ, MF])

        MFI = calcular_media(notas_dict["filosofia"])
        MS = calcular_media(notas_dict["sociologia"])
        MG = calcular_media(notas_dict["geografia"])
        MH = calcular_media(notas_dict["historia"])
        MCH = calcular_media([MFI, MS, MG, MH])

        ME = calcular_media(notas_dict["espanhol"])
        MA = calcular_media(notas_dict["arte"])
        MI = calcular_media(notas_dict["ingles"])
        MLG = calcular_media([MEDF, ME, MI, MA])
    else:
        # Oferta A, Primeiro Semestre
        MB = calcular_media(notas_dict["biologia"])
        MQ = calcular_media(notas_dict["quimica"])
        MF = calcular_media(notas_dict["fisica"])
        MCN = calcular_media([MB, MQ, MF])

        MFI = calcular_media(notas_dict["filosofia"])
        MS = calcular_media(notas_dict["sociologia"])
        MG = calcular_media(notas_dict["geografia"])
        MH = calcular_media(notas_dict["historia"])
        MCH = calcular_media([MFI, MS, MG, MH])

        ME = calcular_media(notas_dict["espanhol"])
        MA = calcular_media(notas_dict["arte"])
        MI = calcular_media(notas_dict["ingles"])
        MLG = calcular_media([MEDF, ME, MI, MA])

    media_global = calcular_media([MM, MP, MCH, MCN, MLG])

    disciplinas_recuperacao = []
    if MM < 5:
        disciplinas_recuperacao.append("Matemática")
    if MP < 5:
        disciplinas_recuperacao.append("Português")
    if MCH < 5:
        disciplinas_recuperacao.append("Ciências Humanas")
    if MCN < 5:
        disciplinas_recuperacao.append("Ciências da Natureza")
    if MLG < 5:
        disciplinas_recuperacao.append("Linguagens")

    if media_global >= 5:
        st.write(f"A Média Global do aluno é: {media_global:.2f}")
        st.write("Aluno aprovado!")
    elif len(disciplinas_recuperacao) <= 3:
        st.write(f"A Média Global do aluno é: {media_global:.2f}")
        st.write("Aluno em recuperação nas seguintes disciplinas:")
        st.write(", ".join(disciplinas_recuperacao))
    else:
        st.write(f"A Média Global do aluno é: {media_global:.2f}")
        st.write("Aluno reprovado.")

# Interface do Streamlit
st.title("Calculadora de Média Global")

# Escolha da oferta
oferta = st.selectbox("Escolha a oferta:", ["A", "B"])

# Inserção das notas
notas_dict = {
    "matematica": solicitar_notas("Matemática", [1, 2, 3, 4]),
    "portugues": solicitar_notas("Português", [1, 2, 3, 4]),
    "educacao_fisica": solicitar_notas("Educação Física", [1, 2, 3, 4]),
    "biologia": solicitar_notas("Biologia", [3, 4]) if oferta == 'A' else solicitar_notas("Biologia", [1, 2]),
    "quimica": solicitar_notas("Química", [3, 4]) if oferta == 'A' else solicitar_notas("Química", [1, 2]),
    "fisica": solicitar_notas("Física", [3, 4]) if oferta == 'A' else solicitar_notas("Física", [1, 2]),
    "filosofia": solicitar_notas("Filosofia", [1, 2]) if oferta == 'A' else solicitar_notas("Filosofia", [3, 4]),
    "sociologia": solicitar_notas("Sociologia", [1, 2]) if oferta == 'A' else solicitar_notas("Sociologia", [3, 4]),
    "geografia": solicitar_notas("Geografia", [1, 2]) if oferta == 'A' else solicitar_notas("Geografia", [3, 4]),
    "historia": solicitar_notas("História", [1, 2]) if oferta == 'A' else solicitar_notas("História", [3, 4]),
    "espanhol": solicitar_notas("Espanhol", [3, 4]),
    "arte": solicitar_notas("Arte", [3, 4]),
    "ingles": solicitar_notas("Inglês", [1, 2]),
}

# Botão para calcular a média global
if st.button("Calcular Média Global"):
    calcular_media_global(notas_dict, oferta)
