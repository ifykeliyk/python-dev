def make_sandwitch(*ingridents, **options):
    print("Making a sandwitch with the following ingredients:")
    for ingridents in ingridents:
        print(f"{ingridents}")
    print("With the following options:")
    for key, value in options.items():
        print(f"{key} : {value}")


make_sandwitch("bread", "lettuce", "tomato", sauce="mayo")
make_sandwitch("bread", "cheese", "ham", sauce="mustard")
