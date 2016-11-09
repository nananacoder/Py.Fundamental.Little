

import pygal                                                       # First import pygal




bar_chart = pygal.Bar() # create a bar graph object
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) # add some values
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file('bar_chart.svg') # save the svg to a file


bar_chart_2 = pygal.StackedBar()
bar_chart_2.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart_2.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart_2.render_to_file('stackedbar_chart.svg')


bar_chart_h = pygal.HorizontalStackedBar()
bar_chart_h.title = "Remarquable sequences"
bar_chart_h.x_labels = map(str, range(11))
bar_chart_h.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart_h.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart_h.render_to_file('hor_stack_chart.svg')
