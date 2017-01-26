"""First Problem"""
import argparse

def hello(name='World'):
    """Simple name printer"""
    if not name:
        name = "World"
    return "Hello, {}!".format(name)

def main():
    """Main wrapper"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Your name", action="store")
    args = parser.parse_args()
    if args.name:
        print(hello(args.name))
    else:
        print(hello())

if __name__ == '__main__':
    try:
        main()
    finally:
        print("\nProgram terminated\n")
