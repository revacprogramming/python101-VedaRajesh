
# Functions
def computepay(h,r):
    if h > 40:
        otp = (1.5 * r) * (h - 40) 
        reg=r*h
        v=otp+reg
    else:
        p = h * r
    return p
    
hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print(p)



