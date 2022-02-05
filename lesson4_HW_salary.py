from sys import argv

script_name, first_parameter, second_parameter = argv

first_parameter = float(first_parameter)
second_parameter = float(second_parameter)
print(f'Учитывая количество отработанных часов и размер почасовой оплаты,\
      \nзаработная плата составит {first_parameter * second_parameter}.')
