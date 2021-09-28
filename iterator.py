import json
import wikipediaapi


class UrlWiki:

    def __init__(self, start, country_file_path):
        self.start = start - 1
        self.country_file_path = country_file_path

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        wiki = wikipediaapi.Wikipedia('en')
        with open(self.country_file_path, encoding='utf-8') as file:
            countries_data = json.load(file)
            end = len(countries_data)
            if self.start == end:
                raise StopIteration
            country_names = countries_data[self.start]['name']['common']
            country_page = wiki.page(country_names)
            country_link = country_page.fullurl
            recording = f'{country_names} - {country_link}'
        return recording


if __name__ == '__main__':
    with open('countries_links.txt', 'w', encoding='utf8') as f:
        for line in UrlWiki(0, 'countries.json'):
            f.write(line + '\n')