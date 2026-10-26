
def display_resources(resources):
    if len(resources) == 0:
        print("No resources available")
    else:
        for r in resources:
            print(r)


def search_by_category(resources, category):
    found = False

    for r in resources:
        if r[2] == category:
            print(r)
            found = True

    if found == False:
        print("Category not found")


def find_unavailable(resources):
    found = False

    for r in resources:
        if r[3] == 0:
            print(r)
            found = True

    if found == False:
        print("All resources are available")


def search_by_id(resources, resource_id):
    found = False

    for r in resources:
        if r[0] == resource_id:
            print(r)
            found = True

    if found == False:
        print("Resource ID not found")


resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

print("All Resources:")
display_resources(resources)

print("\nElectronics Resources:")
search_by_category(resources, "Electronics")

print("\nUnavailable Resources:")
find_unavailable(resources)

print("\nSearch Resource by ID:")
resource_id = int(input("Enter an ID: "))
search_by_id(resources, resource_id)

print("\nTest Negative Quantity:")
quantity = int(input("Enter Quantity: "))

if quantity < 0:
    print("Quantity cannot be negative")
else:
    print("Quantity is valid")

print("\nTest Empty Resource List:")
display_resources([])
