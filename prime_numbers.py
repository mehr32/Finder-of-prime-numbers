def avval_i(n):
    for a in range(2, int(n**0.5)+1):
        avval = True
        if n % a == 0:
            avval = False
            break
        return avval

adad = int(input("adad ra wared conid: "))
prime_count = 0
for i in range(0, adad):
    if avval_i(i):
        prime_count = prime_count + 1

print(f"thedad aedad avval dar in ranj : {prime_count}")
