def norm(x1, x2, norm_type = "L1", verbose=True):
    result = None
    if norm_type == "L1": result = abs(x1) + abs(x2)
    elif norm_type == "L2": result = (x1**2 + x2**2)**0.5
    elif verbose: print("Norm not known: ", norm_type)

    if verbose: print(f"The {norm_type} norm of", [x1, x2], "is:", result)
    return result

norm(3,4)                                       
norm(3,4,"L2")
norm(3,4, norm_type="L2")
norm(3,4, verbose=False)
norm(3,4, verbose=True, norm_type="L1")
norm(x2=3, x1=4, verbose=True, norm_type="L1")