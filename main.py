from neuron import Neuron

lst = [[0, 0], [0, 1], [1, 0], [1, 1]]
lst_not = [[1], [0]]

neuron_and = Neuron(1, -3/2)
neuron_or = Neuron(1, -1/2)
neuron_not = Neuron(-1, 1)

for i in lst:
    # print(neuron_and.compute_with_bias(i))
    # print(neuron_or.compute_with_bias(i))
    # print(neuron_and.calc_with_threshold(i))
    print(neuron_or.calc_with_threshold(i))
    pass
# for i in lst_not:
    # print(neuron_not.compute_with_bias(i))
    # print(neuron_not.calc_with_threshold(i))
