class DesviacionEstandar:
    @staticmethod
    def calcular(datos):
        if len(datos) == 0:
            raise ValueError("La lista de datos está vacía.")

        n = len(datos)
        media = sum(datos) / n
        varianza = sum((x - media) ** 2 for x in datos) / n
        return varianza ** 0.5
