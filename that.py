s = """Gur Znkvzf bs Rdhvgl, ol gur Pbhegf bs Punaprel

Rdhvgl jvyy abg fhssre n jebat gb or jvgubhg n erzrql.
Rdhvgl sbyybjf gur ynj.
Ur jub frrxf rdhvgl zhfg qb rdhvgl.
Ub jub pbzrf gb rdhvgl zhfg pbzr jvgu pyrna unaqf.
Qrynl qrsrngf rdhvgl.
Rdhnyvgl vf rdhvgl.
Rdhvgl ybbxf gb gur vagrag engure guna gur sbez.
Rdhvgl ybbxf ba gung nf qbar juvpu bhtug gb unir orra qbar.
Rdhvgl vzchgrf na vagragvba gb shysvy na boyvtngvba.
Rdhvgl npgf va crefbanz.
Jurer gur rdhvgvrf ner rdhny, gur svefg va gvzr cerinvyf.
Jurer gur rdhvgvrf ner rdhny, gur ynj cerinvyf."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
