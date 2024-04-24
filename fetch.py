from bs4 import BeautifulSoup
import requests

import datetime

def fetch():
    base_url = "https://www.weather-atlas.com/en/brazil/"

    url_exts = [
        "sao-paulo", "rio-de-janeiro",
        "brasilia", "salvador", "fortaleza", "belo-horizonte", "manaus",
        #"curitiba", "recife", "porto-alegre", "goiania", "guarulhos", "campinas", "são-luis", "são-goncalo",
        #"maceio", "duque-de-caxias", "natal", "teresina", "são-bernardo-do-campo", "nova-iguacu", "joao-pessoa",
        #"santo-andre", "osasco", "jaboatao-dos-guararapes", "são-jose-dos-campos", "ribeirao-preto", "uberlandia",
        #"contagem", "sorocaba", "aracaju", "cuiaba", "juiz-de-fora", "joinville", "londrina", "niteroi",
    ]

    cur_date = datetime.datetime.now()
    cur_date = str(cur_date).split('.')[0].split(' ')

    fetch_bulk = []

    for ext in url_exts:
        url = base_url + ext

        print(f"Parsing.... \"{url}\"")

        html_response = requests.get(url, timeout=10)
        if not html_response.ok:
            print(f"Invalid html response: {html_response}")
            exit(1)

        print(f"Status: {html_response.status_code}\t'OK'")

        html = BeautifulSoup(html_response.text, "lxml")

        try:
            min_t, max_t = ( html.find("span", class_="text-primary"), html.find("span", class_="text-danger"),)
            if min_t == None:
                min_t = "_"
            else:
                if 'min' in min_t.text:
                    min_t = min_t.text.split('.')[1].split('°')[0]
                else:
                    min_t = min_t.text.split('C')[0][:-1]

            if max_t == None:
                max_t = "_"
            else:
                if 'max' in max_t.text:
                    max_t = max_t.text.split('.')[1].split('°')[0]
                else:
                    max_t = max_t.text.split('C')[0][:-1]


            data = html.find("ul",  class_="list-unstyled").text
            data = data.split(':')
            wind, wind_dir, humidity, precipitation_prob, precipitation, UV_index = (
                data[1].split('k')[0],
                data[1].split(' ')[-1].split('H')[0],
                data[2].split('%')[0],
                data[3].split('%')[0],
                data[4].split("mmU")[0],
                data[5]
            )
        except AttributeError as err:
            print(f" == unable to fetch {url}, continuing")
            print(err)
            continue

        fetch_bulk.append(cur_date + [ext, min_t, max_t, wind, wind_dir, humidity, precipitation_prob, precipitation, UV_index])

    return fetch_bulk

# dev-test
if __name__ == "__main__":
    res = fetch()
    for r in res:
        print(r)
