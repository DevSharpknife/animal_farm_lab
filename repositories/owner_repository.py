from db.run_sql import run_sql

from models.owner import Owner
from models.animal import Animal


def save(owner):
    sql = "INSERT INTO owners (owner_name) VALUES (%s) RETURNING *"
    values = [owner.owner_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner


def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['owner_name'], row['id'])
        owners.append(owner)
    return owners


def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['owner_name'], result['id'])
    return owner