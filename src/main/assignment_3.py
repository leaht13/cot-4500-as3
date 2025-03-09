# Leah Tomberg

# Euler Method
a=0
b=2
N=10
f0=1
stepSize=(b-a)/N

# First have this f0 val then loop for rest
y2=f0
a2=a
for i in range(N):
    y2=y2+stepSize*(a2-y2**2)  
    a2=a2+stepSize

# Print y after 10 iterations
print(y2)


# Runge-Kutta
# We don't need to redeclare values (all the same)
def f(t, y3):
    return(t-y3**2)

# Reset our vals
a3=a
y3=f0

# Loop to get middle vals and then set new ones
for i in range(N):
    k1=stepSize*f(a3,y3)
    k2=stepSize*f(a3+stepSize/b,y3+k1/b)
    k3=stepSize*f(a3+stepSize/b,y3+k2/b)
    k4=stepSize*f(a3+stepSize,y3+k3)

    y3=y3+(1/6)*(k1+2*k2+2*k3+k4)
    a3=a3+stepSize

print(y3)


