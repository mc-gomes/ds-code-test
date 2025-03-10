# Goals
- Write a python script to import data to [MongoDB](https://www.mongodb.com/).
- Implement a functional CRUD using [VueJS](https://vuejs.org/guide/introduction.html) and [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/).


obs.: The imported data should then be displayed on the CRUD application, they both will use the same database and collection `users`
	
# Detail
### Import Script
There will be a JSON file below that includes all the data to be imported using this script, you will need to parse the data and insert it in the MongoDB database on the `users` collection.

Use the following dataclasses to load the data, that's the format the data should be inserted into the database.
```python
@dataclass
class User:
	username: str
	password: str
	roles: list
	preferences: UserPreferences
	active: bool = True
	created_ts: float
```

```python
@dataclass
class UserPreferences:
	timezone: str
```

```
For the roles you parse like this:
is_user_admin -> admin
is_user_manager -> manager
etc...
```
### CRUD
obs.: YOU MUST USE A UI LIBRARY FOR THIS PART, IT CAN BE ANY VUE LIBRARY. e.g: [Vuetify](https://vuetifyjs.com/en/)

Also keep in mind that the idea is that someone else will use those pages and not you, so actions need to be clear and not dirupt the page structure, just make sure it works like something you would be ok to use if you were the user.

This will be a website with 2 pages, the first and main one is a table displaying the users with the actions. The second one is an individual user page, with the information about a single user.
#### Main Page
- A button somewhere on the page for the `create` action.
- A table listing all the users with the following columns: 
  ```
  Username | Roles | Timezone | Is Active? | Last Updated At | Created At | Actions
  ```
- The username needs to be a link to the user individual page.
- The `Actions` column needs to have these actions: `edit` and `delete`.
- Both `edit` and `delete` need some sort of confirmation before executing.
- To display the fields for `create`and `edit` you can make it however you want but it's recommended to use a modal / dialog in a reusable component. (Need to be intuitive and not disrupt the page flow)
#### User Page
- Just a page listing the same fields as in the columns.
- Need to also be able to `edit` or `delete` the user from this page
# Delivery
EVERYTHING BELOW IS MANDATORY.

Create a a github repository and add the project there, it should include:
- The json given on this task.
- A parser file `parser.py` that will parse the json and add it into the MongoDB `users` collection.
- The files for the client / server.
- A README.md file containing instructions on how to run everything.
