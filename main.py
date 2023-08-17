import scratchattach as scratch3
import os
session = scratch3.login("UserName", "password") # Add Username and Password
conn = session.connect_cloud("projectid") #replace with your project id

client = scratch3.CloudRequests(conn)
UserName = "" # Replace With Sign in Username
UserPass = "" # Replace With Sign in Userpass

@client.request
def auth(argument1, argument2): #called when client receives request
	print(f"User: {argument1} Pass:{argument2}")
	if argument1 == UserName:
		if argument2 == UserPass:
			print('Authorized 200(Ok)')
			return "200(Ok)"
		else:
			print("403(Forbidden)")
			return "403(Forbidden)"
	else:
		print("403(Forbidden)")
		return "403(Forbidden)"

@client.event
def on_ready():
	if os.name == 'posix':
	    os.system('clear')
	elif os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	print("Request handler is running")

client.run() #make sure this is ALWAYS at the bottom of your Python file
