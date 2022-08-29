n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
if media >= 7:
    print("""Media: {:.1f}
Aluno aprovado.""".format(media))
elif 5 <= media <= 6.9:
    exam = float(input())
    mfinal = (media + exam) / 2
    if mfinal >= 5:
        print("""Media: {:.1f}
Aluno em exame.
Nota do exame: {:.1f}
Aluno aprovado.
Media final: {:.1f}""".format(media, exam, mfinal))
    else:
        print("""Media: {:.1f}
Aluno em exame.
Nota do exame: {:.1f}
Aluno reprovado.
Media final: {:.1f}""".format(media, exam, mfinal))
else:
    print("""Media: {:.1f}
Aluno reprovado.""".format(media))
