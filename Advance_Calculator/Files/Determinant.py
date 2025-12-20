def Det():
    Size_Of_Matrix = int(input("What Is x by x Size Of Matrix ---> "))

    for Row in range(Size_Of_Matrix):
        for Col in range(Size_Of_Matrix):
            print(f"  a|{Row+1}x{Col+1}  ", end=" ")
        print("")

    Matrix = []

    for Row in range(Size_Of_Matrix):
        Row_Val = []
        for Col in range(Size_Of_Matrix):
            Val = float(input(f"Value Of a|{Row+1}x{Col+1} ---> "))
            Row_Val.append(Val)
        Matrix.append(Row_Val)

    for Row in range(Size_Of_Matrix):
        for Col in range(Size_Of_Matrix):
            print(f"{Matrix[Row][Col]:6}", end=" ")
        print()

    def Determinant(Mat):
        n = len(Mat)

        if n == 1:
            return Mat[0][0]

        if n == 2:
            return Mat[0][0] * Mat[1][1] - Mat[0][1] * Mat[1][0]

        det = 0
        for col in range(n):
            Minor = []
            for i in range(1, n):
                row = []
                for j in range(n):
                    if j != col:
                        row.append(Mat[i][j])
                Minor.append(row)
            det += ((-1) ** col) * Mat[0][col] * Determinant(Minor)

        return det

    Det_Value = Determinant(Matrix)
    print(f"Determinant Value ---> {Det_Value}")
