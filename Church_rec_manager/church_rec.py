# from ui.App import App
import os

def config_setup():
    if not os.path.exists('.env'):
        print("\nConfiguring your application:")
        db_host = input("Enter DB_HOST [localhost]: ") or "localhost"
        db_port = input("Enter DB_PORT [3306]: ") or "3306"
        db_user = input("Enter DB_USER [username]: ") or "username"
        db_password = input("Enter DB_PASSWORD [password]: ") or "password"

        config_content = f"""
                DB_HOST={db_host}
                DB="Church_db"
                PORT={db_port}
                DB_PASSWORD={db_password}
                DB_USER={db_user}
                BAPTISM_ARCHIVE="./.Archives/Baptism"
                MARRIAGE_ARCHIVE="./.Archives/Marriage"
                DEATH_ARCHIVE="./.Archives/Death"
                """

        with open('.env', 'w') as config_file:
            config_file.write(config_content)

        print("\nConfiguration completed successfully!")
    else:
        print("\n.env file already exists. Skipping configuration.")


def Main():
    config_setup()
    from Church_rec_manager.ui.App import App
    app = App()
    app.mainloop()


if __name__ == '__main__':
    Main()
