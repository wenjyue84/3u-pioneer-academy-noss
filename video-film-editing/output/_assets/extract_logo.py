import pymupdf
pdf=r'C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\raw\adi-mpc-template-2026-09\core-abilities\Core Abilities Level 1_2_3_4_5\Z-009-3-2015\CA1 EFFECTIVE COMMUNICATION\SUB1 COMMUNICATION LIASION PRACTICE\Kertas Penerangan 1.1.PDF'
d=pymupdf.open(pdf); p=d[0]
# locate the image block on page 1 to clip exactly
for b in p.get_text('dict')['blocks']:
    if b['type']==1: print('image block bbox',b['bbox'])
blocks=[b for b in p.get_text('dict')['blocks'] if b['type']==1]
clip=pymupdf.Rect(blocks[0]['bbox']) if blocks else pymupdf.Rect(90,75,185,210)
p.get_pixmap(dpi=300, clip=clip, alpha=False).save(rf'C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\_assets\jpk-logo-official.png'); print('saved clip',clip)
