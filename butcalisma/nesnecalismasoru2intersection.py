def main():
    cumle1=set(str(input("bir cümle giriniz: ")))
    cumle2=set(str(input("bir cümle daha giriniz: ")))

    ortakharfler=cumle1.intersection(cumle2)
    print("Ortak Harfler : ")

    for x in ortakharfler:
        print(x)

if __name__ == "__main__":
    main()


