import store

def run():
    categories = store.get_categories()
    print(categories)


if __name__ == "__main__":
    run()