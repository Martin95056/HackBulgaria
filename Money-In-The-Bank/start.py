import sql_manager
from cli import CLI


def main():
    sql_manager.create_database()
    cli = CLI()
    cli.start()

if __name__ == '__main__':
    main()
