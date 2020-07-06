import settings
import models
import updates
from commands import run, notify
from database import engine

models.Base.metadata.create_all(bind=engine)


def main():
    offset = None

    while True:
        notify()
        update = updates.get_oldest_update(updates.get_updates(offset))
        if not update:
            continue

        run(update)

        offset = updates.get_update_id(update) + 1


if __name__ == '__main__':
    main()
