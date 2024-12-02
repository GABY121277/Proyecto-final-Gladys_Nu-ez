import os

f = open("personas.txt", "w")

letrero = "Nombre\tEdad\tCorreo\tTelefono\tDomicilio\n"
Gladys = "Gladys\t18\tgladys.gabriela0901@gmail.com\t5578342450\tCalle 20 de noviembre, La Blanca\n"
Fernanda = "Fernanda\t18\tFer.barra@gmail.com\t9941027213\tAv. Independencia, Santo Domingo Ingenio\n"
Olivia = "Olivia\t19\tOliv.1813@gmail.com\t9712216108\t2 da sección, Juchitán\n"
Emilio = "Emilio\t18\tOliv.1813@gmail.com\t9712216108\t2 da sección, Juchitán\n"
Kevin = "Kevin\t20\tkevin.taquitl@gmail.com\t9712063058\t4 ta sección, Juchitán\n"

f.write(letrero)
f.write(Gladys)
f.write(Fernanda)
f.write(Olivia)
f.write(Emilio)
f.write(Kevin)

f.close()