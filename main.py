#  Write a recursive program that calculate factorial like f(4)=4*3*2*1=24
def main(x):
    def factorial(n):
        if n == 1: # n=1, f(n)=1
            return 1
        else:
            return factorial(n-1)*n  # n*f(n-1)
    return factorial(x)

print(main(5))
quit()
# Hardly to write comment because it is too short =(