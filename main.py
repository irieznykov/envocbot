from dotenv import load_dotenv

import models
import updates
from commands import run
from database import engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)


def main():
    offset = None

    while True:

        update = updates.get_oldest_update(updates.get_updates(offset))
        if not update:
            continue

        run(update)

        offset = updates.get_update_id(update) + 1


if __name__ == '__main__':
    main()
