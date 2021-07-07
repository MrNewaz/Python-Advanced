def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero")
    return 10 / age


calculate_xfactor(-1)
