from matplotlib.pyplot import plot, show
from recursion.code.snowflake import snowflake

snow = snowflake((0, 0), (0.9, 0), 2, -1)
xs, ys = zip(*snow)
plot(xs, ys, 'b')

snow = snowflake((0, 0), (0.45, -0.45 * 3 ** 0.5), 2, 1)
xs, ys = zip(*snow)
plot(xs, ys, 'b')

snow = snowflake((0.45, -0.45 * 3 ** 0.5), (0.9, 0), 2, 1)
xs, ys = zip(*snow)
plot(xs, ys, 'b')

show()
