#WAF to print the element of list in a single line (list in parameter)
country = ["Nepal", "India", "Canada", "China", "America"]
cities = ["Kathmandu", "Bhaktapur", "Lalitpur", "Nuwakot"]
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)

print()
