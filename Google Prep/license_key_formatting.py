
def licenseKeyFormatting(s, k):
    s = s.replace("-", "").upper()[::-1]
    return "-".join(s[i:i+k] for i in range(0,len(s),k))[::-1]

def main():
    s1 = "5F3Z-2e-9-w"
    k1 = 4
    print(licenseKeyFormatting(s1, k1))

    s2 = "2-5g-3-J"
    k2 = 2
    print(licenseKeyFormatting(s2, k2))
main()
