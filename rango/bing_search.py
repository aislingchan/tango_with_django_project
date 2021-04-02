import json
import requests

""""Error when running this module on its own through the Command prompt"""

def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found')

    if not bing_api_key:
        raise KeyError('Bing key not found')

    return bing_api_key

def run_query(search_terms):
    bing_key = read_bing_key()
    #https://docs.microsoft.com/en-us/answers/questions/160048/request-to-bing-search-v7-api-unauthorized.html
    search_url = 'https://api.bing.microsoft.com/v7.0/search?' #The original url from twd textbook does not work anymore
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': search_terms, 'textDecorations': True, 'textFormat': 'HTML'}
    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        results = []
        for result in search_results['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet']})
        return results
    except Exception as e:
        print("An error has occurred: ")
        print(e)

def main():
    finished = False
    while not finished:
        search_terms = input('(Enter "." to quit) Search for: ')
        if search_terms == ".":
            finished = True
        else:
            results = run_query(search_terms)
            if results:
                for result in results:
                    print(result['title'] + "\n" + result['link'] + "\n" + result['summary'])
                    print("-------------------------------------------")

if __name__ == '__main__':
    main()