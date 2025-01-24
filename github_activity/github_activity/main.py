from argparse import ArgumentParser
from github_activity.github_api_request import api_request

def main() -> None:
    parser = ArgumentParser(description="CLI GitHub User Activity.")
    parser.add_argument("username", type=str, help="GitHub username.") 
    
    args = parser.parse_args()
    print(api_request(args.username))
    
if __name__ == "__main__":
    main()