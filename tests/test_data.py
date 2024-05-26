import faker

fake = faker.Faker()

def generate_test_data(num_users=10):
    test_data = []
    for _ in range(num_users):
        preferences = {'genres': [fake.word() for _ in range(3)]}
        test_data.append(preferences)
    return test_data
