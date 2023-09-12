def compactar_sequencia(sequencia):
    mapeamento = {"A": "00", "C": "01", "G": "10", "T": "11"}
    sequencia_binaria = "".join(
        [mapeamento.get(nucleotideo, "?") for nucleotideo in sequencia])

    zeros_adicionados = 8 - len(sequencia_binaria) % 8

    sequencia_binaria = sequencia_binaria + "0" * zeros_adicionados

    zeros_adicionados_binario = format(zeros_adicionados, "08b")

    sequencia_binaria = zeros_adicionados_binario + sequencia_binaria

    return sequencia_binaria


def descompactar_sequencia(sequencia_binaria):
    zeros_adicionados = int(sequencia_binaria[:8], 2)
    sequencia_binaria = sequencia_binaria[8:]
    if zeros_adicionados > 0:
        sequencia_binaria = sequencia_binaria[:-zeros_adicionados]

    sequencia = []

    for i in range(0, len(sequencia_binaria), 2):
        nucleotideo_binario = sequencia_binaria[i:i+2]

        mapeamento_inverso = {"00": "A", "01": "C", "10": "G", "11": "T"}

        nucleotideo = mapeamento_inverso.get(nucleotideo_binario)
        if nucleotideo is not None:
            sequencia.append(nucleotideo)

    sequencia = "".join(sequencia)

    return sequencia


def salvar_em_arquivo(sequencia_binaria, nome_arquivo):
    bytes_sequencia = bytearray()
    for i in range(0, len(sequencia_binaria), 8):
        byte = sequencia_binaria[i:i+8]
        bytes_sequencia.append(int(byte, 2))

    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(bytes_sequencia)


def ler_sequencia_de_arquivo(nome_arquivo):
    with open(nome_arquivo, "rb") as arquivo:
        bytes_sequencia = arquivo.read()

    sequencia_binaria = "".join(format(byte, "08b")
                                for byte in bytes_sequencia)

    sequencia = descompactar_sequencia(sequencia_binaria)

    return sequencia


nome_arquivo_txt = "sequencia.txt"
with open(nome_arquivo_txt, "r") as arquivo:
    sequencia_original = arquivo.read().strip()

sequencia_compactada = compactar_sequencia(sequencia_original)

nome_arquivo_bin = "sequencia_compactada.bin"
salvar_em_arquivo(sequencia_compactada, nome_arquivo_bin)

sequencia_lida = ler_sequencia_de_arquivo(nome_arquivo_bin)

print(f"Sequência Original: {sequencia_original}")
print(f"Sequência Compactada: {sequencia_compactada}")
print(f"Sequência Lida: {sequencia_lida}")
