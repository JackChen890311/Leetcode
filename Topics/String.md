 - Basic string manipulation
	 ```python
	 s = "abc"
	 s.isalpha() # True
	 s.isalnum() # True
	 
	 s.isdecimal() # False
	 s.isdigit() # False
	 s.isnumeric() # False
	 # https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
	 
	 s.find("a") # 0
	 s.replace("a", "d") # "dbc"
	 
	 s.lower() # abc
	 s.upper() # ABC
	 
	 s = "abc def"
	 s.title() # Abc Def
	 s.capitalize() # Abc def
	
	 s = "abc "
	 # Remove space and newline
	 s.strip() # abc
	 # or specified character
	 s.strip("a") # "bc "	 
	 ```