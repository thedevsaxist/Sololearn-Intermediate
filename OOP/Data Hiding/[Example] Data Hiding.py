class Account:
    def __init__(self) -> None:
        self.username = "SpamEgg123"
        self._balance = 23500
        self.__password = "swo!rdfish"

    def show_info(self):
        return f"Username: {self.username} \nBalance: {self._balance} \nPassword: {self.__password}"

# obj as an instance of class Account
obj = Account()

print("--- Accessing Attributes from Outside the Class ---")

# username
print("Username:", obj.username)

# balance
print("Balance:", obj._balance)

# password - (obj._classname__attributes)
print("Password:", obj._Account__password)  # type: ignore

print("\n\n")


# Method inside the class have access to private attributes inside the class
print("--- Calls the show_info method ---")
print(obj.show_info())