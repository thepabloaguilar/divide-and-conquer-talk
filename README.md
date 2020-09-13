# Divide and Conquer - Workshop

[Slides](https://thepabloaguilar.github.io/divide-and-conquer-talk/)

## How to run the code

```sh
docker-compose up -d
poetry install
FLASK_APP="$(pwd)/divide_conquer/boot.py" flask initdb
FLASK_APP="$(pwd)/divide_conquer/boot.py" flask run
```
