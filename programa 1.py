
agua_inicial=int(input("¿cuanta agua inicial habia?: "))
def agua_dividida():
    n_generacion=int(input("¿Que generacion es?: "))
    if n_generacion < 0 or n_generacion >50:
        return "Error: El número de generación debe estar entre 0 y 50."
    organismos= 2** n_generacion
    agua_por_organismo=agua_inicial/organismos
    
    return agua_por_organismo

agua_final=agua_dividida()
print(f"La cantidad de agua que tiene cada organizmo es:", agua_final)

