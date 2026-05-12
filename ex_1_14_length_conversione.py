x=float(input(" inserire il numero di metri   "))
# print(x)
""" ni = numero di inchs ovvero quanti pollici corrispondopno ad x metri

    nf =n. piedi (foot) ovvero quanti piedi corrispondopno ad x metri

    ny = n. yarde ovvero quante yarde  corrispondopno ad x metri

    nm= n. miglia ovvero quante miglia  corrispondopno ad x metri

    """
ni=x/0.0254
nf=ni/12
ny=nf/3
nm=ny/1760
print( "ni=%.2f, nf=%.2f, ny=%.2f,nm=%.2f" %(ni, nf, ny, nm))
