'''Python script to create a csv file containing data about people,
and relevant courts. Data about people is initially read in, and for each
person an API request is made to attain corresponding court data for that
person. This data is summarised in a csv file.'''

from typing import IO
import pandas as pd
import requests

API_BASE_URL = 'https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode='


def create_initial_dataframe(filename: str) -> pd.DataFrame:
    '''Returns a pandas dataframe containing all information
    stored in a csv file.'''

    return pd.read_csv(filename)


def call_api(postcode: str, court_type: str) -> dict:
    '''Makes a request to the courts and tribunals finder API
    using a postcode input as a query parameter and extracts the
    necessary information for the nearest relevant court,
    storing this in a dictionary.'''

    api_url = f'{API_BASE_URL}{postcode}'
    court_info = {}
    courts = []

    # Find all courts of the right type
    all_courts = requests.get(api_url, timeout=10).json()
    for court in all_courts:
        if court_type in court['types']:
            courts.append(court)

        # Case where no court matches the right type
        elif 'types' not in court.keys():
            court_info['court_name'] = 'Not Available'
            court_info['distance'] = 'Not Available'
            court_info['dx_number'] = 'Not Available'
            return court_info

    # Find the closest court of the right type
    distances = {}
    for court in courts:
        distances[court['distance']] = court

    distances = dict(sorted(distances.items(), key=lambda x: x[0]))
    closest_court = list(distances.values())[0]

    # Get relevant information from the nearest court
    court_info['court_name'] = closest_court['name']
    court_info['distance'] = closest_court['distance']

    if closest_court['dx_number'] is not None:
        court_info['dx_number'] = closest_court['dx_number']
    else:
        court_info['dx_number'] = 'Not Available'
    return court_info


def main(filename: str) -> IO:
    '''Returns a csv file containing all the required court information
    given a csv file containing names, postcodes, and desired courts.'''

    # Read in initial data into a dataframe
    df = create_initial_dataframe(filename)

    # Obtain the corresponding court information for each dataframe entry
    df['nearest_court'] = df.apply(lambda row: call_api(
        row['home_postcode'], row['looking_for_court_type'])['court_name'], axis=1)
    df['distance'] = df.apply(lambda row: call_api(
        row['home_postcode'], row['looking_for_court_type'])['distance'], axis=1)
    df['dx_number'] = df.apply(lambda row: call_api(
        row['home_postcode'], row['looking_for_court_type'])['dx_number'], axis=1)

    df.to_csv('court_data.csv', index=False)


if __name__ == "__main__":
    main('people.csv')
