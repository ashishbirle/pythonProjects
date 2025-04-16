import requests

def get_person_id(name, api_key):
    url = "https://api.themoviedb.org/3/search/person"
    params  = {
        "api_key": api_key,
        "query": name
    }
    response = requests.get(url, params=params)

    data = response.json()
    results = data.get("results", [])

    if results:
        person = results[0]
        return person['id'], person['known_for']
    return None, []

def get_movie_credits(person_id, api_key):
    url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("cast", [])

if __name__ == "__main__":
    name = input("Enter a celebrity's name: ")
    api_key = "a8d8caafe03ce36a91157bdae4bffa0a"

    person_id, known_for = get_person_id(name, api_key)

    if person_id:
        print(f"\n {name} is known for:")
        for item in known_for:
            print(f". {item.get('title') or item.get('name')}")
        
        print(f"\n Movies {name} appeared in:")
        credits = get_movie_credits(person_id, api_key)
        for movie in sorted(credits, key=lambda x: x.get("release_date", "0000"), reverse=True):
            print(f"{movie.get('title')} ({movie.get('release_date', 'N/A')})")
    
    else:
        print("No results found.")