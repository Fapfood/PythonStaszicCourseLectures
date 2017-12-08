def snowflake(a, b, k, s):
    if k > 0:
        x_a = a[0]
        y_a = a[1]
        x_b = b[0]
        y_b = b[1]
        x_c = x_a + (x_b - x_a) * 1 / 3
        y_c = y_a + (y_b - y_a) * 1 / 3
        x_d = x_a + (x_b - x_a) * 2 / 3
        y_d = y_a + (y_b - y_a) * 2 / 3
        w_x = s * (y_d - y_c) * 3 ** (1 / 2) / 2
        w_y = -s * (x_d - x_c) * 3 ** (1 / 2) / 2
        x_e = (x_c + x_d) / 2 + w_x
        y_e = (y_c + y_d) / 2 + w_y
        l = snowflake((x_a, y_a), (x_c, y_c), k - 1, s)
        l += snowflake((x_c, y_c), (x_e, y_e), k - 1, s)[1:]
        l += snowflake((x_e, y_e), (x_d, y_d), k - 1, s)[1:]
        l += snowflake((x_d, y_d), (x_b, y_b), k - 1, s)[1:]
        return l
    else:
        return [a, b]
