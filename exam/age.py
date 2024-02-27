# Description: Define a function that receives an age and returns if the person is an adult or not.
def is_adult(age):
    if age >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

# Examples
def main():
    print(is_adult(20))  # Mayor de edad
    print(is_adult(15))  # Menor de edad
    print(is_adult(18))  # Mayor de edad
    
main()