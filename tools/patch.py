import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
families = json.load(open('tools/contents_parsed.json', encoding='utf-8'))
patches = {
 '107': {'title': 'Complex Matrix Multiplication Below 2.258 and Rectangular Bounds',
         'link': 'preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf',
         'abstract': 'Over every field of characteristic zero, we prove that the square matrix-multiplication exponent satisfies <i>ω</i> < 2.258, the dual exponent satisfies <i>α</i> > 0.465, and $`\\omega(1,0.709,1)\\lt 2.092`$. The strict square and <i>k</i> = 0.709 rectangular bounds also hold over every field except possibly in one finite set of positive characteristics, in the arithmetic-operation model. (secondary writeup)'},
 '337': {'title': 'Sharp integral fillings in CAT(0) spaces',
         'link': 'preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf',
         'abstract': 'Every compactly supported integral <i>n</i>-cycle, <i>n</i> ≥ 2, in a proper CAT(0) space bounds a compactly supported integral current with the sharp Euclidean mass bound. The theorem allows arbitrary integer multiplicities and unrestricted ambient dimension. In particular, we prove the Euclidean Cartan–Hadamard isoperimetric conjecture in dimensions at least three.'},
}
for f in families:
    if f['num'] in patches:
        p = patches[f['num']]
        f['manuscripts'].append({'title': p['title'], 'link': p['link'], 'abstract': p['abstract']})
        print("patched", f['num'], "-> now", len(f['manuscripts']), "manuscripts")
json.dump(families, open('tools/contents_parsed.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print("total manuscripts:", sum(len(f['manuscripts']) for f in families))
