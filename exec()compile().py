import os
import math
import time

files_to_process = [
    r"C:\Users\48735\PycharmProjects\Średnio zaawansowany\math_sin_square.py",
    r"C:\Users\48735\PycharmProjects\Średnio zaawansowany\math_square_root.py"
    ]
for file in files_to_process:
    with open(file, 'r') as f:
        print("File {}".format(os.path.basename(file)))
        source = f.read()
        exec(source)

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000):
    argument_list.append(i/10)

for formula in formulas_list:
    print(formula)
    start = time.time()
    result_list = []
    for x in argument_list:
        result = eval(formula)
        result_list.append(result)
        print(result_list)
   # print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
 #   print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time: {}".format(stop - start))