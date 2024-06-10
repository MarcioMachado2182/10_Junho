livros = [
    {"titulo": "Guia do Mochileiro das Galaxias",  "autor": "Douglas Adamns", "ano de lançamento": "1979", "favorito": "0"},
    {"titulo": "Assassins Creed", "autor": "Oliver Bowden", "ano de lançamento": "2007", "favorito": "0"},
    {"titulo": "Violetas na Janela", "autor": "Zibia Gaspareto", "ano de lançamento": "1993", "favorito": "0" }
]

l_fav = livros[2]

l_fav ["favorito"] = 1

livros[2]= l_fav
print("")
print("")
print (livros[2])


print("")
print("")
for livro in livros:
    if livro["titulo"] == "Guia do Mochileiro das Galaxias":
        livro["favorito"] = 1

print (livros[0])
