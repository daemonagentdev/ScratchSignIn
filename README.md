# Scratch Sign In

A sign in system for scratch


```zsh
git clone https://github.com/Happpydust/ScratchSignIn.git
cd Desktop
pip install -U scratchattach
```

Before you run the script, you need to configure line 3, 4, 8 and 7

```python
session = scratch3.login("UserName", "password") # Add Username and Password
conn = session.connect_cloud("projectid") #replace with your project id

UserName = "" # Replace With Sign in Username
UserPass = "" # Replace With Sign in Userpass

```