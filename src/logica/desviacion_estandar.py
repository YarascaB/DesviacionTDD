class DesviacionEstandar:
    @staticmethod
    def calcular(datos):
        if len(datos) == 0:
            raise ValueError("La lista de datos está vacía.")

        n = len(datos)
        media = sum(datos) / n

        # Si hay un solo dato, la desviación estándar es 0
        if n == 1:
            return 0.0

        varianza = sum((x - media) ** 2 for x in datos) / n
        return varianza ** 0.5
