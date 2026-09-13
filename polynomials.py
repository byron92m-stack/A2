from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        coefs = tuple(coefs)
        if not coefs:
            raise ValueError("El polinomio necesita al menos un coeficiente")
        while len(coefs) > 1 and coefs[-1] == 0:
            coefs = coefs[:-1]
        self.coefficients = coefs

    def degree(self):
        """Grado del polinomio. 0 para el polinomio cero."""
        return len(self.coefficients) - 1

    # ---------- Representación ----------

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [
            f"{'' if c == 1 else c}x^{d}"
            for d, c in enumerate(coefs[2:], start=2)
            if c
        ]
        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return f"Polynomial({self.coefficients!r})"

    # ---------- Igualdad ----------

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return NotImplemented
        return self.coefficients == other.coefficients

    # ---------- Aritmética ----------

    def __add__(self, other):
        if isinstance(other, Polynomial):
            n = max(len(self.coefficients), len(other.coefficients))
            a = self.coefficients + (0,) * (n - len(self.coefficients))
            b = other.coefficients + (0,) * (n - len(other.coefficients))
            return Polynomial(tuple(x + y for x, y in zip(a, b)))

        if isinstance(other, Number):
            return Polynomial(
                (self.coefficients[0] + other,) + self.coefficients[1:]
            )

        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)