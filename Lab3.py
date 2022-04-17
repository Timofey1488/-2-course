import numpy
numpy.random.seed(42)

print("Nonlinear equations \n")

EPS = 10.0 ** -5

def input():
    # expr = numpy.poly1d([1.0, 1.0, 0.0])
    # expr = numpy.poly1d(numpy.poly([1.0, 2.0, 3.0]))
    # expr = numpy.poly1d(numpy.poly([1.0, 1.0, 1.0]))
    # expr = numpy.poly1d(numpy.poly([0.0, 0.0, 1.0]))
    expr = numpy.poly1d([1.0, -6.4951, -31.2543, 23.1782])

    # expr = numpy.poly1d([1.0, -6.4951, -31.2543, 23.1782])
    return (expr)

(f) = input()
print(f)


def SturmSeq(f):
    arr = []
    arr.append(f)
    arr.append(numpy.polyder(f))

    while True:
        fn = -numpy.polydiv(arr[-2], arr[-1])[1]
        if (fn.order > 0 or abs(fn[0]) > 0.0):
            arr.append(fn)
        else:
            break
    
    return arr

def N(stseq, x):
    if (abs(f(x)) < EPS):
        raise ValueError("Number in N() is a root")
    ans = 0
    for i in range(1, len(stseq)):
        if (stseq[i](x) == 0.0):
            raise ValueError("SturmSeq[i] is zero")
        if(stseq[i-1](x) * stseq[i](x) < 0):
            ans += 1
    return ans

def GetBounds(f, a, b):
    if ((abs(f(a)) < EPS) or (abs(f(b)) < EPS)):
        raise ValueError("Bounds contain root")
    if (N(Sturm, a) - N(Sturm, b) == 0):
        return []
    if (N(Sturm, a) - N(Sturm, b) > 1):
        while True:
            M = a + (b - a) / (1.5 + numpy.random.random())
            if (abs(f(M)) > EPS):
                break
        return GetBounds(f, a, M) + GetBounds(f, M, b)
    if (b - a < EPS):
        print("Warning: Bounds are too small")
    return [(a, b)]

Sturm = SturmSeq(f)

print("Amount of roots on [-10, 10]:")
print(N(Sturm, -10) - N(Sturm, 10))
    
bounds = GetBounds(f, -10, 10)
print("Roots are in bounds:")
print(bounds)


iters = 0

def HalfDivisionMethod(L, R):
    global iters
    iters += 1
    M = (L + R) / 2
    if (R - L < EPS):
        return M
    #if (abs(f(M)) < EPS):
    #    return M
    if (f(L) * f(M) <= 0):
        return HalfDivisionMethod(L, M)
    elif (f(R) * f(M) <= 0):
        return HalfDivisionMethod(M, R)
    else:
        raise RuntimeError("Error in Half Division Method")

def ChordMethod(L, R):
    global iters
    fder2 = numpy.polyder(f, 2)
    if (f(R) * fder2(R) > 0):
        (oldx, x) = (R, L)
    elif (f(L) * fder2(L) > 0):
        (oldx, x) = (L, R)
    else:
        raise ValueError("Bad bounds in first Secant method")
    t = oldx
    while (abs(x - oldx) > EPS):
        iters += 1
        oldx = x
        x = x - f(x) * (t - x) / (f(t) - f(x))
        if (not (numpy.isfinite(x))):
            raise RuntimeError("X is not a number")
    if ((x < L) or (R < x)):
        raise RuntimeError("X is not in [L, R]")
    return x
    
def ModifiedChordMethod(L, R):
    global iters
    (x, oldx) = (L, R)
    while (abs(x - oldx) > EPS):
    #while (abs(f(x)) > EPS):
        iters += 1
        oldx = x
        x = L - f(L) * (R - L) / (f(R) - f(L))
        if (not (numpy.isfinite(x))):
            raise RuntimeError("X is not a number")
        if (f(L) * f(x) <= 0):
            R = x
        elif (f(R) * f(x) <= 0):
            L = x
        else:
            raise RuntimeError("Error in second Secant method")
    if ((x < L) or (R < x)):
        raise RuntimeError("X is not in range")
    return x
    
def NewtonMethod(L, R):
    global iters
    fder = numpy.polyder(f)
    fder2 = numpy.polyder(f, 2)
    if (f(L) * fder2(L) > 0):
        (oldx, x) = (R, L)
    elif (f(R) * fder2(R) > 0):
        (oldx, x) = (L, R)
    else:
        raise ValueError("Bad bounds in Newton method")
    while (abs(x - oldx) > EPS):
        iters += 1
        oldx = x
        x = x - f(x) / fder(x)
        if (not (numpy.isfinite(x))):
            raise RuntimeError("X is not a number")
    if ((x < L) or (R < x)):
        raise RuntimeError("X is not in range")
    return x


numpy.set_printoptions(suppress = True, precision = 4, floatmode = "fixed")


def test(method):
    global iters
    for i in range(len(bounds)):
        iters = 0
        try:
            str = method(*bounds[i])
            if  (not str is None):
                str = "{:.4f}".format(str)
            print("{}  {} method ({} iterations)".format(str, method.__name__, iters))
        except Exception as ex:
            print("ERROR: {} - in {} method ({} iterations)".format(ex, method.__name__, iters))
    print()
    

test(HalfDivisionMethod)
test(ChordMethod)
test(ModifiedChordMethod)
test(NewtonMethod)

