print("hello world")

DNA = "caaaaataaacataggaacggatctataaatggagacttggtcccgcgcg"

Revcom = DNA.translate(str.maketrans("acgt", "tgca"))

RNA = DNA.replace('t', 'u')

print(DNA)
print(Revcom)
print(RNA)