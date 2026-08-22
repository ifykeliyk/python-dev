import time


def timer_dec(base_fn):
    def enhanced_func(*args, **kwargs):
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken: {time_taken} seconds")
    return enhanced_func


@timer_dec
def make_coffee(coffee_type, steep_time):
    print(f"Making a cup of {coffee_type} coffee...")
    time.sleep(steep_time)
    print(f"{coffee_type} coffee is ready!")


@timer_dec
def brew_tea():
    print(f"Making a cup of tea...")
    time.sleep(1)
    print(f"Tea is ready!")


brew_tea()
make_coffee("Espresso", 2)
