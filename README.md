
# Lisa Chats

Small project for making chatting something interestring again.



## Authors



- [@mrdili131](https://www.github.com/mrdili131)


## Running Tests

Creating virtual env

```bash
  python -m venv venv
```
Installing needed libraries

```bash
  venv\Scripts\activate && pip install django channels daphne[standard]
```

Running the application

```bash
  daphne conf.asgi:application --reload
```



