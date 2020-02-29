from neuron import Neuron

lst = [[0, 0], [0, 1], [1, 0], [1, 1]]
lst_not = [[1], [0]]

neuron_and = Neuron(1, -3/2)
neuron_or = Neuron(1, -1/2)
neuron_not = Neuron(-1, 1)

# or line in data2:
#     print(line, "\t", and_n.compute_with_bias(line),
#           "\t", or_n.compute_with_bias(line))
print("Таблица истинности на смещении\nTable\tAND\tOR")
for i in lst:
    print(i, "\t", neuron_and.compute_with_bias(i), "\t", neuron_or.compute_with_bias(i))
print("\nTable\tNOT")
for i in lst_not:
    print(i, "\t", neuron_not.compute_with_bias(i))

print("\n\nТаблица истинности через пограничные значения\nTable\tAND\tOR")
for i in lst:
    print(i, "\t", neuron_and.calc_with_threshold(i),
          "\t", neuron_or.calc_with_threshold(i))

print("\nTable\tNOT")
for i in lst_not:
    print(i, "\t", neuron_not.calc_with_threshold(i))
    # print(neuron_or.compute_with_bias(i))
    # print(neuron_and.calc_with_threshold(i))
    # print(neuron_or.calc_with_threshold(i))
# for i in lst_not:
    # print(neuron_not.compute_with_bias(i))
    # print(neuron_not.calc_with_threshold(i))
