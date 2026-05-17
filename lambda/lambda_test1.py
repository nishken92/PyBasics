n = 5
for i in range(5):
    print(i*i)

# Lambda Implementation

print("Lambda Implementation")

square_range = lambda x : [print(x*x) for i in range(x)]

square_range(5)