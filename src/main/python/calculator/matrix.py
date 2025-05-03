import numpy as np

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber


class Matrix:
    def __init__(self, data):
        """
        Initialise une matrice avec les données fournies sous forme de liste de listes.
        """
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("La matrice doit être une liste de listes.")

        # Vérifie si toutes les lignes ont la même taille
        row_lengths = [len(row) for row in data]
        if len(set(row_lengths)) != 1:
            raise ValueError(
                "Toutes les lignes de la matrice doivent avoir la même taille."
            )

        self.data = data
        self.rows = len(data)  # Nombre de lignes
        self.cols = len(data[0])  # Nombre de colonnes

    def accept(self, visitor):
        visitor.visit_matrix(self)

    def get_depth(self):
        return 2  # Représente une dimension 2D (matrice)

    def get_ops(self):
        return self.rows * self.cols

    def get_nbs(self):
        return self.rows * self.cols

    def __str__(self):
        return str(self.data)

    def _cast_to_appropriate_type(self, value):
        """
        Convertit les valeurs en leur type approprié (Integer, Real, Rational).
        """
        if isinstance(value, IntegerNumber):
            return value
        elif isinstance(value, RealNumber):
            return value
        elif isinstance(value, RationalNumber):
            return value
        else:
            raise ValueError("Unsupported number type")

    def add(self, other):
        # Vérifier si les matrices ont les mêmes dimensions
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                "Les matrices doivent avoir les mêmes dimensions pour l'addition."
            )

        result = []
        for i in range(self.rows):
            row_result = []
            for j in range(self.cols):
                val1 = self.data[i][j]
                val2 = other.data[i][j]
                try:
                    val1 = self._cast_to_appropriate_type(val1)
                    val2 = self._cast_to_appropriate_type(val2)
                except ValueError as e:
                    raise ValueError("Unsupported number type") from e

                result_value = val1.add(val2)
                row_result.append(
                    result_value.get_value()
                )  # Assurer de récupérer la valeur réelle du nombre
            result.append(row_result)

        return Matrix(result)

    def multiply(self, other):
        # Vérifier si les matrices sont compatibles pour la multiplication
        if self.cols != other.rows:
            raise ValueError(
                "Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la seconde matrice."
            )

        result = []
        for i in range(self.rows):
            row_result = []
            for j in range(other.cols):
                product = IntegerNumber(0)
                for k in range(self.cols):
                    val1 = self.data[i][k]
                    val2 = other.data[k][j]
                    product = product.add(
                        self._cast_to_appropriate_type(val1).multiply(
                            self._cast_to_appropriate_type(val2)
                        )
                    )
                row_result.append(
                    product.get_value()
                )  # Assurer de récupérer la valeur réelle du nombre
            result.append(row_result)

        return Matrix(result)

    def transpose(self):
        result = np.transpose(self.data)
        return Matrix(result.tolist())

    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("La matrice doit être carrée pour calculer l'inverse.")
        try:
            result = np.linalg.inv(self.data)
            return Matrix(result.tolist())
        except np.linalg.LinAlgError:
            raise ValueError("La matrice n'est pas inversible.")
