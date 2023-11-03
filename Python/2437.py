xm, ym, xr, yr = map(int, input().split())
diff_x = abs(xr-xm)
diff_y = abs(yr-ym)
diff = diff_x + diff_y
print(diff)
