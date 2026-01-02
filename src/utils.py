def generate_unique_id_generator():
    _id = 1
    while True:
        yield _id
        _id += 1

# Instantiate the generator
get_unique_id = generate_unique_id_generator()
