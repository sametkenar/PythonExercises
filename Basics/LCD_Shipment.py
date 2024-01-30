LCD_WEIGHT = 63
EINK_WEIGHT = 30

lcd_count = int(input("Enter the number of LCD screens: "))

eink_count = int(input("Enter the number of e ink displays: "))

total_lcd_weight = LCD_WEIGHT * lcd_count
total_eink_weight = EINK_WEIGHT * eink_count

print("Total weight of LCD screens: {}".format(total_lcd_weight))
print("Total weight of e ink displays: {}".format(total_eink_weight))

