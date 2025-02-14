
'''

# 8.25*10**(-6) - (-2.4*(10**(-6)))
# abs(0.446 - 1.078)

0.0067308

'''

# 50 g tapaus
x_diff = 8.25*10**(-6) - (-2.4*(10**(-6)))
y_diff = abs(0.446 - 1.078)*1000 # Times a thousand for kilopascals

area = x_diff*y_diff
print("Pinta-ala (50g): "+str(area))




# 100 g tapaus
# x_diff = 8.25*10**(-6) - (-2.4*(10**(-6)))
# y_diff = abs(0.446 - 1.078)*1000 # Times a thousand for kilopascals

x_diff = (8.33*(10**(-6))) - (-1.05*10**(-6))
y_diff = abs(0.443 - 1.62)*1000

area = x_diff*y_diff
print("Pinta-ala (100g): "+str(area))



# 150 g tapaus

x_diff = (1*(10**(-5))) - (-1.25*10**(-6))
y_diff = abs(0.507 - 2.31)*1000

area = x_diff*y_diff
print("Pinta-ala (150g): "+str(area))

