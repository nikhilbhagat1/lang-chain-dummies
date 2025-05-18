import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if (mock):
        linkedin_profile_url = "https://gist.githubusercontent.com/nikhilbhagat1/21685f2982c27d0bb8dc098d4d36b84a/raw/35c62088b101df5b41cc3eab04b3156ee31d2cd9/nikhilbhagat-scrapin.json"
        response = requests.get(url=linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {"linkedInUrl": linkedin_profile_url, "apikey": os.environ.get("PROXYCURL_API_KEY")},
        response = requests.get(api_endpoint,
                                params=params,
                                timeout=10)

    data = response.json().get("person")
    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile("", True)
    )
