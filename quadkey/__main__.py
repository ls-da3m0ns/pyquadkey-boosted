from .quadkey import lat_lng_to_quadkey

def main():
    return lat_lng_to_quadkey(37.7749, -122.4194, 12)


if __name__ == "__main__":
    print(main() )
