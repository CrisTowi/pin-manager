# PIN Manager

## Run project

There are multiple ways to run this application in local environment:

- With python by installing all packages as global
- With python by installing all packages in a **virtualenv**
- Using docker Docker

Requirements:

- Ask for the `.env` file from a member of the team and place it in the `root` of the project.

### With global packages

```
pip install -r requirements.txt
python pin-manager.py
```

### With virtualenv

```
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python pin-manager.py
```

### With Docker

(You need to have installed docker and docker-compose)
`docker-compose up`

## Usage

### Endpoints

#### Assign pin

Assign a PIN to the card  with a password to retrieve later.

`POST - [base_url]/assign_pin`

```
{
 "card_id": "string",
 "password": "string",
 "pin": "string"
}
```

#### Retrieve PIN

Retrieve PIN from a card with the ID and the correct password.

`POST - [base_url]/retrieve_pin`

```
{
 "card_id": "string",
 "password": "string",
}
```

#### Reset password

Reset password from a card with the correct password and a new password to be assigned so clients are now able to retrieve the PIN again.

`PUT - [base_url]/reset_password`

```
{
 "card_id": "string",
 "new_password": "string",
 "password": "sting"
}
```
