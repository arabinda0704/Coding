def find_gcd(a,b):
    if b==0:
        return a
    return find_gcd(b,a%b)
            
    
def main():
    n1 = 13
    n2 = 91

    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()